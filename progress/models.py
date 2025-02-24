from django.db import models

class Task(models.Model):
    course_code = models.CharField(max_length=5, verbose_name='Course')
    week_num = models.IntegerField(verbose_name='Week')
    user_id = models.IntegerField(verbose_name='User')
    sort_order = models.IntegerField(default=0, verbose_name='Sort')
    title = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['week_num', '-sort_order']
