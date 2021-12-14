from django.forms import ModelForm, widgets
from edit.models import receipt

class ReceiptForm(ModelForm):
    class Meta: 
        model = receipt
        fields = '__all__'
        widgets = {
            'belegdatum' : widgets.DateInput(attrs={'type': 'date'}),
            'faelligkeit' : widgets.DateInput(attrs={'type': 'date'})
        }
        