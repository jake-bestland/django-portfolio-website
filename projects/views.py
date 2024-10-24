from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .models import Project
from django.views import generic
from .forms import ContactForm
from django.template.loader import render_to_string

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
    return render(request, 'projects/about.html')