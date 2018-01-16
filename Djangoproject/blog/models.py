from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
# Create your models here.


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE,)
    title = models.CharField(max_length=200)
    picture = models.ImageField(
        upload_to="blog/static/picture",
        help_text="The image picture of lab member",
        blank=True
    )
    text = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE,)
    content = RichTextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content
