from django import forms
from .models import Gasto

class GastoForm(forms.ModelForm):
    class Meta:
        model = Gasto
        fields = ['descripcion', 'monto', 'fecha']
        widgets = {
            'descripcion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Descripción del gasto'}),
            'monto': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0.00'}),
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }