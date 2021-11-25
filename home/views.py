from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
# Create your views here.

def dashboard(request):
    context = {"title": "Dashboard"}
    return render(request, 'home/dashboard.html',context)

def settings(request):
    context = {"title": "Einstellungen"}
    return render(request, 'home/settings.html',context)

def profile(request):
    context = {"title": "Profil"}
    return render(request, 'home/profile.html',context)

def accounts(request):
    context = {"title": "Konten"}
    return render(request, 'home/accounts.html',context)
    
def receipts(request):
    context = {"title": "Belege"}
    return render(request, 'home/receipts.html',context)