from django.db import models
from django.urls import reverse
# Create your models here.

PRIORITY_OPTIONS = (
    ('L', 'Low'),
    ('M', 'Medium'),
    ('H', 'High'),
)
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    due_date = models.DateTimeField()
    notes = models.TextField(blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    total_time_spent = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'task_id': self.id})
    
class Status(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    pomegranates_completed = models.IntegerField(default=0)
    breaks = models.IntegerField(default=0)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    is_latest = models.BooleanField(default=False)  # New field to indicate if it's the latest status

    def __str__(self):
        return f"Created: {self.created}, Complete: {self.complete}, Pomegranates Completed: {self.pomegranates_completed}, Breaks: {self.breaks}"
    
    class Meta:
        ordering = ['-created']


