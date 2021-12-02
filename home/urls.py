from django.urls.conf import path
from . import views

app_name = 'home'
urlpatterns = [
    #User ruft den Pfad auf, der im ersten Parameter steht
    #danach wird View im 2.Parameter geladen, die in der Datei Views.py steht
    #Die Index View gibt unsere main.html Datei zurück
    #Name ist das, was im Browser angezeigt wird unter Pfad
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),
    path('accounts/', views.accounts, name='accounts'),
    path('receipts/', views.receipts, name='receipts'),
    path('contacts/', views.contacts, name='contacts'),
]