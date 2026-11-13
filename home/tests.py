from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class HomePageTests(TestCase):
    def test_homepage_loads_with_base_template(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_favourites_show_seven_dishes_with_controls(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, 'class="favourite-card', count=7)
        self.assertContains(response, 'favourites.js')
        self.assertContains(response, 'Steak Pie')
        self.assertContains(response, 'Cheesecake')

    def test_anonymous_user_sees_login_and_register_links(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, reverse('account_login'))
        self.assertContains(response, reverse('account_signup'))
        self.assertNotContains(response, reverse('account_logout'))

    def test_logged_in_user_sees_logout_link(self):
        user = get_user_model().objects.create_user(
            username='guest', email='guest@example.com', password='Ferry-pass-123'
        )
        self.client.force_login(user)
        response = self.client.get(reverse('home'))
        self.assertContains(response, reverse('account_logout'))
        self.assertNotContains(response, reverse('account_signup'))


class AccountPageTests(TestCase):
    def test_signup_page_uses_site_layout(self):
        response = self.client.get(reverse('account_signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')

    def test_user_can_register_with_email(self):
        response = self.client.post(reverse('account_signup'), {
            'email': 'new@example.com',
            'password1': 'Ferry-pass-123',
            'password2': 'Ferry-pass-123',
        })
        self.assertRedirects(response, reverse('home'))
        self.assertTrue(
            get_user_model().objects.filter(email='new@example.com').exists()
        )
    def test_logout_page_has_cancel_link(self):
        user = get_user_model().objects.create_user(
            username='guest', email='guest@example.com', password='Ferry-pass-123'
        )
        self.client.force_login(user)
        response = self.client.get(reverse('account_logout'))
        self.assertContains(response, 'Cancel')
        self.assertContains(response, 'btn btn-success')
