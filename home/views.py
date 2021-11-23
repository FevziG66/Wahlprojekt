from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
# Create your views here.

def dashboard(request):
    context = {"title": "Dashboard"}
    return render(request, 'home/dashboard.html',context)
