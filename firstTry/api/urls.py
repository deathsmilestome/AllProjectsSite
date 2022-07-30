from django.urls import path
from .views import get_projects, get_projects_k, get_projects_p

urlpatterns = [
    path('projectlist/', get_projects),
    path('projectlist/python', get_projects_p),
    path('projectlist/kotlin', get_projects_k),

]