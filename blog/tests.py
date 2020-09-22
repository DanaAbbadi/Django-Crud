from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import Post
from django.urls import reverse
# Create your tests here.

class BlogTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='dana',
            email='dana@gmail.com',
            password='password'
        )

        self.post = Post.objects.create(
            title='oranges',
            author=self.user,
            body='Vitmain C',
        )

    def test_string_representation(self):
        post = Post(title='title')
        self.assertEqual(str(post), post.title)

    def test_all_fields(self):
        
        self.assertEqual(str(self.post), 'oranges')
        self.assertEqual(f'{self.post.author}', 'dana')
        self.assertEqual(self.post.body, 'Vitmain C')


    def test_blog_list_view(self):
        response = self.client.get(reverse('blog'))
        self.assertEqual(response.status_code, 200)

    def test_details_view(self):
        response = self.client.get(reverse('details', args='1'))
        self.assertEqual(response.status_code, 200)

    def test_update_view(self):
        response = self.client.post(reverse('update', args='1'), {
            'title': 'Phoebe',
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Phoebe')

    def test_create_view(self):
        response = self.client.post(reverse('new'), {
            'title': 'Phoebe',
            'author': self.user,
            'body' :'Vitmain C',
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Phoebe')
        self.assertContains(response, 'Vitmain C')
        self.assertContains(response, 'dana')

    def test_delete_view(self):
        response = self.client.get(reverse('delete', args='1'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Are you sure you want to delete?')

        post_response = self.client.post(reverse('delete', args='1'))
        self.assertRedirects(post_response, reverse('blog'), status_code=302)



        