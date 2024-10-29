from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .models import Project, Skill, AboutMe
from .forms import ContactForm
from django.template.loader import render_to_string

# Create your views here.
def homepage(request):
    projects = Project.objects.all()
    return render(request, 'projects/homepage.html', {'projects': projects})

def index(request):
    projects = Project.objects.all()
    return render(request, 'projects/index.html', {'projects': projects})

def detail(request, slug):
    project = Project.objects.get(slug=slug)
    return render(request, 'projects/detail.html', {'project': project})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            hmtl = render_to_string('projects/emails/contact_form.html', {
                'name': name,
                'email': email,
                'message': message
            })

            send_mail('Message from Portfolio contact page.', 'This is the message', email, ['jake.bestland@gmail.com'], html_message = hmtl)

            return redirect('/contact')
        
    else:
        form = ContactForm()
    return render(request, 'projects/contact.html', {'form': form})

def about(request):
    skills = Skill.objects.all()
    text = AboutMe.objects.get(id=1)
    context = {
        'skills': skills,
        'text': text
    }
    return render(request, 'projects/about.html', context=context)