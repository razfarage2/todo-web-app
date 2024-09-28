from django.test import TestCase, Client
from django.urls import reverse
from .models import Task
from django.contrib.auth import get_user_model
import json

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')  # Log in the user
        self.task = Task.objects.create(title='Test Task', description='Test Description', user=self.user)

    def test_project_get(self):

        response = self.client.get(reverse('tasks'))

        #
        self.assertEqual(response.status_code, 200)


        self.assertTemplateUsed(response, 'base/task_list.html')  #
