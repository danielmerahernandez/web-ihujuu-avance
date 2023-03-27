# librerias del crud
from contextlib import _RedirectStream, redirect_stdout
from django.shortcuts import render 
from modulo1.models import *
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import CustomUserForm
from django.contrib.auth import login, authenticate
#importo el modelo de la base de datos de models.py
from django.contrib import messages 
 
# Habilitamos los mensajes para class-based views 
from django.contrib.messages.views import SuccessMessageMixin 
 

# Habilitamos el uso de mensajes en Django
from django.contrib import messages

# Habilitamos los mensajes para class-based views
from django.contrib.messages.views import SuccessMessageMixin

# Habilitamos los formularios en Django
from django import forms
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def Home2(request):
    return render(request, "tours.html")

def Home1(request):
    return render(request, "index3.html")

def Login(request):
    return render (request, "login.html")

def Discografia(request):
    return render (request, "vista-usuario/discography.html")

def Index(request):
    return render (request, "vista-usuario/index-vistap.html")

#----------------------------------registro--------------------------------------------#
def registro_usuario(request):
    data = {
        'form': CustomUserForm()
    }
    if request.method == 'POST':
        formulario = CustomUserForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect (to='index3.html')


    return render(request, 'registration/registrar.html', data)

#----------------------------------registro--------------------------------------------#


# Create your views here.





#-----------------------accionpermitida--------------------------------#
class ListadoAccionpermitida(ListView):
     model = Accionpermitida
    
class AccionpermitidaCrear(SuccessMessageMixin, CreateView):
    model = Accionpermitida
    form = Accionpermitida
    fields = "__all__"
    success_message ='Accionpermitida creada correctamente'
     
    def get_success_url(self):        
        return reverse('modulo1:leerccion') # Redireccionamos a la vista principal 'leer'

class AccionpermitidaDetalle (DetailView):
    model =Accionpermitida

class  AccionpermitidaActualizar(SuccessMessageMixin,UpdateView):
    model =  Accionpermitida
    form = Accionpermitida
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Contratos Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('modulo1:leerccion') # Redireccionamos a la vista principal 'leer'
class AccionpermitidaEliminar(SuccessMessageMixin, DeleteView): 
    model = Accionpermitida 
    form = Accionpermitida
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Accionpermitida Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('modulo1:leerccion') # Redireccionamos a la vista principal 'leer'
 
#-----------------------accionpermitida--------------------------------#
#-----------------------eventos--------------------------------#
class ListadoEvento(ListView):
     model = Evento
    
class EventoCrear(SuccessMessageMixin, CreateView):
    model = Evento
    form = Evento
    fields = "__all__"
    success_message ='Evento creada correctamente'
     
    def get_success_url(self):        
        return reverse('modulo1:leerccion') # Redireccionamos a la vista principal 'leer'

class EventoDetalle (DetailView):
    model =Evento

class  EventoActualizar(SuccessMessageMixin,UpdateView):
    model =  Evento
    form = Evento
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Contratos Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('modulo1:leerccion') # Redireccionamos a la vista principal 'leer'
class EventoEliminar(SuccessMessageMixin, DeleteView): 
    model = Evento
    form = Evento
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Accionpermitida Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('modulo1:leerccion') # Redireccionamos a la vista principal 'leer'
 
#-----------------------eventos--------------------------------#
#-----------------------accionpermitidahasplantilla--------------------------------#
class ListadoAccionpermitidaHasPlantilla(ListView):
     model = AccionpermitidaHasPlantilla
    
class AccionpermitidaHasPlantillaCrear(SuccessMessageMixin, CreateView):
    model = AccionpermitidaHasPlantilla
    form = AccionpermitidaHasPlantilla
    fields = "__all__"
    success_message ='AccionPermitidaHasPlantilla creada correctamente'
     
    def get_success_url(self):        
        return reverse('modulo1:leerplan') # Redireccionamos a la vista principal 'leer'

class AccionpermitidaHasPlantillaDetalle (DetailView):
    model =AccionpermitidaHasPlantilla

