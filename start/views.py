# Create your views here.
from django.shortcuts import redirect, render
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from .forms import RegisterForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as logouts
from django.contrib.auth.decorators import login_required

#Methoden, die in Urls.py aufgerufen werden. Diese geben eine Html Datei und den dazugehörigen Titel zurück
def aboutUs(request):
    context = {"title": "Über uns"}
    return render(request, 'start/aboutUs.html',context)

def impressum(request):
    context = {"title": "Impressum"}
    return render(request, 'start/impressum.html',context)

def register(request):
    #Wenn es sich um eine POST-Anfrage handelt, müssen wir die Formulardaten verarbeiten
    template = 'start/register.html'
   
    if request.method == 'POST':
        # Formularinstanz erstellen und mit Daten der Anfrage füllen
        form = RegisterForm(request.POST)
        # Prüfen, ob es gültig ist
        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data['username']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Benutzername existiert bereits.'
                })
            elif User.objects.filter(email=form.cleaned_data['email']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Email-Adresse existiert bereits.'
                })
            elif form.cleaned_data['passwort'] != form.cleaned_data['passwort_wiederholen']:
                return render(request, template, {
                    'form': form,
                    'error_message': 'Passwörter stimmen nicht überein.'
                })
            else:
                # User erstellen
                user = User.objects.create_user(
                    form.cleaned_data['username'],
                    form.cleaned_data['email'],
                    form.cleaned_data['passwort']
                )
                
                user.first_name = form.cleaned_data['vorname']
                user.last_name = form.cleaned_data['nachname']
                user.save()
                
                #ungetestet, nicht umgesetzt
                #Standardkonten für User anlegen, z.B. 
                #Büromaterial, Fuhrpark, Miete, Personal, Portokasse, Einnahmen, Dienstleistungen, Lizenzen, Spenden, Gewinn

                # User einloggen
                login(request, user)
               
                # Redirect zur Login Seite
                return render(request, 'start/login.html')

   #Keine POST Daten vorhanden, nur die Seite anzeigen.
    else:
        form = RegisterForm()

    return render(request, template, {'form': form})

def user_login(request):
    if request.method == 'POST':
        # Anfrage bearbeiten, wenn Daten vorhanden
        username = request.POST['username']
        password = request.POST['password']
        # Überprüfen ob Username und Passwort korrekt sind
        user = authenticate(username=username, password=password)
        if user is not None:
            #Session Cookie speichern, damit man sich anmelden kann
            login(request, user)
            #User anmmelden
            return render(request, 'home/dashboard.html')
        else:
            #Falsche Eingaben, Error anzeigen
            return render(request, 'start/login.html', {'error_message': 'Falscher Username oder Passwort.'})
    else:
        #Keine POST Daten vorhanden, nur die Seite anzeigen.
        return render(request, 'start/login.html')

def logout(request):
    if request.method == 'POST':
        logouts(request)
        return render(request, 'start/login.html/')

def forgotPassword(request):
    context = {"title": "Passwort vergessen"}
    return render(request, 'start/forgotPassword.html',context)

def reset_password(request):
    context = {"title": "Passwort zurücksetzen"}
    return render(request, 'start/password_reset.html',context)

def password_reset_done(request):
    context = {"title": "Passwort zurücksetzen"}
    return render(request, 'start/password_reset_done.html',context)

@login_required()
def emailSend(request):
    context = {"title": "Passwort zurücksetzen"}
    return render(request, 'start/emailSend.html',context)

@login_required()
def resetPassword(request):
    context = {"title": "Neues Passwort festlegen"}
    return render(request, 'start/resetPassword.html',context)

@login_required()
def resetPasswordDone(request):
    context = {"title": "Passwort geändert"}
    return render(request, 'start/resetPasswordDone.html',context)