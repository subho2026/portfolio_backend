from django.urls import path
from . import views

urlpatterns = [
    path("get-portfolio-details", views.GetPortfolioDetails, name="get-portfolio-details"),
    path("get-portfolio-details/<int:portfolio_id>", views.GetPortfolioDetails, name="get-portfolio-details"),
]