class  AccionpermitidaHasPlantillaActualizar(SuccessMessageMixin,UpdateView):
    model =  AccionpermitidaHasPlantilla
    form = AccionpermitidaHasPlantilla
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Contratos Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('modulo1:leerplan') # Redireccionamos a la vista principal 'leer'
class AccionpermitidaHasPlantillaEliminar(SuccessMessageMixin, DeleteView): 
    model = AccionpermitidaHasPlantilla
    form = AccionpermitidaHasPlantilla
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Accionpermitida Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('modulo1:leerplan') # Redireccionamos a la vista principal 'leer'
 
#-----------------------accionpermitidahasplantilla--------------------------------#

#-----------------------ListadoAccionpermitidaHasUsuario--------------------------------#
class ListadoAccionpermitidaHasUsuario(ListView):
     model = AccionpermitidaHasUsuario
    
class AccionpermitidaHasUsuarioCrear(SuccessMessageMixin, CreateView):
    model = AccionpermitidaHasUsuario
    form = AccionpermitidaHasUsuario
    fields = "__all__"
    success_message ='AccionpermitidaHasUsuario creada correctamente'
     
    def get_success_url(self):        
        return reverse('modulo1:leerplanUsuario') # Redireccionamos a la vista principal 'leer'

class AccionpermitidaHasUsuarioDetalle (DetailView):
    model =AccionpermitidaHasUsuario

class  AccionpermitidaHasUsuarioActualizar(SuccessMessageMixin,UpdateView):
    model =  AccionpermitidaHasUsuario
    form = AccionpermitidaHasUsuario
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Contratos Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('modulo1:leerplanUsuario') # Redireccionamos a la vista principal 'leer'
class AccionpermitidaHasUsuarioEliminar(SuccessMessageMixin, DeleteView): 
    model = AccionpermitidaHasUsuario
    form = AccionpermitidaHasUsuario
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'AccionpermitidaHasUsuario Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('modulo1:leerplanUsuario') # Redireccionamos a la vista principal 'leer'
 
#-----------------------ListadoAccionpermitidaHasUsuario--------------------------------#

#-----------------------cronograma--------------------------------#
class ListadoCronograma(ListView):
     model = Cronograma
    
class CronogramaCrear(SuccessMessageMixin, CreateView):
    model = Cronograma
    form = Cronograma
    fields = "__all__"
    success_message ='Cronograma creada correctamente'
     
    def get_success_url(self):        
        return reverse('modulo1:leerCronograma') # Redireccionamos a la vista principal 'leer'

class CronogramaDetalle (DetailView):
    model = Cronograma

class  CronogramaActualizar(SuccessMessageMixin,UpdateView):
    model =  Cronograma
    form = Cronograma
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Cronograma Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('modulo1:leerCronograma') # Redireccionamos a la vista principal 'leer'
class CronogramaEliminar(SuccessMessageMixin, DeleteView): 
    model = Cronograma
    form = Cronograma
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'AccionpermitidaHasUsuario Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('modulo1:leerCronograma') # Redireccionamos a la vista principal 'leer'
 
#-----------------------cronograma--------------------------------#

#-----------------------Departamento--------------------------------#
class ListadoDepartamento(ListView):
     model = Departamento
    
class DepartamentoCrear(SuccessMessageMixin, CreateView):
    model = Departamento
    form = Departamento
    fields = "__all__"
    success_message ='Departamento creada correctamente'
     
    def get_success_url(self):        
        return reverse('modulo1:leeroti') # Redireccionamos a la vista principal 'leer'

class DepartamentoDetalle (DetailView):
    model =Departamento

class  DepartamentoActualizar(SuccessMessageMixin,UpdateView):
    model =  Cronograma
    form = Cronograma
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Cronograma Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('modulo1:leeroti') # Redireccionamos a la vista principal 'leer'
class DepartamentoEliminar(SuccessMessageMixin, DeleteView): 
    model = Departamento
    form = Departamento
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'AccionpermitidaHasUsuario Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('modulo1:leeroti') # Redireccionamos a la vista principal 'leer'
 
#-----------------------departamento--------------------------------#

#-----------------------Reserva--------------------------------#
class ListadoReserva(ListView):
     model = Reserva
    
