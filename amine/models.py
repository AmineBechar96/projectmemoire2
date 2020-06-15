from django.db import models

class Job(models.Model):
    image23 = models.ImageField(upload_to='images/')
    chars = models.CharField(max_length=30)
