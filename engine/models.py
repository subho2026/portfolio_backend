from django.db import models

from account.models import User


# Create your models here.

class Portfolio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


class About(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    cv_url = models.URLField()
    linkedin_url = models.URLField()
    github_url = models.URLField()
    primary_image = models.ImageField()
    secondary_image = models.ImageField()
    about = models.TextField(max_length=1024)


class Education(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    degree = models.CharField(max_length=1024)
    university = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(null=True)
    certificate = models.FileField(upload_to="files")


class ProfessionalExperience(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    company = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    file = models.FileField(upload_to="files", null=True, blank=True)


class Project(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    thumbnail = models.ImageField()
    name = models.CharField(max_length=255)
    github_url = models.URLField()
    demo_url = models.URLField(blank=True)
