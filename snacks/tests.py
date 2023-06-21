from django.test import TestCase

# Create your tests here.
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import Snack


class ThingsTests(TestCase):
    def setUp(self):
        purchaser = get_user_model().objects.create(username="tester",password="tester")
        Snack.objects.create(name="rake", purchaser=purchaser)

    def test_list_page_status_code(self):
        url = reverse('snacks')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_list_page_template(self):
        url = reverse('snacks')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_list.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_list_page_context(self):
        url = reverse('snacks')
        response = self.client.get(url)
        things = response.context['snacks']
        self.assertEqual(len(things), 1)
        self.assertEqual(things[0].name, "rake")
        self.assertEqual(things[0].purchaser.username, "tester")

    def test_detail_page_status_code(self):
        url = reverse('snack_detail',args=(1,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_detail_page_template(self):
        url = reverse('snack_detail',args=(1,))
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_detail.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_detail_page_context(self):
        url = reverse('snack_detail',args=(1,))
        response = self.client.get(url)
        snack = response.context['snack']
        self.assertEqual(snack.name, "rake")
        self.assertEqual(snack.purchaser.username, "tester")

    def test_create_page_status_code(self):
        url = reverse('snack_create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_delete_page_status_code(self):
        url = reverse('snack_delete',args=(1,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_page_status_code(self):
        url = reverse('snack_update',args=(1,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_page_template(self):
        url = reverse('snack_update',args=(1,))
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_update.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_update_page_context(self):
        url = reverse('snack_update',args=(1,))
        response = self.client.get(url)
        snack = response.context['snack']
        self.assertEqual(snack.name, "rake")
        self.assertEqual(snack.purchaser.username, "tester")

    def test_create_page_template(self):
        url = reverse('snack_create')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_create.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_create_page_context(self):
        url = reverse('snack_create')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_create.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_delete_page_template(self):
        url = reverse('snack_delete',args=(1,))
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_delete.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_delete_page_context(self):
        url = reverse('snack_delete',args=(1,))
        response = self.client.get(url)
        snack = response.context['snack']
        self.assertEqual(snack.name, "rake")
        self.assertEqual(snack.purchaser.username, "tester")
