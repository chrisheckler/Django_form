from django.shortcuts import render
from django import forms
from .forms import ContactForm

def contact(request):
    form_class = ContactForm

    return render(request, 'templates/contact.html', {
        'form': form_class,
    })
