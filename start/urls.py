from django.urls.conf import path
from . import views
from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
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
    path('logout/', views.logout, name='logout'),
    #url(r'^register/$', views.user_register, name='user_register')

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='start/password_reset.html'), name='reset_password'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='start/password_reset_done.html'), name='password_reset_done'),
    path("password_reset_confirm/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name='start/password_reset_confirm.html'), name='password_reset_confirm'),
    path("password_reset_complete/", auth_views.PasswordResetCompleteView.as_view(template_name='start/password_reset_complete.html'), name='password_reset_complete'),
]