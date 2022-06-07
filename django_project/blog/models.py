from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

'''
auto_now fields are updated to the current timestamp every time an object is saved 
and are therefore perfect for tracking when an object was last modified, 
while an auto_now_add field is saved as the current timestamp when a row is 
first added to the database, and is therefore perfect for tracking when it was created. 
'''


class post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})