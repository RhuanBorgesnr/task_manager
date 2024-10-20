from rest_framework import serializers
from .models import Task, TimeRecord
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        
        token['is_admin'] = user.groups.filter(name='Administrador').exists()
        
        return token
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
    formatted_hours = serializers.SerializerMethodField() 
    
    class Meta:
        model = TimeRecord
        fields = ['id', 'task', 'description', 'formatted_hours', 'hours', 'date', 'task_description']
        
    def get_task_description(self, obj):
        if obj.task:
            return obj.task.description
        return obj.task
    
    def get_formatted_hours(self, obj):
        return self.format_hours(obj.hours)

    def format_hours(self, decimal_hours):
        hours = int(decimal_hours)
        minutes = round((decimal_hours - hours) * 60)
        return f"{hours:02}:{minutes:02}"