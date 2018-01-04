from django.shortcuts import render
from django.utils import timezone
from .models import Post


# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now())
    posts = posts.order_by('published_date')
    return render(
        request,
        'blog/post_list.html',
        {'posts': posts, 'post_list': 4567}
    )


def post_id(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'blog/post.html', {'post': post})
