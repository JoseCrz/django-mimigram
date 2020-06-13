from django.db import models

# Create your models here.
class User(models.Model):
    """ User Model """
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    birthdate = models.DateField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    country = models.TextField(blank=True)
    city = models.TextField(blank=True)

    def __str__(self):
        return self.email