from django.db import models

class blog(models.Model):
    title = models.TextField(max_length=20)
    date = models.DateField()
    body = models.TextField(max_length=200)
    image = models.ImageField(upload_to='images/')