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

    def __str__(self):
        return self.title

class comments(models.Model):
    memory = models.ForeignKey(Memories, on_delete=models.CASCADE , related_name="allcomments")
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=500)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.comment