class ReservaCrear(SuccessMessageMixin, CreateView):
    model = Reserva
    form = Reserva
    fields = "__all__"
    success_message ='Reserva creada correctamente'
     
    def get_success_url(self):        
        return reverse('modulo1:leereserva') # Redireccionamos a la vista principal 'leer'

class ReservaDetalle (DetailView):
    model = Reserva

class ReservaActualizar(SuccessMessageMixin,UpdateView):
    model =  Reserva
    form = Reserva
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Cronograma Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('modulo1:leereserva') # Redireccionamos a la vista principal 'leer'
class ReservaEliminar(SuccessMessageMixin, DeleteView): 
    model = Reserva
    form = Reserva
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'AccionpermitidaHasUsuario Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('modulo1:leereserva') # Redireccionamos a la vista principal 'leer'
 
#-----------------------reserva--------------------------------#

#-----------------------Establecimiento--------------------------------#
class ListadoEstablecimiento(ListView):
     model = Establecimiento
    
class EstablecimientoCrear(SuccessMessageMixin, CreateView):
    model =Establecimiento
    form = Establecimiento
    fields = "__all__"
    success_message ='Reserva creada correctamente'
     
    def get_success_url(self):        
        return reverse('modulo1:leerestable') # Redireccionamos a la vista principal 'leer'

class EstablecimientoDetalle (DetailView):
    model = Reserva

class EstablecimientoActualizar(SuccessMessageMixin,UpdateView):
    model =  Establecimiento
    form = Establecimiento
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Cronograma Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('modulo1:leerestable') # Redireccionamos a la vista principal 'leer'
class EstablecimientoEliminar(SuccessMessageMixin, DeleteView): 
    model = Establecimiento
    form = Establecimiento
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'AccionpermitidaHasUsuario Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('modulo1:leerestable') # Redireccionamos a la vista principal 'leer'
 
#-----------------------Establecimiento--------------------------------#

#-----------------------Establedispo--------------------------------#
class ListadoEstabledispo(ListView):
     model = Establedispo
    
class EstabledispoCrear(SuccessMessageMixin, CreateView):
    model =Establedispo
    form = Establedispo
    fields = "__all__"
    success_message ='Establedispo creada correctamente'
     
    def get_success_url(self):        
        return reverse('modulo1:leerestabledis') # Redireccionamos a la vista principal 'leer'

class EstabledispoDetalle (DetailView):
    model = Establedispo

class EstabledispoActualizar(SuccessMessageMixin,UpdateView):
    model =  Establedispo
    form = Establedispo
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Establedispo Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('modulo1:leerestabledis') # Redireccionamos a la vista principal 'leer'
class EstabledispoEliminar(SuccessMessageMixin, DeleteView): 
    model = Establedispo
    form = Establedispo
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Establedispo Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('modulo1:leerestabledis') # Redireccionamos a la vista principal 'leer'
 
#-----------------------Establedispo--------------------------------#


#-----------------------Estado--------------------------------#
class ListadoEstado(ListView):
     model = Establedispo
    
class EstadoCrear(SuccessMessageMixin, CreateView):
    model = Estado
    form = Estado
    fields = "__all__"
    success_message ='Estado creada correctamente'
     
    def get_success_url(self):        
        return reverse('modulo1:leerestado') # Redireccionamos a la vista principal 'leer'

class EstadoDetalle (DetailView):
    model = Estado

class EstadoActualizar(SuccessMessageMixin,UpdateView):
    model =  Estado
    form = Estado
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Estado Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('modulo1:leerestado') # Redireccionamos a la vista principal 'leer'
class EstadoEliminar(SuccessMessageMixin, DeleteView): 
    model = Estado
    form = Estado
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Estado Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('modulo1:leerestado') # Redireccionamos a la vista principal 'leer'
 
#-----------------------estado--------------------------------#

#-----------------------Estadocivil--------------------------------#
class ListadoEstadocivil(ListView):
     model = Estadocivil
    
class EstadocivilCrear(SuccessMessageMixin, CreateView):
    model = Estadocivil
    form = Estadocivil
    fields = "__all__"
    success_message ='Estadocivil creada correctamente'
     
    def get_success_url(self):        
        return reverse('modulo1:leerestadocivil') # Redireccionamos a la vista principal 'leer'

