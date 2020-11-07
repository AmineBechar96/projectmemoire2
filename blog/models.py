from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=20)
    date = models.DateField()
    body = models.TextField(max_length=200)
    image = models.ImageField(upload_to='images/')
    image2 = models.CharField(default=1,max_length=50)
    def summary(self):
        return self.body[:10]