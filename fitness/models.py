from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    gender=models.CharField(max_length=1)
    weight=models.PositiveIntegerField(default=0)
    age=models.PositiveIntegerField(default=0)

    def __unicode__(self):
        return self.user.username
