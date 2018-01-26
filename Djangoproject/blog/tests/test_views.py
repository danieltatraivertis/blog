from django.test import TestCase
from django.test import Client
from blog.models import Post, Comment
from django.contrib.auth.models import User


class ViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.c = Client()
        author = User.objects.create(username='valami', password='')
        cls.post = Post.objects.create(
            author=author,
            title='betta',
        )
        cls.post_id = cls.post.id

    def test_post_list(self):
        response = self.c.post('')
        self.assertEqual(response.status_code, 200)
        response = self.c.get('')
        self.assertNotEqual(response.content, '')

    def test_post_new_comment(self):
        response = self.c.post('/'+str(self.post_id)+'/post_new_comment/')
        print(response.content)

        print(response.status_code)
        self.assertNotEqual(response.status_code, 200)

    def test_register(self):
        response = self.c.post('/register/')

        self.assertEqual(response.status_code, 200)
