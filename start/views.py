from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
# Create your views here.
def index(request):
    return render(request, 'start/main.html')

def register(request):
    register_form = UserCreationForm()
    #Wir übergeben die Form an unsere Html Datei
    return render(request, 'start/register.html', {'register_form': register_form})

def login(request):
    login_form = AuthenticationForm()
    #Wir übergeben die Form an unsere Html Datei
    return render(request, 'start/login.html', {'login_form': login_form})

def aboutUs(request):
    return render(request, 'start/aboutUs.html')

def impressum(request):
    return render(request, 'start/impressum.html')