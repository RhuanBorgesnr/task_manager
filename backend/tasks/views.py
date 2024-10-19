from rest_framework import viewsets
from .models import Task, TimeRecord
from .serializers import TaskSerializer, TimeRecordSerializer
from rest_framework.response import Response
from rest_framework import status

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    def destroy(self, request, *args, **kwargs):
        task = self.get_object()
        if task.user != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

 
class TimeRecordViewSet(viewsets.ModelViewSet):
    queryset = TimeRecord.objects.all()
    serializer_class = TimeRecordSerializer 

    def get_queryset(self):
        queryset = TimeRecord.objects.filter(task__user=self.request.user)
        date = self.request.query_params.get('date', None)
        hours = self.request.query_params.get('hours', None)
        description = self.request.query_params.get('description', None)
        task_id = self.request.query_params.get('task', None)

        if date:
            queryset = queryset.filter(date=date)
        if hours:
            queryset = queryset.filter(hours=hours)
        if description:
            queryset = queryset.filter(description__icontains=description)
        if task_id:
            queryset = queryset.filter(task_id=task_id)

        return queryset