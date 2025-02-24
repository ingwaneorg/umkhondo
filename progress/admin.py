from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('course_code','user_id','sort_order','title','completed','comment')
    list_filter = ('course_code','user_id')
    search_fields = ('title','comment')
    ordering = ('course_code','user_id','sort_order')
    
admin.site.register(Task, TaskAdmin)
