from rest_framework import serializers
from .models import Task, TimeRecord

class TaskSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = ['id', 'user', 'description', 'created_at', 'username']
        read_only_fields = ['user', 'created_at']
    
    def get_username(self, obj):
        if obj.user:
            return obj.user.username
        return None
            
        
        
class TimeRecordSerializer(serializers.ModelSerializer):
    task_description = serializers.SerializerMethodField()
    
    class Meta:
        model = TimeRecord
        fields = ['id', 'task', 'description', 'hours', 'date', 'task_description']
        
    def get_task_description(self, obj):
        if obj.task:
            return obj.task.description
        return obj.task