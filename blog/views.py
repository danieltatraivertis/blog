from django.shortcuts import render
from django.utils import timezone
from .models import Post, Comment
from .forms import CommentForm
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect


# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now())
    posts = posts.order_by('published_date')
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
        print(request.user)
        if form.is_valid():
            author = get_user_model().objects.get(username=request.user)
            post = Post.objects.get(pk=post_id)
            Comment.objects.create(
                author=author,
                content=form.cleaned_data.pop("new_comment"),
                post=post
            )
        else:
            return HttpResponseRedirect("/")
    return HttpResponseRedirect('/')
