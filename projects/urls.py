from django.urls import path
from . import views



app_name = 'projects'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='homepage'),
    path('projects/', views.ProjectIndexView.as_view(), name='projects'),
    path('projects/<slug:slug>', views.ProjectDetailView.as_view(), name='project_detail'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
]