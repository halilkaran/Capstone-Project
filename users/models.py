from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.URLField(default="https://img.favpng.com/8/14/0/computer-icons-user-profile-material-design-png-favpng-fhWEA7BrBaUmKQZ5DYmuv2qDm.jpg")

    def __str__(self):
        return "{} {}".format(self.user, 'Profile')