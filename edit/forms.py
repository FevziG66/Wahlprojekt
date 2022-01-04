from django.forms import ModelForm, widgets
<<<<<<< HEAD
from django.forms.models import ModelChoiceField
from home.models import contact, receipt, konto
=======
from home.models import contact, receipt
from django import forms
>>>>>>> c4103381d4a2c998f742d5869d601ca9c45f520e

class ReceiptForm(ModelForm):
    class Meta: 
        model = receipt
        fields = '__all__'
        widgets = {
            'belegdatum' : widgets.DateInput(attrs={'type': 'date'}),
            'faelligkeit' : widgets.DateInput(attrs={'type': 'date'})
        }

class EditContactForm(ModelForm):
    class Meta: 
        model = contact
        fields = '__all__'
<<<<<<< HEAD
        
class EditAccountForm(ModelForm):
    class Meta:
        model = konto
        fields = '__all__'
    
=======

>>>>>>> c4103381d4a2c998f742d5869d601ca9c45f520e
