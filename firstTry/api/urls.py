from django.urls import path
from .views import AllProjects, get_projects_k, get_projects_p

urlpatterns = [
    path('projectlist/', AllProjects.as_view()),
    path('projectlist/python', get_projects_p),
    path('projectlist/kotlin', get_projects_k),

]