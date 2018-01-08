from django.shortcuts import render
from django.utils import timezone
from .models import Post, Comment
from .forms import Post_New_Comment
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
        {'posts': posts, 'comments': comments}
    )


def post_id(request, post_id):
    post = Post.objects.get(pk=post_id)
    comments = Comment.objects.filter(post=post_id)
    return render(
        request,
        'blog/post.html',
        {'post': post, 'comments': comments}
    )


def post_new_comment(request, post_id):
    if request.method == 'POST':
        print(request.POST)
        text = request.POST["post_new_comment"]
#        author =
#        content = models.TextField()
#        post = models.ForeignKey(Post, on_delete=models.CASCADE)
#        created_date = models.DateTimeField(auto_now_add=True)
#        last_updated = models.DateTimeField(auto_now=True)
        author = get_user_model().objects.get(username="admin")
#        print(author)
        post = Post.objects.get(pk=post_id)
        Comment.objects.create(author=author, content=text, post=post)
    return HttpResponseRedirect('/')
