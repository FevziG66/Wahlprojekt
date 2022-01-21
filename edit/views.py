from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from edit.forms import ReceiptForm
from edit.forms import EditContactForm, EditAccountForm, EditTodoForm
from home.models import contact, konto, receipt, todo
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
                return redirect('edit:editReceipts') #Wenn Belegnummer bereits existiert, Fehlermeldung anzeigen
            try:
                form.save()
            except:
                messages.error(request,'Beleg konnte nicht gesichert werden!')
                return redirect('edit:editReceipts') #Wenn Beleg anderweitig nicht gesichert werden konnte, Fehlermeldung anzeigen
            messages.success(request,'Beleg erfolgreich gesichert!')
            return redirect('edit:editReceipts')

    else:   
        letzter_beleg = receipt.objects.last() #letzten Beleg holen 
        letzte_belegnummer = letzter_beleg.belegnummer + 1 #Auf Nummer des Belegs 1 addieren, für 'automatische' Vergabe der Belegnummer 
        form = ReceiptForm(initial={'belegnummer': letzte_belegnummer}) #neue Belegnummer zuweisen 
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
                return redirect('edit:editContacts') #Fehler, wenn Kontakt bereits existiert 
            form.save()
            messages.success(request,'Kontakt erfolgreich hinzugefügt!') #Erfolgsnachricht, wenn Kontakt gespeichert 
            return redirect('edit:editContacts')
    else: 
        form = EditContactForm()
    context = {"title": "Kontakte bearbeiten","form":form}
    return render(request, 'edit/editContacts.html',context)

@login_required()
def editBankAccount(request):
    if request.method == 'POST':
        form = EditAccountForm(request.POST)
        if form.is_valid():
            if konto.objects.filter(name=form.cleaned_data['name']).exists():
                form = EditAccountForm()
                messages.error(request,'Konto mit diesem Namen existiert bereits.')
                return redirect('edit:editBankAccount') #Fehlermeldung, Konto existiert bereits 
            try:
                form.save()
            except:
                messages.error(request,'Konto konnte nicht gesichert werden!') #Fehlermeldung, Konto konnte aus anderem Grund nicht gesichert werden
                return redirect('edit:editBankAccount')
            messages.success(request,'Konto erfolgreich gesichert!')
            return redirect('edit:editBankAccount')
    else: 
        form = EditAccountForm()
    context = {"title": "Konto erstellen","form":form}
    return render(request, 'edit/editBankAccount.html',context)
    
@login_required()
def editToDos(request):
    if request.method == 'POST':
        postdata = request.POST #postdata entspricht jetzt Daten aus request.POST
        postdata._mutable = True #mutable -> Daten könnnen verändert werden
        postdata['erledigt'] = '0' #erledigt auf 0 setzen, da kein Status erledigt im Frontend vorhanden 
        postdata._mutable = False 
        form = EditTodoForm(postdata) #EditTodoForm mit 'geänderten' Daten aus postdata instanziieren 
        if form.is_valid():
            if todo.objects.filter(nummer=form.cleaned_data['nummer']).exists():
                form = EditTodoForm()
                messages.error(request,'To-Do mit dieser Nummer existiert bereits.')
                return redirect('edit:editToDos') #Fehlermeldung, To-Do existiert bereits 
            try:
                form.save()
            except:
                messages.error(request,'To-Do konnte nicht gesichert werden!')
                return redirect('edit:editToDos')
            messages.success(request,'To-Do erfolgreich gesichert!')
            return redirect('edit:editToDos')
    else: 
        form = EditTodoForm()
    context = {"title": "Aufgabe erstellen","form":form}
    return render(request, 'edit/editToDos.html',context)


@login_required()
def password_change_done(request):
    context = {"title": "Aufgabe erstellen"}
    return render(request, 'edit/change_password_done.html',context)
