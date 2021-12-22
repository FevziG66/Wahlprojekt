from django.forms import ModelForm, widgets
from home.models import contact, receipt

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
        