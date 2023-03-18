from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User



class MyModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def get_absolute_url(self):
        return reverse('my_model_detail', args=[str(self.pk)])

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthdate = models.DateField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse('user_profile_detail', args=[str(self.pk)])

    def __str__(self):
        return self.user.username

