from django.shortcuts import render, redirect
from django import forms
from .forms import PersonForm


def contact(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)

        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()

            return redirect('contact')
    else:
        form = PersonForm()

    return render(request, "contact.html", {'form': form})
