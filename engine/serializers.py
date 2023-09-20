from . import models
from rest_framework import serializers


class Portfolio(serializers.ModelSerializer):
    class Meta:
        model = models.Portfolio
        fields = '__all__'


class About(serializers.ModelSerializer):
    class Meta:
        model = models.About
        fields = '__all__'


class Education(serializers.ModelSerializer):
    class Meta:
        model = models.Education
        fields = '__all__'


class ProfessionalExperience(serializers.ModelSerializer):
    class Meta:
        model = models.ProfessionalExperience
        fields = '__all__'


class Skill(serializers.ModelSerializer):
    class Meta:
        model = models.Skill
        fields = '__all__'


class Project(serializers.ModelSerializer):
    class Meta:
        model = models.Project
        fields = '__all__'
