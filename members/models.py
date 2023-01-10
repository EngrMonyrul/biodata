from django.db import models

class People(models.Model):
    name = models.CharField(max_length=255)
    age = models.FloatField()
    number = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images')
    details = models.TextField()