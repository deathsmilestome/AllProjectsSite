from django.shortcuts import render
from .models import Project


def home(request):
    projects = Project.objects.order_by('-id')
    home_dict = {
        'title': 'Projects',
        'projects': projects
    }
    return render(request, 'myProjectsapp/home.html', home_dict)


def python(request):
    py_proj = Project.objects.filter(lang='python')
    py_dict = {
        'title': 'PythonProjects',
        'projects': py_proj
    }
    return render(request, 'myProjectsapp/python.html', py_dict)


def kotlin(request):
    ko_proj = Project.objects.filter(lang='kotlin')
    ko_dict = {
        'title': 'KotlinProjects',
        'projects': ko_proj
    }
    return render(request, 'myProjectsapp/python.html', ko_dict)