class EstadocivilDetalle (DetailView):
    model = Estadocivil

class EstadocivilActualizar(SuccessMessageMixin,UpdateView):
    model =  Estadocivil
    form = Estadocivil
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Estadocivil Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('modulo1:leerEstadocivil') # Redireccionamos a la vista principal 'leer'
class EstadocivilEliminar(SuccessMessageMixin, DeleteView): 
    model = Estadocivil
    form = Estadocivil
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Estadocivil Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('modulo1:leerestadocivil') # Redireccionamos a la vista principal 'leer'
 
#-----------------------Estadocivil--------------------------------#

#-----------------------Estagenemusi--------------------------------#
class ListadoEstagenemusi(ListView):
     model = Estagenemusi
    
class EstagenemusiCrear(SuccessMessageMixin, CreateView):
    model = Estagenemusi
    form = Estagenemusi
    fields = "__all__"
    success_message ='estagenemusi creada correctamente'
     
    def get_success_url(self):        
        return reverse('modulo1:leerestagenemusi') # Redireccionamos a la vista principal 'leer'

class EstagenemusiDetalle (DetailView):
    model = Estagenemusi

class EstagenemusiActualizar(SuccessMessageMixin,UpdateView):
    model =  Estagenemusi
    form = Estagenemusi
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Estagenemusi Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('modulo1:leerestagenemusi') # Redireccionamos a la vista principal 'leer'
class EstagenemusiEliminar(SuccessMessageMixin, DeleteView): 
    model = Estagenemusi
    form = Estagenemusi
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Estagenemusi Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('modulo1:leerestagenemusi') # Redireccionamos a la vista principal 'leer'
 
#-----------------------Estagenemusi--------------------------------#

#-----------------------Estatipgen--------------------------------#
class ListadoEstatipgen(ListView):
     model = Estatipgen
    
class EstatipgenCrear(SuccessMessageMixin, CreateView):
    model = Estatipgen
    form = Estatipgen
    fields = "__all__"
    success_message ='Estatipgen creada correctamente'
     
    def get_success_url(self):        
        return reverse('modulo1:leerestatipgen') # Redireccionamos a la vista principal 'leer'

class EstatipgenDetalle (DetailView):
    model = Estatipgen

class EstatipgenActualizar(SuccessMessageMixin,UpdateView):
    model =  Estatipgen
    form = Estatipgen
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Estatipgen Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('modulo1:leerestatipgen') # Redireccionamos a la vista principal 'leer'
class EstatipgenEliminar(SuccessMessageMixin, DeleteView): 
    model = Estatipgen
    form = Estatipgen
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Estatipgen Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('modulo1:leerestatipgen') # Redireccionamos a la vista principal 'leer'
 
#-----------------------Estatipgen--------------------------------#

#-----------------------EventoHasArtista--------------------------------#
class ListadoEventoHasArtista(ListView):
     model = EventoHasArtista
    
class EventoHasArtistaCrear(SuccessMessageMixin, CreateView):
    model = EventoHasArtista
    form = EventoHasArtista
    fields = "__all__"
    success_message ='EventoHasArtista creada correctamente'
     
    def get_success_url(self):        
        return reverse('modulo1:leerEventoHasArtista') # Redireccionamos a la vista principal 'leer'

class EventoHasArtistaDetalle (DetailView):
    model = EventoHasArtista

class EventoHasArtistaActualizar(SuccessMessageMixin,UpdateView):
    model =  EventoHasArtista
    form = EventoHasArtista
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'EventoHasArtista Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('modulo1:leereventoHasArtista') # Redireccionamos a la vista principal 'leer'
class EventoHasArtistaEliminar(SuccessMessageMixin, DeleteView): 
    model = EventoHasArtista
    form = EventoHasArtista
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'EventoHasArtista Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('modulo1:leereventoHasArtista') # Redireccionamos a la vista principal 'leer'
 
#-----------------------EventoHasArtista--------------------------------#

#-----------------------Genero--------------------------------#
class ListadoGenero(ListView):
     model = Genero
    
