from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    decs = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
