# Generated by Django 5.2 on 2025-04-08 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_info', '0008_rename_created_by_activity_created_by_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='general_task',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='activity',
            name='gnrl_pickup',
            field=models.CharField(blank=True, default='', max_length=40),
        ),
    ]
