# Generated by Django 4.2.19 on 2025-02-24 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('progress', '0003_alter_task_week_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='user_id',
            field=models.IntegerField(verbose_name='User'),
        ),
    ]
