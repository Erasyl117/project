from django.db import models
from django.conf import settings
from django.core.validators import MinLengthValidator

class Article(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title=models.CharField(max_length=255)
    text=models.TextField()
    timestamp=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title