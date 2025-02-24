from django.db import models

class Task(models.Model):
    course_code = models.IntegerField(verbose_name='Course')
    user_id = models.IntegerField(verbose_name='User')
    sort_order = models.IntegerField(default=0, verbose_name='Sort')
    title = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.course_code}-{self.user_id}: {self.title}'

    class Meta:
        ordering = ['course_code', '-sort_order']
