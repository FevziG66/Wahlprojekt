from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
# Create your views here.

def register(request):
    context = {"title": "Account anlegen"}
    return render(request, 'start/register.html',context)

def login(request):
    context = {"title": "Anmelden"}
    return render(request, 'start/login.html',context)

def aboutUs(request):
    context = {"title": "Über uns"}
    return render(request, 'start/aboutUs.html',context)

def impressum(request):
    context = {"title": "Impressum"}
    return render(request, 'start/impressum.html',context)

def forgotPassword(request):
    context = {"title": "Passwort vergessen"}
    return render(request, 'start/forgotPassword.html',context)

def resetPassword(request):
    context = {"title": "Passwort zurücksetzen"}
    return render(request, 'start/resetPassword.html',context)