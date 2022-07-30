from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('python', views.python, name='Python'),
    path('kotlin', views.kotlin, name='Kotlin')
]