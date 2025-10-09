from django.test import TestCase
from datetime import datetime


from accounts.models import User, Profile
from blog.models import Post

class TestModel(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(email='test@test.com',password='/@1234567')
        self.profile = Profile.objects.create(
            user = self.user,
            first_name = 'test_first_name',
            last_name = 'test_last_name',
            description = 'test_description'
        )

    def test_post_create_with_valid_data(self):
        post = Post.objects.create(
            author = self.profile,
            status = True,
            title = 'testing',
            content = 'this is context',
            category = None,
            published_date = datetime.now()
        )

        self.assertTrue(Post.objects.filter(pk=post.id).exists())
        self.assertEqual(post.title, 'testing')