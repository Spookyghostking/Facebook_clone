from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    created_by = models.ForeignKey(User,
        on_delete=models.CASCADE,
        related_name="posts")
    text = models.TextField()

    created = models.DateTimeField(auto_now_add=True)


class Image(models.Model):
    post = models.ForeignKey(Post,
        on_delete=models.CASCADE,
        related_name="images")
    image = models.ImageField(upload_to="images/")
