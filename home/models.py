from django.db import models

# Create your models here.
class receipt(models.Model):
    belegnummer = models.IntegerField()
    belegdatum = models.DateField()
    zahlart_choices = [('Bar','Bar'),
                ('Karte','Karte'),]
    zahlart = models.CharField(max_length=10,choices=zahlart_choices,default="Karte")            
    faelligkeit = models.DateField()
    betrag = models.DecimalField(max_digits=10,decimal_places=2)
    #datei = models.FileField()
    beschreibung = models.CharField(max_length=150)
    
class contact(models.Model):
    kontaktnummer = models.IntegerField()
    firma = models.CharField(max_length=25)
    ansprechpartner = models.CharField(max_length=40)
    adresse = models.CharField(max_length=50)
    telefonnummer = models.CharField(max_length=15)
    email = models.EmailField(max_length=254)

class todo(models.Model):
    aufgabe = models.CharField(max_length=50)
    erledigt = models.IntegerField()