class GeneroCrear(SuccessMessageMixin, CreateView):
    model = Genero
    form = Genero
    fields = "__all__"
    success_message ='Genero creada correctamente'
     
    def get_success_url(self):        
        return reverse('modulo1:leergenero') # Redireccionamos a la vista principal 'leer'

class GeneroDetalle (DetailView):
    model = Genero

class GeneroActualizar(SuccessMessageMixin,UpdateView):
    model =  Genero
    form = Genero
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Genero Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('modulo1:leergenero') # Redireccionamos a la vista principal 'leer'
class GeneroEliminar(SuccessMessageMixin, DeleteView): 
    model = Genero
    form = Genero
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Genero Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('modulo1:leergenero') # Redireccionamos a la vista principal 'leer'
 
#-----------------------Genero--------------------------------#

#-----------------------Generomusica--------------------------------#
class ListadoGeneromusica(ListView):
     model = Generomusica
    
class GeneromusicaCrear(SuccessMessageMixin, CreateView):
    model = Generomusica
    form = Generomusica
    fields = "__all__"
    success_message ='Generomusica creada correctamente'
     
    def get_success_url(self):        
        return reverse('modulo1:leergeneromusica') # Redireccionamos a la vista principal 'leer'

class GeneromusicaDetalle (DetailView):
    model = Generomusica

class GeneromusicaActualizar(SuccessMessageMixin,UpdateView):
    model =  Generomusica
    form = Generomusica
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Generomusica Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('modulo1:leergeneromusica') # Redireccionamos a la vista principal 'leer'
class GeneromusicaEliminar(SuccessMessageMixin, DeleteView): 
    model = Generomusica
    form = Generomusica
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Generomusica Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('modulo1:leergeneromusica') # Redireccionamos a la vista principal 'leer'
 
#-----------------------Generomusica--------------------------------#

#-----------------------Municipio--------------------------------#
class ListadoMunicipio(ListView):
     model = Municipio
    
class MunicipioCrear(SuccessMessageMixin, CreateView):
    model = Municipio
    form = Municipio
    fields = "__all__"
    success_message ='Municipio creada correctamente'
     
    def get_success_url(self):        
        return reverse('modulo1:leermunicipio') # Redireccionamos a la vista principal 'leer'

class MunicipioDetalle (DetailView):
    model = Municipio

class MunicipioActualizar(SuccessMessageMixin,UpdateView):
    model =  Municipio
    form = Municipio
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Municipio Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('modulo1:leermunicipio') # Redireccionamos a la vista principal 'leer'
class MunicipioEliminar(SuccessMessageMixin, DeleteView): 
    model = Municipio
    form = Municipio
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Municipio Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('modulo1:leermunicipio') # Redireccionamos a la vista principal 'leer'
 
#-----------------------Municipio--------------------------------#

#-----------------------Organizador--------------------------------#
class ListadoOrganizador(ListView):
     model = Organizador
    
class OrganizadorCrear(SuccessMessageMixin, CreateView):
    model = Organizador
    form = Organizador
    fields = "__all__"
    success_message ='Organizador creada correctamente'
     
    def get_success_url(self):        
        return reverse('modulo1:leerorganizador') # Redireccionamos a la vista principal 'leer'

class OrganizadorDetalle (DetailView):
    model = Organizador

class OrganizadorActualizar(SuccessMessageMixin,UpdateView):
    model =  Organizador
    form = Organizador
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Organizador Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('modulo1:leerorganizador') # Redireccionamos a la vista principal 'leer'
class OrganizadorEliminar(SuccessMessageMixin, DeleteView): 
    model = Organizador
    form = Organizador
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Organizador Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('modulo1:leerorganizador') # Redireccionamos a la vista principal 'leer'
 
#-----------------------Organizador--------------------------------#

#-----------------------Pais--------------------------------#
class ListadoPais(ListView):
     model = Pais
    
class PaisCrear(SuccessMessageMixin, CreateView):
    model = Pais
    form = Pais
    fields = "__all__"
    success_message ='Pais creada correctamente'
     
    def get_success_url(self):        
        return reverse('modulo1:leerpais') # Redireccionamos a la vista principal 'leer'

class PaisDetalle (DetailView):
    model = Pais

