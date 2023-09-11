from django.db import models


# Create your models here.

class portfolio(models.Model):
    pass


class About(models.Model):
    portfolio = models.ForeignKey(portfolio,on_delete=models.CASCADE())
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
    portfolio = models.ForeignKey(portfolio, on_delete=models.CASCADE())
    university = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(null=True)
    certificate = models.FileField(upload_to="files")


class ProfessionalExperience(models.Model):
    portfolio = models.ForeignKey(portfolio, on_delete=models.CASCADE())
    company = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(null=True)
    file = models.FileField(upload_to="files")
