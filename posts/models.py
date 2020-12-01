from django.db import models
import random
from datetime import date
from django.utils import timezone
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Post(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  content = models.TextField(blank=True, null=True)
  photo = models.FileField(upload_to='images/', blank=True, null=True)
  created = models.DateTimeField(default=timezone.now)

  class Meta:
      ordering = ['-id']

  def serialize(self):
      return {
        "id": self.id,
        "content": self.content,
        "likes": random.randint(0, 200),
        "created": self.created
    }
