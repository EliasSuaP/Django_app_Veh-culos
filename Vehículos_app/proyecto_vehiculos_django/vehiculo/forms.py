from django import forms

# Create your forms here

"""
Este script contiene el formulario django que se renderiza para ingresar vehículos en la base de datos
Tiene dos selects con el campo choice field para selección, se agrega estilo de boostrap en widget
"""

class VehiculoForm(forms.Form):
    marca = forms.ChoiceField(label='Marca', choices=[('Fiat', 'Fiat'),('Chevrolet', 'Chevrolet'), ('Ford', 'Ford'), ('Toyota', 'Toyota')], widget=forms.Select(attrs={'class': 'form-control'}))
    modelo = forms.CharField(label='Modelo',max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    serial_carroceria = forms.CharField(label='Serial carrocería', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    serial_motor = forms.CharField(label='Serial motor', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    categoria = forms.ChoiceField(label='Categoría', choices=[('Particular', 'Particular'), ('Transporte', 'Transporte'), ('Carga', 'Carga')], widget=forms.Select(attrs={'class': 'form-control'}))
    precio = forms.IntegerField(label='Precio', widget=forms.TextInput(attrs={'class': 'form-control'}))
