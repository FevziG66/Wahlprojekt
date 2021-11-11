from django.urls.conf import path
from . import views

app_name = 'start'
urlpatterns = [
    #User ruft den Pfad auf, der im ersten Parameter steht
    #danach wird die "index View" geladen, die in der Datei Views.py steht
    #Die Index View gibt unsere main.html Datei zurück
    #Name ist das, was im Browser angezeigt wird unter Pfad
    path('', views.aboutUs, name='aboutUs'), 
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('impressum/', views.impressum, name='impressum'), 
]
