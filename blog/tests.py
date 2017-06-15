from django.test import TestCase
from blog.models import Post
from django.contrib.auth.models import User

class PostTestCase(TestCase):
    def setUp(self):
	user = User.objects.create_user(username='Ana', email='some@email.com', password='onion')
	Post.objects.create(author=user, title="Test Case", text="This is a test.")
	Post.objects.create(author=user, title="Another Test Case", text="This is another test.")
    
    def test_posts(self):
	a = Post.objects.get(title = "Test Case")
	t = Post.objects.get(title = "Another Test Case")
	self.assertEqual(str(a), "Test Case")
	self.assertEqual(str(t), "Another Test Case")

