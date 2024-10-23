from django.contrib import admin
from .models import Project, Skill

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_skill')
    exclude = ['slug']

admin.site.register(Project, ProjectAdmin)
admin.site.register(Skill)