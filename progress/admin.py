from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Task, Course


class TaskAdmin(admin.ModelAdmin):
    list_display = ('course_id', 'user_id', 'sort_order', 'title', 'completed', 'comment')
    list_filter = ('course_id', 'user_id')
    search_fields = ('title', 'comment')
    ordering = ('course_id', 'user_id', 'sort_order')
    
admin.site.register(Task, TaskAdmin)


class CourseAdmin(admin.ModelAdmin):
    list_display = ('short_code', 'description') 
    search_fields = ('short_code', 'description')
    ordering = ('short_code',)

admin.site.register(Course, CourseAdmin) 
