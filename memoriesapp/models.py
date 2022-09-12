from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField

# Create your models here.
class Memories(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    slug = AutoSlugField(populate_from = "title",null=False, unique = True)
