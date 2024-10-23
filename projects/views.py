from django.shortcuts import render
from .models import Project
from django.views import generic

# Create your views here.
def homepage(request):
    context = {

    }
    return render(request, 'projects/homepage.html', context)

# class RecentProjectListView(generic.ListView):
#     model = Project
#     # template_name =

def index(request):
    projects = Project.objects.all()
    return render(request, 'projects/index.html', {'projects': projects})

def detail(request, slug):
    project = Project.objects.get(slug=slug)
    return render(request, 'projects/detail.html', {'projects': project})