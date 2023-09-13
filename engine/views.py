from django.shortcuts import render
from . import models, serializers
from rest_framework.response import Response
from django.http import JsonResponse


# Create your views here.
def GetPortfolioDetails(request):
    if request.method == "GET":
        portfolio_id = request.GET.get("portfolio_id")
        portfolio = models.Portfolio.objects.get(id=portfolio_id)
        serialized_portfolio = serializers.Portfolio(portfolio)

        education = models.Education.objects.filter(portfolio=portfolio_id)
        serialized_education = serializers.Education(education, many=True)

        about = models.About.objects.filter(portfolio=portfolio_id)
        serialized_about = serializers.About(about, many=True)

        professionalexperience = models.ProfessionalExperience.objects.filter(portfolio=portfolio_id)
        serialized_professionalexperience = serializers.ProfessionalExperience(professionalexperience, many=True)

        project = models.Project.objects.filter(portfolio=portfolio_id)
        serialized_project = serializers.Project(project, many=True)

        print(portfolio, education, about, professionalexperience, project)

        return JsonResponse({"portfolio": serialized_portfolio.data, "education": serialized_education.data,
                             "about": serialized_about.data,
                             "professionalexperience": serialized_professionalexperience.data,
                             "project": serialized_project.data})
