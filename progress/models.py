from django.db import models

class Course(models.Model):
    course_id = models.IntegerField(primary_key=True)  # Manually entered
    short_code = models.CharField(max_length=5, verbose_name='Short Code')
    description = models.CharField(max_length=255, verbose_name='Description')

    def __str__(self):
        return f"{self.short_code} - {self.description}"

class Task(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)  
    user_id = models.IntegerField(verbose_name='User')
    sort_order = models.IntegerField(default=0, verbose_name='Sort')
    title = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.course.short_code}-{self.user_id}: {self.title}'

    class Meta:
        ordering = ['user_id','sort_order']
