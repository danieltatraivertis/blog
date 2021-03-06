from django.contrib import admin
from .models import Post
from .models import Comment
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_filter = ['published_date']


# Only for test autocomplete_fields, deletable
class CommentAdmin(admin.ModelAdmin):
    autocomplete_fields = ['post']


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
