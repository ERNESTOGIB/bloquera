from django import forms
from .models import Cat_M_Empleado

class frmCat_M_Empleado(forms.ModelForm):
    
    class Meta:
        model = Cat_M_Empleado
        fields = [
            'IDEmpleado',
            'NombreEmpleado',
            'Foto',
            'Direccion',
            'NSS',
            'Rfc',
            'Email',
            'Telefono1',
            'PeriodoPago',
            'Sueldo',
            'HorasExtra',
            'Area',
            'MontoHoraExtra',
            'Puesto',
        ]