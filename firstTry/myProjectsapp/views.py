from django.shortcuts import render
from .models import Project, Category


def home(request):
    projects = Project.objects.order_by('-id')
    categories = Category.objects.all().values('name')
    home_dict = {
        'title': 'Projects',
        'projects': projects,
        'categories': categories
    }
    return render(request, 'myProjectsapp/home.html', home_dict)


def python(request):
    py_proj = Project.objects.select_related('category').filter(category__name='Python').order_by('-id')
    py_dict = {
        'title': 'PythonProjects',
        'projects': py_proj
    }
    return render(request, 'myProjectsapp/python.html', py_dict)


def kotlin(request):
    ko_proj = Project.objects.select_related('category').filter(category__name='Kotlin').order_by('-id')
    ko_dict = {
        'title': 'KotlinProjects',
        'projects': ko_proj
    }
    return render(request, 'myProjectsapp/python.html', ko_dict)