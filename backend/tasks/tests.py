from django.contrib.auth.models import User
from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from .models import Task, TimeRecord

class TaskViewSetTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='user', password='12345')
        self.admin_user = User.objects.create_user(username='admin', password='12345')
        self.admin_user.groups.create(name='Administrador')
        self.client.force_authenticate(user=self.user)

    def test_task_creation(self):
      data = {'description': 'Test Task'}
      response = self.client.post('/api/tasks/', data)
      
      self.assertEqual(response.status_code, status.HTTP_201_CREATED)
      
      task = Task.objects.get(description='Test Task')
      self.assertEqual(task.user, self.user)

    def test_task_deletion_success(self):
        task = Task.objects.create(description='Task to Delete', user=self.user)
        response = self.client.delete(f'/api/tasks/{task.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertRaises(Task.DoesNotExist, Task.objects.get, id=task.id)

class TimeRecordViewSetTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='user', password='12345')
        self.admin_user = User.objects.create_user(username='admin', password='12345')
        self.admin_user.groups.create(name='Administrador')
        self.client.force_authenticate(user=self.user)
        self.task = Task.objects.create(description='Task for Time Record', user=self.user)

    def test_time_record_creation(self):
        data = {
            'task': self.task.id,
            'date': '2024-10-21',
            'hours': 5.00,
            'description': 'Worked on task'
        }
        response = self.client.post('/api/time-records/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        time_record = TimeRecord.objects.get(description='Worked on task')
        self.assertEqual(time_record.task, self.task)

    def test_time_record_deletion_forbidden(self):
        time_record = TimeRecord.objects.create(task=self.task, date='2024-10-21', hours=2.0, description='Record to Delete')
        self.client.force_authenticate(user=self.admin_user)
        response = self.client.delete(f'/api/time-records/{time_record.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_time_record_deletion_success(self):
        time_record = TimeRecord.objects.create(task=self.task, date='2024-10-21', hours=2.0, description='Record to Delete')
        response = self.client.delete(f'/api/time-records/{time_record.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertRaises(TimeRecord.DoesNotExist, TimeRecord.objects.get, id=time_record.id)
