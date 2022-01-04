from django.shortcuts import render
from django.db.models import Sum
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from home.models import contact, receipt, todo, konto
from home.forms import ReceiptForm
from edit.forms import ReceiptForm as EditReceiptForm
from edit.forms import EditContactForm
from home.forms import ContactForm,AccountDetailForm
from django.contrib.auth.decorators import login_required

# Create your views here.




@login_required()
def dashboard(request):
    all_todos = todo.objects.all()
    all_todos_dict = {
        'todo': all_todos
    }

    context = {"title": "Dashboard","all_todos_dict": all_todos}
    return render(request, 'home/dashboard.html',context)

@login_required()
def profile(request):
    context = {"title": "Profil"}
    return render(request, 'home/profile.html',context)

@login_required()
def accounts(request):
    all_kontos = konto.objects.all()
    all_kontos_dict = {
        'konto': all_kontos
    }
    context = {"title": "Konten","all_kontos_dict":all_kontos}
    return render(request, 'home/accounts.html',context)

@login_required()
def receipts(request):
    if request.method == "POST":
        if 'deleteReceipt' in request.POST:
            receipt.objects.filter(belegnummer=request.POST['belegnummer']).delete()
        elif 'updateReceipt' in request.POST: 
                receipt.objects.filter(belegnummer=request.POST['belegnummer']).update(
                    belegnummer = request.POST['belegnummer'],
                    belegdatum = request.POST['belegdatum'],
                    zahlart = request.POST['zahlart'],
                    faelligkeit = request.POST['faelligkeit'],
                    betrag = request.POST['betrag'],
                    beschreibung = request.POST['beschreibung'],
                    art = request.POST['art'],
                    konto_name = request.POST.get('konto', False))

    all_kontos = konto.objects.all()
    all_kontos_dict = {
        'konto': all_kontos
    }
    all_receipts = receipt.objects.all()
    all_receipts_dict = {
        'receipt': all_receipts
    }
    context = {"title": "Belege","all_receipts_dict": all_receipts,"all_kontos_dict":all_kontos} 
    return render(request, 'home/receipts.html',context)

@login_required()
def contacts(request):
    if 'edit' in request.GET:
        knummer = request.GET.get('edit')
        receipt_to_edit = receipt.objects.get(kontaktnummer=knummer)
        form = EditContactForm(instance=receipt_to_edit)
    else:
        form = EditContactForm()
    all_contacts = contact.objects.all()
    all_contacts_dict = {
        'contact': all_contacts
    }
    context = {"title": "Kontakte","all_contacts_dict": all_contacts,"form": form}
    return render(request, 'home/contacts.html',context)

@login_required()
def bills(request):
    context = {"title": "Rechnungen"}
    return render(request, 'home/bills.html',context)

@login_required()
def todos(request):
    context = {"title": "To-Do's"}
    return render(request, 'home/todos.html',context)

@login_required()
def accountDetails(request):
    
    all_einnahmen = receipt.objects.filter(konto_name='Personalausgaben',art='Einnahme')
    all_einnahmen_dict = {
        'einnahme': all_einnahmen
    }
    summe_e = receipt.objects.filter(konto_name='Personalausgaben',art='Einnahme').aggregate(sum=Sum('betrag'))['sum']
    print(summe_e)
    
    all_ausgaben = receipt.objects.filter(konto_name = 'Personalausgaben',art='Ausgabe')
    all_ausgaben_dict = {
        'receipt': all_ausgaben
    }
    summe_a = receipt.objects.filter(konto_name='Personalausgaben',art='Ausgabe').aggregate(sum=Sum('betrag'))['sum']
    name = 'Personalausgaben'

    
    context = {"title": "Details","all_ausgaben_dict": all_ausgaben,"all_einnahmen_dict":all_einnahmen,"konto":name,
        "summe_einnahmen":summe_e,"summe_ausgaben":summe_a}
    return render(request, 'home/accountDetails.html',context)