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
        serialized_education = serializers.Education(education, many=True, context={"request": request})

        about = models.About.objects.filter(portfolio=portfolio_id)
        serialized_about = serializers.About(about, many=True, context={"request": request})

        professionalexperience = models.ProfessionalExperience.objects.filter(portfolio=portfolio_id)
        serialized_professionalexperience = serializers.ProfessionalExperience(professionalexperience, many=True,
                                                                               context={"request": request})

        skill = models.Skill.objects.filter(portfolio=portfolio_id)
        serialized_skill = serializers.Skill(skill, many=True, context={"request": request})

        project = models.Project.objects.filter(portfolio=portfolio_id)
        serialized_project = serializers.Project(project, many=True, context={"request": request})

        print(portfolio, education, about, professionalexperience, project, skill)

        return JsonResponse({"portfolio": serialized_portfolio.data, "education": serialized_education.data,
                             "about": serialized_about.data,
                             "professionalexperience": serialized_professionalexperience.data,
                             "project": serialized_project.data,
                             "skill": serialized_skill.data})
