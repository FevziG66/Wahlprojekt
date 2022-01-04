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
    beschreibung = models.CharField(max_length=150)
    konto_name = models.ForeignKey('konto',on_delete=models.CASCADE,to_field='name')
    art_choices = [('Einnahme','Einnahme'),
                ('Ausgabe','Ausgabe'),]
    art = models.CharField(max_length=10,choices=art_choices,default="Einnahme")

    

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

class konto(models.Model):
    name = models.CharField(max_length=30,primary_key=True)
    bank = models.CharField(max_length=40)
    iban = models.CharField(max_length=22)
    bic = models.CharField(max_length=10)
    kontostand = models.DecimalField(max_digits=10,decimal_places=2)