from django.db import models
import simditor.fields import RichTextField

class Post(models.Model):
	content = RichTextField()
	