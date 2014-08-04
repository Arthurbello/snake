from django.contrib.auth.models import User
from django.db import models

# Create your models here.
# class Profile(models.Model):
#     user = models.OneToOneField(User)

class Score(models.Model):
    score = models.IntegerField()
    user = models.ForeignKey(User)