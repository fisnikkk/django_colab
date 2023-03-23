from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User



class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)  # Replace ForeignKey with CharField
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title




class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthdate = models.DateField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse('user_profile_detail', args=[str(self.pk)])

    def __str__(self):
        return self.user.username