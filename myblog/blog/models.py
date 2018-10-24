from django.db import models
from simditor.fields import RichTextField
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=100)