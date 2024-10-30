from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.db.models import UniqueConstraint
from django.db.models.functions import Lower

# Create your models here.

class AboutMe(models.Model):
    """Model representing About Me information"""
    tag_line_text = models.CharField(max_length=200)
    main_text = models.TextField()
    

class Skill(models.Model):
    """Model representing technology used for a Project."""
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.name
    
    def get_absolute_url(self):
        """Returns the URL to access a particular Skill instance."""
        return reverse('skill-detail', args=[str(self.id)])
    
    class Meta:
        constraints = [
            UniqueConstraint(
                Lower('name'),
                name='skill_name_case_insensitive_unique',
                violation_error_message= "Skill already exists (case insensitive match)"
            ),
        ]

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    skill = models.ManyToManyField(Skill, help_text="Select a skill used for this project.")
    slug = models.SlugField(unique=True, null=True, blank=True)
    preview_image = models.ImageField(upload_to='images/previews/', null=True, blank=True)
    animated_gif = models.ImageField(upload_to='images/gifs/', null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    highlight = models.BooleanField(default=False)
    

    def save(self, *args, **kwargs):
        """overwrites the internal save() method to automatically create a slug, if not provided."""
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    
    def __str__(self):
        """String for representing the Model object."""
        return self.title
    
    def get_absolute_url(self):
        """Returns the URL to access a detail record for this project."""
        return reverse('project-detail', args=[str(self.id)])
    
    def display_skill(self):
        """Create a string for the Skill.  This is required to display the skill in Admin."""
        return ', '.join(skill.name for skill in self.skill.all())
    
    def skills_as_list(self):
        return (skill.name for skill in self.skill.all())
    
    display_skill.short_description = 'Skill'