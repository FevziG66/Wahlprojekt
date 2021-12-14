from django.forms import ModelForm
from home.models import receipt

class ReceiptForm(ModelForm):
    class Meta: 
        model = receipt
        fields = '__all__'