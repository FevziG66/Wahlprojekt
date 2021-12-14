from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from edit.forms import ReceiptForm
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
    if request.method == 'POST':
        form = ReceiptForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ReceiptForm()

    
    context = {"title": "Beleg hinzufügen","form": form}
    return render(request, 'edit/editReceipts.html',context)

def editContacts(request):
    context = {"title": "Kontakte bearbeiten"}
    return render(request, 'edit/editContacts.html',context)

def editPassword(request):
    context = {"title": "Kontakte bearbeiten"}
    return render(request, 'edit/editPassword.html',context)