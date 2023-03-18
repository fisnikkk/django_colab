from django.db import models
from django.urls import reverse



class MyModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def get_absolute_url(self):
        return reverse('my_model_detail', args=[str(self.pk)])



