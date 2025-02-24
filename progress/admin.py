from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('week_num','user_id','sort_order','title','completed','comment')
    list_filter = ('week_num','user_id')
    search_fields = ('title','comment'),
    ordering = ('week_num','user_id','sort_order')
    
admin.site.register(Task, TaskAdmin)
