# Generated by Django 5.1.7 on 2025-03-25 12:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_info', '0002_remove_task_id_alter_task_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=40, unique=True)),
                ('password', models.CharField(max_length=40)),
                ('role', models.CharField(choices=[('admin', 'Admin'), ('user', 'User')], default='user', max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('task_id', models.AutoField(primary_key=True, serialize=False)),
                ('task_name', models.CharField(max_length=40)),
                ('task_des', models.CharField(max_length=400)),
                ('status', models.BooleanField(default=False)),
                ('created_by', models.CharField(max_length=40)),
                ('assin_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='get_info.user')),
            ],
        ),
    ]
