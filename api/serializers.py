from projects.models import Project, Skill, AboutMe
from rest_framework import serializers

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ['title', 'description', 'skill', 'slug', 'preview_image', 'animated_gif', 'link', 'highlight']   # only use certain fields?


class SkillSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Skill
        fields = ['name']

class AboutMeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AboutMe
        fields = ['tag_line_text', 'main_text']