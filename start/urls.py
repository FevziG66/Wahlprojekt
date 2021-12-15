from django.urls.conf import path
from . import views
from django.conf.urls import url

app_name = 'start'
urlpatterns = [
    #User ruft den Pfad auf, der im ersten Parameter steht
    #danach wird View im 2.Parameter geladen, die in der Datei Views.py steht
    #Die Index View gibt unsere main.html Datei zurück
    #Name ist das, was im Browser angezeigt wird unter Pfad
    path('', views.aboutUs, name='aboutUs'), 
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='user_login'),
    path('impressum/', views.impressum, name='impressum'),
    path('forgotPassword/', views.forgotPassword, name='forgotPassword'),
    path('emailSend/', views.emailSend, name='emailSend'),
    path('resetPassword/', views.resetPassword, name='resetPassword'),
    path('resetPasswordDone/', views.resetPasswordDone, name='resetPasswordDone'),
    #url(r'^register/$', views.user_register, name='user_register')
]