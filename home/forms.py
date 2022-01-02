from django.forms import ModelForm,widgets
from home.models import receipt
from home.models import contact

class ReceiptForm(ModelForm):
    class Meta: 
        model = receipt
        fields = '__all__'
        
class ContactForm(ModelForm):
    class Meta: 
        model = contact 
        fields = '__all__'      