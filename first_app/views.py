from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Musician, Album, Person
from first_app import forms
# Create your views here.

def index(request):
    musician_list = Musician.objects.order_by('first_name')
    diction = {'text1':'This is a list of Musicians', 'musician':musician_list}
    return render(request, 'first_app/index.html', context=diction)

def home(request):
    return HttpResponse("<h1>This is Homepage</h1> <a href='/first_app/contact/'>Contact</a> <a href='/first_app/about/'>About</a>")

def contact(request):
    return HttpResponse("<h1>This is Contact Page</h1><a href='/first_app/'>Homepage</a> <a href='/first_app/about/'>About</a>")

def about(request):
    return HttpResponse("<h1>This is About Page</h1> <a href='/first_app/'>Homepage</a> <a href='/first_app/contact/'>Contact</a>")

def form(request):
    new_form = forms.user_form()
    diction = {'test_form': new_form, 'heading1':"This form is creater with django library"}
    
    if request.method == 'POST':
        new_form = forms.user_form(request.POST)

        if new_form.is_valid():
            user_name = new_form.cleaned_data['user_name']
            user_dob = new_form.cleaned_data['user_dob']
            user_email = new_form.cleaned_data['user_email']

            diction.update({'user_name':user_name})
            diction.update({'user_dob':user_dob})
            diction.update({'user_email':user_email})
            diction.update({'form_submitted':"Yest"})

    return render(request, 'first_app/form.html', context=diction)
