from time import timezone
from django.db import models
import datetime
from django.contrib.auth.models import User
# Create your models here.

#Model für Beleg 
class receipt(models.Model):
    belegnummer = models.IntegerField()
    belegdatum = models.DateField(default=datetime.date.today) #Belegdatum automatisch vorbelegen
    zahlart_choices = [('Bar','Bar'), #verschiedene Zahlarten, beliebig erweiterbar 
                ('Karte','Karte'),]
    zahlart = models.CharField(max_length=10,choices=zahlart_choices,default="Karte")            
    faelligkeit = models.DateField(default=datetime.date.today)
    betrag = models.DecimalField(max_digits=10,decimal_places=2)
    beschreibung = models.CharField(max_length=150)
    konto_name = models.ForeignKey('konto',on_delete=models.CASCADE,to_field='name')#Fremdbeziehung zu Konto
    art_choices = [('Einnahme','Einnahme'),
                ('Ausgabe','Ausgabe'),
                ]
    #user = models.ForeignKey(User,on_delete=models.CASCADE)#Beleg User zuweisen
    art = models.CharField(max_length=20,choices=art_choices,default="Einnahme")#Einnahme oder Ausgabe, 
                                                                                #wichtig für spätere Auswertungen
                                                                                #user = models.ForeignKey(User,on_delete=models.CASCADE)#Beleg User zuweisen
     #user = models.ForeignKey(User,on_delete=models.CASCADE)#Beleg User zuweisen
    #ungetestet, Daten zum User zuordnen

    

class contact(models.Model):
    kontaktnummer = models.IntegerField()
    firma = models.CharField(max_length=25)
    ansprechpartner = models.CharField(max_length=40)
    adresse = models.CharField(max_length=50)
    telefonnummer = models.CharField(max_length=15)
    email = models.EmailField(max_length=254)
    #user = models.ForeignKey(User,on_delete=models.CASCADE)#Beleg User zuweisen
    #user = models.ForeignKey(User,on_delete=models.CASCADE)#Beleg User zuweisen
    #ungetestet, Daten zum User zuordnen

class todo(models.Model):
    nummer = models.IntegerField()
    aufgabe = models.CharField(max_length=30)
    erledigt = models.IntegerField() #erledigt = 1, 'noch nicht erledigt'= 0 
    datum = models.DateField()
    faelligkeit = models.DateField()
    beschreibung = models.CharField(max_length=50)
    #user = models.ForeignKey(User,on_delete=models.CASCADE)#Beleg User zuweisen
    #ungetestet, Daten zum User zuordnen

class konto(models.Model):
    name = models.CharField(max_length=30,primary_key=True)#als Primary Key gesetzt, wird in in Beleg zu Zuordnung verwendet
    bank = models.CharField(max_length=40)
    iban = models.CharField(max_length=22) #IBAN in Deutschland = 22 Stellen 
    bic = models.CharField(max_length=10)
    kontostand = models.DecimalField(max_digits=10,decimal_places=2) # 10-stellige Zahl, für Kleinunternehmer ausreichend
    #user = models.ForeignKey(User,on_delete=models.CASCADE)#Beleg User zuweisen
    #ungetestet, Daten zum User zuordnen