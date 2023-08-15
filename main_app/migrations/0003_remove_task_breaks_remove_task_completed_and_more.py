# Generated by Django 4.2.4 on 2023-08-13 20:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_remove_task_priority'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='breaks',
        ),
        migrations.RemoveField(
            model_name='task',
            name='completed',
        ),
        migrations.RemoveField(
            model_name='task',
            name='created',
        ),
        migrations.RemoveField(
            model_name='task',
            name='pomodoros_completed',
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('complete', models.BooleanField(default=False)),
                ('pomodoros_completed', models.IntegerField(default=0)),
                ('breaks', models.IntegerField(default=0)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.task')),
            ],
        ),
    ]