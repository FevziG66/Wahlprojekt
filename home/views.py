from django.shortcuts import render
from django.db.models import Sum
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from home.models import contact, receipt, todo, konto
from home.forms import ReceiptForm, DashboardForm
from edit.forms import ReceiptForm as EditReceiptForm
from edit.forms import EditContactForm
from home.forms import ContactForm,AccountDetailForm
from django.contrib.auth.decorators import login_required

# Create your views here.




@login_required()
def dashboard(request):
    if request.method == "POST":
        if 'todo_done' in request.POST: #Button todo_done, der als Value die Aufgabe des To-Dos zugewiesen bekommt
            todo.objects.filter(aufgabe=request.POST['todo_done']).update( 
                erledigt = '1'
            ) #Filtern in der Datenbank nach To-Do 'Aufgabe', als erledigt kennzeichnen 
        if 'delete_todo' in request.POST: #Filtern in der Datenbank nach To-Do 'Aufgabe', To-Do löschen 
            todo.objects.filter(aufgabe=request.POST['delete_todo']).delete()
    sum_einnahmen =  receipt.objects.filter(art='Einnahme').aggregate(sum=Sum('betrag'))['sum']
    sum_ausgaben = receipt.objects.filter(art='Ausgabe').aggregate(sum=Sum('betrag'))['sum']
    sum_gewinn = sum_einnahmen - sum_ausgaben
    abstand_kleinugrenze_umsatz = 600000 - sum_einnahmen
    abstand_kleinugrenze_gewinn = 60000-sum_gewinn 
    # form = DashboardForm(initial={'einnahmen': sum_einnahmen,
    #     'ausgaben': sum_ausgaben,
    #     'umsatz': sum_umsatz,
    #     'kleinugrenze_Umsatz': abstand_kleinugrenze_umsatz,
    #     'kleinugrenze_Gewinn': abstand_kleinugrenze_gewinn
    # }) Obsolet, da Anzeige über die obigen, einzelnen Variablen gelöst wird 
    all_todos = todo.objects.all() #alle To-Dos werden aus der Datenbank geladen, um sie später anzeigen zu können 
    all_todos_dict = {
        'todo': all_todos
    } #todo zum Durchiterieren zugewiesen 

    context = {"title": "Dashboard","all_todos_dict": all_todos,"sum_einnahmen":sum_einnahmen,"sum_ausgaben":sum_ausgaben, #Zuweisen der einzelnen Variablen 
    "sum_gewinn":sum_gewinn,"abstand_kleinugrenze_umsatz":abstand_kleinugrenze_umsatz,"abstand_kleinugrenze_gewinn":abstand_kleinugrenze_gewinn}
    return render(request, 'home/dashboard.html',context)

@login_required()
def profile(request):
    context = {"title": "Profil"}
    return render(request, 'home/profile.html',context)

@login_required()
def accounts(request):
    all_kontos = konto.objects.all() #Alle Kontos werden aus der Datenbank geholt 
    all_kontos_dict = {
        'konto': all_kontos
    } #konto zum Durchiterieren zuweisen 
    context = {"title": "Konten","all_kontos_dict":all_kontos}
    return render(request, 'home/accounts.html',context)

@login_required()
def receipts(request):
    if request.method == "POST":
        if 'deleteReceipt' in request.POST: #Button 'deleteReceipt' löst Löschen aus 
            receipt.objects.filter(belegnummer=request.POST['belegnummer']).delete() #nach Belegnummer filtern, löschen 
        elif 'updateReceipt' in request.POST: #Button 'updateReceipt' löst Update eines Beleges aus 
                receipt.objects.filter(belegnummer=request.POST['belegnummer']).update( #Filter nach Belegnummer
                    belegnummer = request.POST['belegnummer'],
                    belegdatum = request.POST['belegdatum'],
                    zahlart = request.POST['zahlart'],
                    faelligkeit = request.POST['faelligkeit'],
                    betrag = request.POST['betrag'],
                    beschreibung = request.POST['beschreibung'],
                    art = request.POST['art'],
                    konto_name = request.POST.get('konto', False)) #einzelne Variablen updaten 

    all_kontos = konto.objects.all() #Alle Kontos aus Datenbank holen, um sie beim Bearbeiten des Belegs 
    all_kontos_dict = {
        'konto': all_kontos
    } 
    all_receipts = receipt.objects.all() # Alle Belege aus Datenbank holen, um sie später in Tabelle anzuzeigen
    all_receipts_dict = {
        'receipt': all_receipts
    }
    context = {"title": "Belege","all_receipts_dict": all_receipts,"all_kontos_dict":all_kontos} #Dict-Strukturen zuweisen
    return render(request, 'home/receipts.html',context)

