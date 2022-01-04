from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    vorname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    nachname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    passwort = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    passwort_wiederholen = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))