class PaisActualizar(SuccessMessageMixin,UpdateView):
    model =  Pais
    form = Pais
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Pais Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('modulo1:leerpais') # Redireccionamos a la vista principal 'leer'
class PaisEliminar(SuccessMessageMixin, DeleteView): 
    model = Pais
    form = Pais
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Pais Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('modulo1:leerpais') # Redireccionamos a la vista principal 'leer'
 
#-----------------------Pais--------------------------------#

#-----------------------Persona--------------------------------#
class ListadoPersona(ListView):
     model = Persona
    
class PersonaCrear(SuccessMessageMixin, CreateView):
    model = Persona
    form = Persona
    fields = "__all__"
    success_message ='Persona creada correctamente'
     
    def get_success_url(self):        
        return reverse('modulo1:leerpersona') # Redireccionamos a la vista principal 'leer'

class PersonaDetalle (DetailView):
    model = Persona

class PersonaActualizar(SuccessMessageMixin,UpdateView):
    model =  Persona
    form = Persona
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Persona Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('modulo1:leerpersona') # Redireccionamos a la vista principal 'leer'
class PersonaEliminar(SuccessMessageMixin, DeleteView): 
    model = Persona
    form = Persona
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Persona Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('modulo1:leerpersona') # Redireccionamos a la vista principal 'leer'
 
#-----------------------Persona--------------------------------#

#-----------------------Plantilla--------------------------------#
class ListadoPlantilla(ListView):
     model = Plantilla
    
class PlantillaCrear(SuccessMessageMixin, CreateView):
    model = Plantilla
    form = Plantilla
    fields = "__all__"
    success_message ='Plantilla creada correctamente'
     
    def get_success_url(self):        
        return reverse('modulo1:leerplantilla') # Redireccionamos a la vista principal 'leer'

class PlantillaDetalle (DetailView):
    model = Plantilla

class PlantillaActualizar(SuccessMessageMixin,UpdateView):
    model =  Plantilla
    form = Plantilla
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Plantilla Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('modulo1:leerplantilla') # Redireccionamos a la vista principal 'leer'
class PlantillaEliminar(SuccessMessageMixin, DeleteView): 
    model = Plantilla
    form = Plantilla
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Plantilla Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('modulo1:leerplantilla') # Redireccionamos a la vista principal 'leer'
 
#-----------------------Plantilla--------------------------------#


#-----------------------Artista--------------------------------#
class ListadoArtista(ListView):
     model = Artista
    
class ArtistaCrear(SuccessMessageMixin, CreateView):
    model = Artista
    form = Artista
    fields = "__all__"
    success_message ='Artista creada correctamente'
     
    def get_success_url(self):        
        return reverse('modulo1:leerrtista') # Redireccionamos a la vista principal 'leer'

class ArtistaDetalle (DetailView):
    model = Artista

class ArtistaActualizar(SuccessMessageMixin,UpdateView):
    model =  Artista
    form = Artista
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Artista Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('modulo1:leerrtista') # Redireccionamos a la vista principal 'leer'
class ArtistaEliminar(SuccessMessageMixin, DeleteView): 
    model = Artista
    form = Artista
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Artista Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('modulo1:leerrtista') # Redireccionamos a la vista principal 'leer'
 
#-----------------------Artista--------------------------------#

#-----------------------Asiste--------------------------------#
class ListadoAsiste(ListView):
     model = Asiste
    
class AsisteCrear(SuccessMessageMixin, CreateView):
    model = Asiste
    form = Asiste
    fields = "__all__"
    success_message ='Asiste creada correctamente'
     
    def get_success_url(self):        
        return reverse('modulo1:leerAsiste') # Redireccionamos a la vista principal 'leer'

class AsisteDetalle (DetailView):
    model = Asiste

class AsisteActualizar(SuccessMessageMixin,UpdateView):
    model =  Asiste
    form = Asiste
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Asiste Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('modulo1:leerAsiste') # Redireccionamos a la vista principal 'leer'
class AsisteEliminar(SuccessMessageMixin, DeleteView): 
    model = Asiste
    form = Asiste
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Asiste Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('modulo1:leerAsiste') # Redireccionamos a la vista principal 'leer'
 
