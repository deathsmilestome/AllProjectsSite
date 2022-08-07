from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ProjectSerializer
from myProjectsapp.models import Project, Category


class AllProjects(APIView):
    def get(self, request):
        projects = Project.objects.all().order_by('-id')
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    def post(self, request):
        npd = request.data
        category_name = Category.objects.get(name=npd["category"])
        new_project = Project.objects.create(category=category_name, name=npd["name"], title=npd["title"], path=npd["path"], text=npd["text"])
        new_project.save()
        serializer=ProjectSerializer(new_project)
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
