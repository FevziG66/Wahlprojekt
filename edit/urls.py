from django.urls.conf import path
from . import views

app_name = 'edit'
urlpatterns = [
    #User ruft den Pfad auf, der im ersten Parameter steht
    #danach wird View im 2.Parameter geladen, die in der Datei Views.py steht
    #Die Index View gibt unsere main.html Datei zurück
    #Name ist das, was im Browser angezeigt wird unter Pfad
    path('setttings/', views.settings, name='settings'),
    path('editBankData/', views.editBankData, name='editBankData'),
    path('deleteAccount/', views.deleteAccount, name='deleteAccount'),
    path('editReceipts/', views.editReceipts, name='editReceipts'),
    path('editContacts/', views.editContacts, name='editContacts'),
]