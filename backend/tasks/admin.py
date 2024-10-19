from django.contrib import admin
from .models import Task, TimeRecord






class TaskAdmin(admin.ModelAdmin):
    pass

class TimeRecordAdmin(admin.ModelAdmin):
    pass
  

    
  
admin.site.register(Task, TaskAdmin)
admin.site.register(TimeRecord, TimeRecordAdmin)

