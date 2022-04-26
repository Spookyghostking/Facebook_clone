from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User,
        on_delete=models.CASCADE,
        related_name="profile")
    slug = models.SlugField(max_length=255, unique=True)
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user.username)
        super(Profile, self).save(*args, **kwargs)
