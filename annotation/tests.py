from django.test import TestCase

# Create your tests here.
from django.test import TestCase

# Create your tests here.
from rest_framework.test import APITestCase
from rest_framework import status
from .models import AnnotationTask

class AnnotationTaskViewTest(APITestCase):
    def test_create_task(self):
        data = {
            "image_url": "https://example.com/image.jpg",
            "annotated_text": "Test annotation"
        }
        response = self.client.post('/api/tasks/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_fetch_tasks(self):
        AnnotationTask.objects.create(
            image_url="https://example.com/image.jpg",
            annotated_text="Sample annotation."
        )
        response = self.client.get('/api/tasks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
