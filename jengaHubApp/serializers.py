from rest_framework import serializers
from .models import Project, Feedback

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'engineer', 'title', 'description', 'date_added']

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['id', 'project', 'client', 'comment', 'date_added']
