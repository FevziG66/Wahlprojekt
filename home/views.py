from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required()
def dashboard(request):
    context = {"title": "Dashboard"}
    return render(request, 'home/dashboard.html',context)

@login_required()
def profile(request):
    context = {"title": "Profil"}
    return render(request, 'home/profile.html',context)

@login_required()
def accounts(request):
    context = {"title": "Konten"}
    return render(request, 'home/accounts.html',context)

@login_required()
def receipts(request):
    context = {"title": "Belege"}
    return render(request, 'home/receipts.html',context)

@login_required()
def contacts(request):
    context = {"title": "Kontakte"}
    return render(request, 'home/contacts.html',context)

@login_required()
def bills(request):
    context = {"title": "Rechnungen"}
    return render(request, 'home/bills.html',context)