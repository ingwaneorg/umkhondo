# Generated by Django 4.2.19 on 2025-02-25 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('progress', '0016_alter_task_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_id',
            field=models.CharField(max_length=2, primary_key=True, serialize=False),
        ),
    ]
