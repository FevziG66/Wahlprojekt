from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
# Create your views here.

def dashboard(request):
    context = {"title": "Dashboard"}
    return render(request, 'home/dashboard.html',context)

def profile(request):
    context = {"title": "Profil"}
    return render(request, 'home/profile.html',context)

def accounts(request):
    context = {"title": "Konten"}
    return render(request, 'home/accounts.html',context)
    
def receipts(request):
    context = {"title": "Belege"}
    return render(request, 'home/receipts.html',context)

def contacts(request):
    context = {"title": "Kontakte"}
    return render(request, 'home/contacts.html',context)

def bills(request):
    context = {"title": "Rechnungen"}
    return render(request, 'home/bills.html',context)

def todo(request):
    context = {"title": "To-Do-Liste"}
    return render(request, 'home/todo.html',context)