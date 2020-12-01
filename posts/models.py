from django.db import models

class Post(models.Model):
  content = models.TextField(blank=True, null=True)
  photo = models.FileField(upload_to='images/', blank=True, null=True)