# myapp/models.py
from django.db import models

class MailRequest(models.Model):
    subject = models.CharField(max_length=255)
    recipient = models.CharField(max_length=255)
    from_time = models.TimeField()
    to_time = models.TimeField()
    date = models.DateField()
    department = models.CharField(max_length=100)
    year = models.IntegerField()
    content = models.TextField()
    status = models.CharField(max_length=50, default='Pending')
    rejection_reason = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.subject
