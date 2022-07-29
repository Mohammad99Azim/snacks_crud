from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import Snack


# Create your tests here.

class SnacksTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='test',
            email='test@test.com',
            password='test@12345'
        )
        self.snack = Snack.objects.create(
            title="Test",
            purchaser=self.user,
            description="test description description description"
        )

    def test_list_view(self):
        url = reverse('snacks_list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'snack_list.html')

    def test_detail_view(self):
        url = reverse('snack_detail', args=[self.snack.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'snack_detail.html')

    def test_create_view(self):
        url = reverse('create_snack')
        data = {
            "title": "Test Create",
            "purchaser": self.user.id,
            "description": "test description description description"
        }
        response = self.client.post(path=url, data=data, follow=True)
        self.assertTemplateUsed(response, "snack_detail.html")
        self.assertRedirects(response, reverse("snack_detail", args=[2]))

    def test_update_view(self):
        url = reverse('update_snack', args=[self.snack.id])
        data = {
            "title": "Edited",
            "purchaser": self.user.id,
            "description": "test description description description"
        }
        response = self.client.post(path=url, data=data, follow=True)

        self.assertEqual(self.snack.title, "Test")
        self.assertTemplateUsed(response, "snack_detail.html")
        self.assertRedirects(response, reverse("snack_detail", args=[self.snack.id]))

    def test_delete_view(self):
        url = reverse('delete_snack', args=[self.snack.id])

        response = self.client.post(path=url, follow=True)

        self.assertTemplateUsed(response, "snack_list.html")
        self.assertRedirects(response, reverse("snacks_list"))


    def test_string_representation(self):
        snack = Snack(title="My entry title")
        self.assertEqual(str(snack), snack.title)

    def test_all_model_fields(self):
        self.assertEqual(self.snack.title, "Test")
        self.assertEqual(self.snack.purchaser, self.user)
        self.assertEqual(self.snack.description, "test description description description")

