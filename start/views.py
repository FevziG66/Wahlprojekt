from django.contrib import auth
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
# Create your views here.
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout

#def register(request):
#    context = {"title": "Account anlegen"}
#    return render(request, 'start/register.html',context)

#def login(request):
#    context = {"title": "Anmelden"}
#    return render(request, 'start/login.html',context)

def aboutUs(request):
    context = {"title": "Über uns"}
    return render(request, 'start/aboutUs.html',context)

def impressum(request):
    context = {"title": "Impressum"}
    return render(request, 'start/impressum.html',context)

def forgotPassword(request):
    context = {"title": "Passwort vergessen"}
    return render(request, 'start/forgotPassword.html',context)

def emailSend(request):
    context = {"title": "Passwort zurücksetzen"}
    return render(request, 'start/emailSend.html',context)

def resetPassword(request):
    context = {"title": "Passwort zurücksetzen"}
    return render(request, 'start/resetPassword.html',context)

def resetPasswordDone(request):
    context = {"title": "Passwort geändert"}
    return render(request, 'start/resetPasswordDone.html',context)
def register(request):
    # if this is a POST request we need to process the form data
    template = 'start/register.html'
   
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data['username']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Unternehmen existiert bereits.'
                })
            elif User.objects.filter(email=form.cleaned_data['email']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Email-Adresse existiert bereits.'
                })
            elif form.cleaned_data['password'] != form.cleaned_data['password_repeat']:
                return render(request, template, {
                    'form': form,
                    'error_message': 'Passwörter stimmen nicht überein.'
                })
            else:
                # User erstellen
                user = User.objects.create_user(
                    form.cleaned_data['username'],
                    form.cleaned_data['email'],
                    form.cleaned_data['password']
                )
                user.first_name = form.cleaned_data['first_name']
                user.last_name = form.cleaned_data['last_name']
                user.save()
               
                # User einloggen
                login(request, user)
               
                # Redirect zur Login Seite
                return HttpResponseRedirect('home/dashboard.html')

   # No post data availabe, let's just show the page.
    else:
        form = RegisterForm()

    return render(request, template, {'form': form})

def user_login(request):
    if request.method == 'POST':
        # Process the request if posted data are available
        username = request.POST['username']
        password = request.POST['password']
        # Überprüfen ob Username und Passwort korrekt
        user = authenticate(username=username, password=password)
        if user is not None:
            # Session Cookie speichern, damit man sich anmelden kann
            login(request, user)
            # User anmmelden
            return render(request, 'home/dashboard.html')
        else:
            # Falsche Eingaben, Error anzeigen
            return render(request, 'start/login.html', {'error_message': 'Incorrect username and / or password.'})
    else:
        # No post data availabe, let's just show the page to the user.
        return render(request, 'start/login.html')


def logout_view(request):
        logout(request)
        return redirect('start/login/')