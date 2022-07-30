from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProjectSerializer
from myProjectsapp.models import Project


@api_view(['GET'])
def get_projects(request):
    projects = Project.objects.all().order_by('-id')
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_projects_p(request):
    projects = Project.objects.select_related('category').filter(category__name='Python').order_by('-id')
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_projects_k(request):
    projects = Project.objects.select_related('category').filter(category__name='Kotlin').order_by('-id')
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)
