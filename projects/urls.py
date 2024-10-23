from django.urls import path
from . import views



app_name = 'projects'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('projects/', views.index, name='projects'),
    path('projects/<slug:slug>', views.detail, name='project_detail'),
]