#-----------------------Asiste--------------------------------#

#-----------------------Cliente--------------------------------#
class ListadoCliente(ListView):
     model = Cliente
    
class ClienteCrear(SuccessMessageMixin, CreateView):
    model = Cliente
    form = Cliente
    fields = "__all__"
    success_message ='Cliente creada correctamente'
     
    def get_success_url(self):        
        return reverse('modulo1:leercliente') # Redireccionamos a la vista principal 'leer'

class ClienteDetalle (DetailView):
    model = Cliente

class ClienteActualizar(SuccessMessageMixin,UpdateView):
    model =  Cliente
    form = Cliente
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Cliente Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('modulo1:leercliente') # Redireccionamos a la vista principal 'leer'
class ClienteEliminar(SuccessMessageMixin, DeleteView): 
    model = Cliente
    form = Cliente
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Cliente Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('modulo1:leercliente') # Redireccionamos a la vista principal 'leer'
 
#-----------------------Cliente--------------------------------#

#-----------------------Reserva--------------------------------#
class ListadoReserva(ListView):
     model = Reserva
    
class ReservaCrear(SuccessMessageMixin, CreateView):
    model = Reserva
    form = Reserva
    fields = "__all__"
    success_message ='Reserva creada correctamente'
     
    def get_success_url(self):        
        return reverse('modulo1:leerReserva') # Redireccionamos a la vista principal 'leer'

class ReservaDetalle (DetailView):
    model = Reserva

class ReservaActualizar(SuccessMessageMixin,UpdateView):
    model =  Reserva
    form = Reserva
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Reserva Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('modulo1:leerReserva') # Redireccionamos a la vista principal 'leer'
class ReservaEliminar(SuccessMessageMixin, DeleteView): 
    model = Reserva
    form = Reserva
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Reserva Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('modulo1:leerReserva') # Redireccionamos a la vista principal 'leer'
 
#-----------------------Reserva--------------------------------#

#-----------------------Telefono--------------------------------#
class ListadoTelefono(ListView):
     model = Telefono
    
class TelefonoCrear(SuccessMessageMixin, CreateView):
    model = Telefono
    form = Telefono
    fields = "__all__"
    success_message ='Telefono creada correctamente'
     
    def get_success_url(self):        
        return reverse('modulo1:leerTelefono') # Redireccionamos a la vista principal 'leer'

class TelefonoDetalle (DetailView):
    model = Telefono

class TelefonoActualizar(SuccessMessageMixin,UpdateView):
    model =  Telefono
    form = Telefono
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Telefono Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('modulo1:leerTelefono') # Redireccionamos a la vista principal 'leer'
class TelefonoEliminar(SuccessMessageMixin, DeleteView): 
    model = Telefono
    form = Telefono
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Telefono Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('modulo1:leerTelefono') # Redireccionamos a la vista principal 'leer'
 
#-----------------------Telefono--------------------------------#

#-----------------------Tipoartista--------------------------------#
class ListadoTipoartista(ListView):
     model = Tipoartista
    
class TipoartistaCrear(SuccessMessageMixin, CreateView):
    model = Tipoartista
    form = Tipoartista
    fields = "__all__"
    success_message ='Tipoartista creada correctamente'
     
    def get_success_url(self):        
        return reverse('modulo1:leerTipoartista') # Redireccionamos a la vista principal 'leer'

class TipoartistaDetalle (DetailView):
    model = Tipoartista

class TipoartistaActualizar(SuccessMessageMixin,UpdateView):
    model =  Tipoartista
    form = Tipoartista
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Tipoartista Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('modulo1:leerTipoartista') # Redireccionamos a la vista principal 'leer'
class TipoartistaEliminar(SuccessMessageMixin, DeleteView): 
    model = Tipoartista
    form = Tipoartista
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Tipoartista Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('modulo1:leerTipoartista') # Redireccionamos a la vista principal 'leer'
 
#-----------------------Tipoartista--------------------------------#

#-----------------------Tipoevento--------------------------------#
class ListadoTipoevento(ListView):
     model = Tipoevento
    
