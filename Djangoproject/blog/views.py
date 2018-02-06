from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Post, Comment
from .forms import CommentForm
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from .forms import SignUpForm
from django.contrib.auth import login
from rest_framework import viewsets
from .serializers import PostSerializer, CommentSerializer
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from rest_framework.response import Response
from rest_framework.status import HTTP_403_FORBIDDEN
from django.utils import translation
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.models import User
from django.core.mail import send_mail


# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now())
    posts = posts.order_by('-published_date')
    comments = Comment.objects.order_by('created_date')
    return render(
        request,
        'blog/post_list.html',
        {'posts': posts, 'comments': comments, 'form': CommentForm()}
    )


def post_detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    comments = Comment.objects.filter(post=post_id)
    return render(
        request,
        'blog/post.html',
        {'post': post, 'comments': comments, 'form': CommentForm()}
    )


def post_new_comment(request, post_id):
    if request.method == 'POST':
        if request.user.is_authenticated is False:
            return HttpResponseRedirect("/accounts/login/")

        form = CommentForm(request.POST)
        if form.is_valid():
            author = get_user_model().objects.get(username=request.user)
            post = Post.objects.get(pk=post_id)
            Comment.objects.create(
                author=author,
                content=form.cleaned_data.pop("new_comment"),
                post=post
            )
    return HttpResponseRedirect('/')


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'Activate Your MySite Account'
            message = render_to_string('registration/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token': account_activation_token.make_token(user),
            })
            send_mail(subject, message, 'bot@vertis.com', [user.email])
            return redirect('account_activation_sent')
    else:
        form = SignUpForm()
    return render(request, 'registration/register.html', {'form': form})

    #         username = form.cleaned_data.get('username')
    #         raw_password = form.cleaned_data.get('password1')
    #         user = authenticate(username=username, password=raw_password)
    #         login(request, user)
    #         return HttpResponseRedirect('/')
    # else:
    #     form = SignUpForm()
    # return render(request, 'registration/register.html', {'form': form})


def set_lang(request, lang):
    user_language = lang
    translation.activate(user_language)
    request.session[translation.LANGUAGE_SESSION_KEY] = user_language
    return HttpResponseRedirect('/')


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('index')
    else:
        return redirect('account_activation_invalid')


def account_activation_sent(request):
    return render(request, 'registration/account_activation_sent.html')


def account_activation_invalid(request):
    return render(request, 'registration/account_activation_invalid.html')


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly,)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_fields = ('post',)

    def destroy(self, request, *args, **kwargs):
        if (
            request.user == self.get_object().author or
            request.user.is_superuser
        ):
            return super(CommentViewSet, self).destroy(
                request, *args, **kwargs)
        return Response("Forbidden", status=HTTP_403_FORBIDDEN)
