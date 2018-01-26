from django.test import TestCase
from blog.models import Post, Comment
from django.contrib.auth.models import User


class PostTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up data for the whole TestCase
        author = User.objects.create(username='valami', password='')
        cls.post = Post.objects.create(
            author=author,
            title='title',
        )

    def test__str__(self):
        # Some test using self.foo
        self.assertEqual('title', self.post.__str__())

    def test_publish(self):
        self.post.publish()
        self.assertNotEqual(self.post.published_date, None)


class CommentTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        author = User.objects.create(username='valami', password='')
        post = Post.objects.create(author=author, title='cim')
        cls.comment = Comment.objects.create(
            post=post,
            author=author,
            content='betta'
        )

    def test__str__(self):
        self.assertEqual('betta', self.comment.__str__())
