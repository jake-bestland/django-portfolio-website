from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .models import Project, Skill, AboutMe
from .forms import ContactForm
from django.template.loader import render_to_string
from django.views import generic


class HomePageView(generic.ListView):
    model = Project
    template_name = 'projects/homepage.html'

class ProjectIndexView(generic.ListView):
    model = Project
    template_name = 'projects/index.html'

class ProjectDetailView(generic.DetailView):
    model = Project
    template_name = 'projects/detail.html'

def contact(request):
    """View function for sending a email through contact form."""
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
    """View function for about me page."""
    skills = Skill.objects.all()
    text = AboutMe.objects.get(id=1)
    context = {
        'skills': skills,
        'text': text
    }
    return render(request, 'projects/about.html', context=context)
