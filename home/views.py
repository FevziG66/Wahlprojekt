from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from home.models import contact, receipt, todo
from home.forms import ReceiptForm
from edit.forms import ReceiptForm as EditReceiptForm
from edit.forms import EditContactForm
from home.forms import ContactForm
from django.contrib.auth.decorators import login_required


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
    context = {"title": "Konten"}
    return render(request, 'home/accounts.html',context)

@login_required()
def receipts(request):
    if 'edit' in request.GET:
        bnummer = request.GET.get('edit')
        print(bnummer)
        receipt_to_edit = receipt.objects.get(belegnummer=bnummer)
        form = EditReceiptForm(instance=receipt_to_edit)
    else:
        form = EditReceiptForm()
    all_receipts = receipt.objects.all()
    all_receipts_dict = {
        'receipt': all_receipts
    }

    context = {"title": "Belege","all_receipts_dict": all_receipts,"form":form}
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
    context = {"title": "Konten"}
    return render(request, 'home/accountDetails.html',context)