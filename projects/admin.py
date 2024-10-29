from django.contrib import admin
from .models import Project, Skill, AboutMe

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'display_skill')
    exclude = ['slug']

admin.site.register(Project, ProjectAdmin)
admin.site.register(Skill)
admin.site.register(AboutMe)