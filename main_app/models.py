from django.db import models
from django.urls import reverse

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    due_date = models.DateTimeField()
    total_time_spent = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title} ({self.id})'

    def get_absolute_url(self):
        return reverse('detail', kwargs={'task_id': self.id})
