from django import forms
from django.forms import ModelForm,widgets
from home.models import receipt
from home.models import contact

class ReceiptForm(ModelForm): #Form anhand des Models aufgebaut
    class Meta: 
        model = receipt
        fields = '__all__'

class ContactForm(ModelForm): #Form anhand des Models aufgebaut
    class Meta: 
        model = contact 
        fields = '__all__'      

class AccountDetailForm(): #Form obsolete, Anzeigen der Detaildaten für Konten über Dict-Strukturen gelöst
    summe_einnahmen = forms.DecimalField()
    summe_ausgaben = forms.DecimalField()
    konto = forms.CharField(max_length=30)

class DashboardForm(ModelForm): #Form obsolete, Anzeigen der Daten im Dashboard über Dict-Strukturen gelöst 
    einnahmen = forms.DecimalField()
    ausgaben = forms.DecimalField()
    umsatz = forms.DecimalField()
    kleinugrenze_Umsatz = forms.DecimalField()
    kleinugrenze_Gewinn = forms.DecimalField()
    # def __init__(self,einnahmen,ausgaben,umsatz,kleinugrenze_Umsatz,kleinugrenze_Gewinn):
    #     self.einnahmen = einnahmen
    #     self.ausgaben = ausgaben
    #     self.umsatz = umsatz
    #     self.kleinugrenze_Umsatz = kleinugrenze_Umsatz
    #     self.kleinugrenze_Gewinn = kleinugrenze_Gewinn
