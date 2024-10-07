from django.db import models
from django.contrib.auth.models import User

class Professional(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_image = models.ImageField(upload_to='profiles/')
    profession = models.CharField(max_length=100)
    
class Project(models.Model):
    professional = models.ForeignKey(Professional, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
       return self.title

class Feedback(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="feedbacks")
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
