from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
# Create your views here.

def settings(request):
    context = {"title": "Einstellungen"}
    return render(request, 'edit/settings.html',context)