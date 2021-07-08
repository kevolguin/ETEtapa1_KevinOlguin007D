from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from . models import  Usuario

class UsuarioForm(forms.ModelForm):

    class Meta: 
        model= Usuario
        fields = ['rut', 'nombre', 'telefono', 'direccion','email','pais','contrasena','image']
        labels ={
            'rut': 'Rut', 
            'nombre': 'Nombre', 
            'telefono': 'Telefono', 
            'direccion': 'Direccion',
            'email': 'Email',
            'pais': 'Pais',
            'contrasena': 'Contraseña',
            'image': 'Image',
        }
        widgets={
            'rut': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese rut', 
                    'id': 'rut'
                }
            ), 
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese nombre', 
                    'id': 'nombre'
                }
            ), 
            'telefono': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese telefono', 
                    'id': 'telefono'
                }
            ), 
            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese dirección', 
                    'id': 'direccion',
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese email', 
                    'id': 'email',
                }
            ),
            'pais': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese pais', 
                    'id': 'pais',
                }
            ),
            'contrasena': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese contraseña', 
                    'id': 'contrasena',
                }
            ),
            'image': forms.ClearableFileInput(
            attrs={
                'class':'form-control',
                'id': 'image'
            }
            ),
        }
