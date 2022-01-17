from django.forms import ModelForm, widgets
import datetime
from django.forms.models import ModelChoiceField
from home.models import contact, receipt, konto, todo

from home.models import contact, receipt
from django import forms

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
        
class EditAccountForm(ModelForm):
    class Meta:
        model = konto
        fields = '__all__'

class EditTodoForm(ModelForm):
    class Meta: 
        model = todo
        fields = '__all__'
        widgets = {
            'datum' : widgets.DateInput(attrs={'type': 'date'}),
            'faelligkeit' : widgets.DateInput(attrs={'type': 'date'})
        }
    
