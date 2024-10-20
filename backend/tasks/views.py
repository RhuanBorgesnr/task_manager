from rest_framework import viewsets
from .models import Task, TimeRecord
from .serializers import TaskSerializer, TimeRecordSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.decorators import action


class UserDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        groups = user.groups.values_list('name', flat=True)
        return Response({'username': user.username, 'groups': list(groups)})

class NonAdminUserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        non_admin_users = User.objects.exclude(groups__name='Administrador')
        users_data = [{'id': user.id, 'username': user.username} for user in non_admin_users]
        return Response(users_data, status=status.HTTP_200_OK)
    
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
    def get_queryset(self):
        user = self.request.user
        if user.groups.filter(name='Administrador').exists():
            return Task.objects.all()
        else:
            return Task.objects.filter(user=user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    def destroy(self, request, *args, **kwargs):
        task = self.get_object()
        if task.user != request.user and not request.user.groups.filter(name='Administrador').exists():
            return Response(status=status.HTTP_403_FORBIDDEN)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

 
class TimeRecordViewSet(viewsets.ModelViewSet):
    queryset = TimeRecord.objects.all()
    serializer_class = TimeRecordSerializer 

    def get_queryset(self):
        user = self.request.user
        if user.groups.filter(name='Administrador').exists():
            queryset = TimeRecord.objects.all()
        else:
            queryset = TimeRecord.objects.filter(task__user=user)
        date = self.request.query_params.get('date', None)
        hours = self.request.query_params.get('hours', None)
        description = self.request.query_params.get('description', None)
        task_id = self.request.query_params.get('task', None)
        user = self.request.query_params.get('user', None)
        

        if date:
            queryset = queryset.filter(date=date)
        if hours:
            queryset = queryset.filter(hours=hours)
        if description:
            queryset = queryset.filter(description__icontains=description)
        if task_id:
            queryset = queryset.filter(task_id=task_id)
        if user:
            queryset = queryset.filter(task__user_id=user)

        return queryset
    
    def destroy(self, request, *args, **kwargs):
        time_records = self.get_object()
        if time_records.task.user != request.user and not request.user.groups.filter(name='Administrador').exists():
            return Response(status=status.HTTP_403_FORBIDDEN)
        time_records.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)