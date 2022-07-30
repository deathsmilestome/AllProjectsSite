from rest_framework import serializers
from myProjectsapp.models import Project


class ProjectSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    class Meta:
        model = Project
        fields = '__all__'
