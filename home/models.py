from django.db import models

# Create your models here.
class receipt(models.Model):
    #belegnummer = models.IntegerField()
    belegdatum = models.DateField()
    zahlart = [('B','Bar'),
                ('K','Karte'),]
    faelligkeit = models.DateField()
    betrag = models.DecimalField(max_digits=10,decimal_places=2)
    #datei = models.FileField()
    beschreibung = models.CharField(max_length=150)
