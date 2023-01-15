"""Test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from TestApp import views
from TestApp.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    # candidate
    path('', CandidateListView.as_view(), name="home_list"),
    path('candidate/create', CandidateCreateView.as_view(), name='candidate_create'),
    path('candidate/update/<int:pk>', CandidateUpdateView.as_view(), name='candidate_update'),
    path('candidate/delete/<int:pk>',CandidateDeleteView.as_view(), name='candidate_delete'),

    # Technology candidate years
    path('technology_candidate', TechnologyCandidateListView.as_view(), name="techno_candidate_list"),
    path('technology_candidate/create', TechnologyCandidateCreateView.as_view(), name='techno_candidate_create'),
    path('technology_candidate/update/<int:pk>', TechnologyCandidateUpdateView.as_view(), name='techno_candidate_update'),
    path('technology_candidate/delete/<int:pk>',TechnologyCandidateDeleteView.as_view(), name='techno_candidate_delete'),
    path('technology_candidate/delete/<int:pk>',TechnologyCandidateDeleteView.as_view(), name='techno_candidate_delete'),

    # Reporte
    path('report/details/<int:pk>', reporte, name='reporte'),


]
