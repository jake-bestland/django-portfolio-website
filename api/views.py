from projects.models import Project, Skill, AboutMe
from rest_framework import viewsets, permissions
from .serializers import ProjectSerializer, SkillSerializer, AboutMeSerializer

# Create your views here.
class ProjectViewSet(viewsets.ModelViewSet):
    """API endpoint that allows posts to be viewed or edited."""
    queryset = Project.objects.all().order_by('-title')
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

class SkillViewSet(viewsets.ModelViewSet):
    """API endpoint that allows posts to be viewed or edited."""
    queryset = Skill.objects.all().order_by('-name')
    serializer_class = SkillSerializer
    permission_classes = [permissions.IsAuthenticated]

class AboutMeViewSet(viewsets.ModelViewSet):
    """API endpoint that allows posts to be viewed or edited."""
    queryset = AboutMe.objects.all().order_by('-tag_line_text')
    serializer_class = AboutMeSerializer
    permission_classes = [permissions.IsAuthenticated]