@login_required()
def contacts(request):
    if request.method == "POST":
        if 'deleteContact' in request.POST: #Button 'deleteContact' löst Löschen aus 
            contact.objects.filter(kontaktnummer=request.POST['kontaktnummer']).delete()#nach Kontaktnummer filtern, dann löschen
        elif 'updateContact' in request.POST: #Button 'updateContact' löst Update eines Kontakts aus
                contact.objects.filter(kontaktnummer=request.POST['kontaktnummer']).update(
                    kontaktnummer = request.POST['kontaktnummer'],
                    firma = request.POST['firma'],
                    ansprechpartner = request.POST['ansprechpartner'],
                    adresse = request.POST['adresse'],
                    telefonnummer = request.POST['telefonnummer'],
                    email = request.POST['email']) #einzelne Variablen updaten 

    all_contacts = contact.objects.all() #alle Kontakte aus Datenbank holen 
    all_contacts_dict = {
        'contact': all_contacts
    }
    context = {"title": "Kontakte","all_contacts_dict": all_contacts,"all_contacts_dict": all_contacts}
    return render(request, 'home/contacts.html',context)

@login_required()
def todos(request):
    if request.method == "POST":
        if 'deleteTodo' in request.POST:
            todo.objects.filter(nummer=request.POST['nummer']).delete()
        elif 'updateTodo' in request.POST: 
            statusneu = 0 #Variable für Status, erstmal auf 0 gesetzt 
            if request.POST['status'] == 'Erledigt': #Wurde Status auf Erledigt geändert, wird Änderung in DB umgesetzt 
                statusneu = 1
            todo.objects.filter(nummer=request.POST['nummer']).update(
                nummer = request.POST['nummer'],
                aufgabe = request.POST['aufgabe'],
                beschreibung = request.POST['beschreibung'],                    
                erledigt = statusneu,
                datum = request.POST['datum'],
                faelligkeit = request.POST['faelligbis']) #einzelne Variablen mit Daten aus request.POST updaten

    all_todos = todo.objects.all() #alle To-Dos aus Datenbank holen, für spätere Anzeige in Tabelle 
    all_todos_dict = {
        'todo': all_todos
    }
    context = {"title": "To-Dos","all_todos_dict": all_todos}
    return render(request, 'home/todos.html',context)

@login_required()
def accountDetails(request):
    context = {"title": "Konten"}
    
    all_einnahmen = receipt.objects.filter(konto_name='Personalausgaben',art='Einnahme')#Alle Belege eines Kontos filtern
    all_einnahmen_dict = {                                                              #Statt 'Personalausgaben' überall eigentlich Variable,                                                              
        'einnahme': all_einnahmen                                                       #Umsetzung nicht mehr geschafft 
    }
    summe_e = receipt.objects.filter(konto_name='Personalausgaben',art='Einnahme').aggregate(sum=Sum('betrag'))['sum']#Nach Konto Variable u. Einnahme filtern, Summe der Belege aggregieren 

    all_ausgaben = receipt.objects.filter(konto_name = 'Personalausgaben',art='Ausgabe')
    all_ausgaben_dict = {
        'receipt': all_ausgaben
    }
    summe_a = receipt.objects.filter(konto_name='Personalausgaben',art='Ausgabe').aggregate(sum=Sum('betrag'))['sum']#Nach Konto Variable u. Ausgabe filtern, Summe der Belege aggregieren 
    name = 'Personalausgaben' #Konto-Variable statt Personalausgaben 

    
    context = {"title": "Details","all_ausgaben_dict": all_ausgaben,"all_einnahmen_dict":all_einnahmen,"konto":name,
        "summe_einnahmen":summe_e,"summe_ausgaben":summe_a} #Variablen für Anzeige zuweisen 
    return render(request, 'home/accountDetails.html',context)