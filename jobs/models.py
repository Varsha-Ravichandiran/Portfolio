from django.db import models

# Create your models here.
class Job(models.Model):
    topic = models.TextField(max_length=50)
    image = models.ImageField(upload_to='images/')
    video = models.FileField(upload_to='videos/',blank=True, null=True)
    summary = models.CharField(max_length=10000)

    def __str__(self):
        return self.topic