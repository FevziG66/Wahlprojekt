from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from edit.models import receipt
from home.forms import ReceiptForm
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
    if request.method == "POST":
        print('ja')
    else: 
        all_receipts = receipt.objects.all()
        all_receipts_dict = {
            'receipt': all_receipts
        }
        # context = {
        #     'all_receipts_dict':all_receipts
        # }
    context = {"title": "Belege","all_receipts_dict": all_receipts_dict}
    return render(request, 'home/receipts.html',context)

def contacts(request):
    context = {"title": "Kontakte"}
    return render(request, 'home/contacts.html',context)

def bills(request):
    context = {"title": "Rechnungen"}
    return render(request, 'home/bills.html',context)