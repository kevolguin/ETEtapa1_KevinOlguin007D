from django.urls import path
from .views import index,crearUsuario,Ver,form_mod_usuario,form_del_usuario

urlpatterns = [

    path('', index, name="index"), 
    path('crear_usuario',crearUsuario, name="crearUsuario"),
    path('ver',Ver, name="ver"),
    path('form_mod_usuario/<id>', form_mod_usuario, name="form_mod_usuario"),
    path('form_del_usuario/<id>', form_del_usuario, name="form_del_usuario")
]