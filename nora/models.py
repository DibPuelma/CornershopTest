from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.

class Option(models.Model):
    description = models.CharField(max_length=100)

class Menu(models.Model):
    menu_uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    options = models.ManyToManyField(Option)

class UserChoice(models.Model):
    user = models.OneToOneField(User)
    menu = models.OneToOneField(Menu)
    choice = models.OneToOneField(Option)
    isBig = models.BooleanField()
    additionalInfo = models.CharField(max_length=100)
