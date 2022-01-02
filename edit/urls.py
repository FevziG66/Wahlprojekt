from django.urls.conf import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

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
    path('editBankAccount/', views.editBankAccount, name='editBankAccount'),
    path('editToDos/', views.editToDos, name='editToDos'),


    path('change_password_form', auth_views.PasswordChangeView.as_view(template_name='edit/change_password_form.html', success_url=reverse_lazy('account:password_change_done')), name='change_password_form'),
    #path('password_change_done', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
]
