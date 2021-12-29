from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from edit.forms import ReceiptForm
from edit.forms import EditContactForm
from home.models import contact, receipt
from django.contrib import messages

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
    if request.method == 'POST':
        form = ReceiptForm(request.POST)
        if form.is_valid():
            if receipt.objects.filter(belegnummer=form.cleaned_data['belegnummer']).exists():
                messages.error(request,'Beleg unter dieser Nummer existiert bereits.')
                return redirect('edit:editReceipts')
            form.save()
    else:
        form = ReceiptForm()

    
    context = {"title": "Beleg hinzufügen","form": form}
    return render(request, 'edit/editReceipts.html',context)

@login_required()
def editContacts(request):
    if request.method == 'POST':
        form = EditContactForm(request.POST)
        if form.is_valid():
            if contact.objects.filter(kontaktnummer=form.cleaned_data['kontaktnummer']).exists():
                form = EditContactForm()
                messages.error(request,'Kontakt unter dieser Nummer existiert bereits.')
                return redirect('edit:editContacts')
            form.save()
    else: 
        form = EditContactForm()
    context = {"title": "Kontakte bearbeiten","form":form}
    return render(request, 'edit/editContacts.html',context)

@login_required()
def editPassword(request):
    context = {"title": "Kontakte bearbeiten"}
    return render(request, 'edit/editPassword.html',context)

@login_required()
def editBankAccount(request):
    context = {"title": "Konto erstellen"}
    return render(request, 'edit/editBankAccount.html',context)