class TipoeventoCrear(SuccessMessageMixin, CreateView):
    model = Tipoevento
    form = Tipoevento
    fields = "__all__"
    success_message ='Tipoevento creada correctamente'
     
    def get_success_url(self):        
        return reverse('modulo1:leerTipoevento') # Redireccionamos a la vista principal 'leer'

class TipoeventoDetalle (DetailView):
    model = Tipoevento

class TipoeventoActualizar(SuccessMessageMixin,UpdateView):
    model =  Tipoevento
    form = Tipoevento
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Tipoevento Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('modulo1:leerTipoevento') # Redireccionamos a la vista principal 'leer'
class TipoeventoEliminar(SuccessMessageMixin, DeleteView): 
    model = Tipoevento
    form = Tipoevento
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Tipoevento Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('modulo1:leerTipoevento') # Redireccionamos a la vista principal 'leer'
 
#-----------------------Tipoevento--------------------------------#

#-----------------------Tipogenero--------------------------------#
class ListadoTipogenero(ListView):
     model = Tipogenero
    
class TipogeneroCrear(SuccessMessageMixin, CreateView):
    model = Tipogenero
    form = Tipogenero
    fields = "__all__"
    success_message ='Tipogenero creada correctamente'
     
    def get_success_url(self):        
        return reverse('modulo1:leerTipogenero') # Redireccionamos a la vista principal 'leer'

class TipogeneroDetalle (DetailView):
    model = Tipogenero

class TipogeneroActualizar(SuccessMessageMixin,UpdateView):
    model =  Tipogenero
    form = Tipogenero
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Tipogenero Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('modulo1:leerTipogenero') # Redireccionamos a la vista principal 'leer'
class TipogeneroEliminar(SuccessMessageMixin, DeleteView): 
    model = Tipogenero
    form = Tipogenero
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Tipogenero Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('modulo1:leerTipogenero') # Redireccionamos a la vista principal 'leer'
 
#-----------------------Tipogenero--------------------------------#

#-----------------------Tipoidentificacion--------------------------------#
class ListadoTipoidentificacion(ListView):
     model = Tipoidentificacion
    
class TipoidentificacionCrear(SuccessMessageMixin, CreateView):
    model = Tipoidentificacion
    form = Tipoidentificacion
    fields = "__all__"
    success_message ='Tipoidentificacion creada correctamente'
     
    def get_success_url(self):        
        return reverse('modulo1:leerTipoidentificacion') # Redireccionamos a la vista principal 'leer'

class TipoidentificacionDetalle (DetailView):
    model = Tipoidentificacion

class TipoidentificacionActualizar(SuccessMessageMixin,UpdateView):
    model =  Tipoidentificacion
    form = Tipoidentificacion
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Tipoidentificacion Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('modulo1:leerTipoidentificacion') # Redireccionamos a la vista principal 'leer'
class TipoidentificacionEliminar(SuccessMessageMixin, DeleteView): 
    model = Tipoidentificacion
    form = Tipoidentificacion
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Tipoidentificacion Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('modulo1:leerTipoidentificacion') # Redireccionamos a la vista principal 'leer'
 
#-----------------------Tipoidentificacion--------------------------------#

#-----------------------Tipotelefono--------------------------------#
class ListadoTipotelefono(ListView):
     model = Tipotelefono
    
class TipotelefonoCrear(SuccessMessageMixin, CreateView):
    model = Tipotelefono
    form = Tipotelefono
    fields = "__all__"
    success_message ='Tipotelefono creada correctamente'
     
    def get_success_url(self):        
        return reverse('modulo1:leerTipotelefono') # Redireccionamos a la vista principal 'leer'

class TipotelefonoDetalle (DetailView):
    model = Tipotelefono

class TipotelefonoActualizar(SuccessMessageMixin,UpdateView):
    model =  Tipotelefono
    form = Tipotelefono
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Tipotelefono Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('modulo1:leerTipotelefono') # Redireccionamos a la vista principal 'leer'
class TipotelefonoEliminar(SuccessMessageMixin, DeleteView): 
    model = Tipotelefono
    form = Tipotelefono
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Tipotelefono Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('modulo1:leerTipotelefono') # Redireccionamos a la vista principal 'leer'
 
#-----------------------Tipotelefono--------------------------------#




















