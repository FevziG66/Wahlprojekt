from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
# Create your views here.

# login_required ist dafür da, dass die Seite nur aufgerufen werden kann, wenn man angemeldet ist
@login_required()
def settings(request):
    context = {"title": "Einstellungen"}
    return render(request, 'edit/settings.html',context)

@login_required()
def editBankData(request):
    context = {"title": "Bankdaten"}
    return render(request, 'edit/editBankData.html',context)

@login_required()
def deleteAccount(request):
    context = {"title": "Account löschen"}
    return render(request, 'edit/deleteAccount.html',context)

@login_required()
def editReceipts(request):
    context = {"title": "Beleg bearbeiten"}
    return render(request, 'edit/editReceipts.html',context)

@login_required()
def editContacts(request):
    context = {"title": "Kontakte bearbeiten"}
    return render(request, 'edit/editContacts.html',context)

@login_required()
def editPassword(request):
    context = {"title": "Kontakte bearbeiten"}
    return render(request, 'edit/editPassword.html',context)