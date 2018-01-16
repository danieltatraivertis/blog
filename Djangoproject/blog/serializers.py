from rest_framework import serializers
from .models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    author = serializers.CharField(
        read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'author', 'title', 'text')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
