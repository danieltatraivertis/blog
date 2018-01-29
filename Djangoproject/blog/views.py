from django.shortcuts import render
from django.utils import timezone
from .models import Post, Comment
from .forms import CommentForm
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from rest_framework import viewsets
from .serializers import PostSerializer, CommentSerializer
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from rest_framework.response import Response
from rest_framework.status import HTTP_403_FORBIDDEN


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
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


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
