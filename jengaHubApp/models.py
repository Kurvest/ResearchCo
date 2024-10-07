from django.db import models
from django.contrib.auth.models import User
class Professional(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_image = models.ImageField(upload_to='profiles/')

class Project(models.Model):
    engineer = models.ForeignKey(Engineer, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

class Feedback(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="feedbacks")
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
