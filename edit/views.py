from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
# Create your views here.

def settings(request):
    context = {"title": "Einstellungen"}
    return render(request, 'edit/settings.html',context)

def editBankData(request):
    context = {"title": "Bankdaten"}
    return render(request, 'edit/editBankData.html',context)

def deleteAccount(request):
    context = {"title": "Account löschen"}
    return render(request, 'edit/deleteAccount.html',context)

def editReceipts(request):
    context = {"title": "Beleg bearbeiten"}
    return render(request, 'edit/editReceipts.html',context)

def editContacts(request):
    context = {"title": "Kontakte bearbeiten"}
    return render(request, 'edit/editContacts.html',context)

def editPassword(request):
    context = {"title": "Kontakte bearbeiten"}
    return render(request, 'edit/editPassword.html',context)