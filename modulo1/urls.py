"""technohome URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from turtle import home
from django.contrib import admin
from django.urls import path, include
from modulo1.views import*
from .views import registro_usuario


urlpatterns = [
#------------------------------------------registro----------------------------#
  path('registro/', registro_usuario, name='registro_usuario'),
  
  path("vistap/", Index, name="vistap"),
  


 

#------------------------------------------contratos----------------------------#
    path('ccionpermitida/', ListadoAccionpermitida.as_view(template_name = "crud\ccionpermitida\index.html"), name='leerccion'),
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Contratos o registro  
    path('ccionpermitida/crear', AccionpermitidaCrear.as_view(template_name = "crud\Accionpermitida\crear.html"), name='crearccion'),
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Contratos o registro 
    path('ccionpermitida/detalle/<int:pk>',AccionpermitidaDetalle.as_view(template_name = "crud\ccionpermitida\detalle.html"), name='detalleccion'),
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Contratos o registro de la Base de Datos 
    path('ccionpermitida/editar/<int:pk>', AccionpermitidaActualizar.as_view(template_name = "crud\ccionpermitida\eactualizar.html"), name='actualizarccion'), 
    # La ruta 'eliminar' que usaremos para eliminar un Contratos o registro de la Base de Datos 
    path('ccionpermitida/eliminar/<int:pk>', AccionpermitidaEliminar.as_view(), name="crud\ccionpermitida\eliminar.html"),  
    #---------------------------------------eventos---------------------------------------#
    path('Evento/', ListadoEvento.as_view(template_name = "index.html"), name='home'),
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Contratos o registro  
    path('Evento/crear', EventoCrear.as_view(template_name = "crud\Accionpermitida\crear.html"), name='crearccion'),
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Contratos o registro 
    path('Evento/detalle/<int:pk>',EventoDetalle.as_view(template_name = "crud\ccionpermitida\detalle.html"), name='detalleccion'),
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Contratos o registro de la Base de Datos 
    path('Evento/editar/<int:pk>', EventoActualizar.as_view(template_name = "crud\ccionpermitida\eactualizar.html"), name='actualizarccion'), 
    # La ruta 'eliminar' que usaremos para eliminar un Contratos o registro de la Base de Datos 
    path('Evento/eliminar/<int:pk>', EventoEliminar.as_view(), name="crud\ccionpermitida\eliminar.html"),

    #------------------------------------------ccionpermitidaHasPlantilla----------------------------#
    path('ccionpermitidaHasPlantilla/', ListadoAccionpermitidaHasPlantilla.as_view(template_name = "crud\ccionpermitidaHasPlantilla\index.html"), name='leerplan'),
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Contratos o registro  
    path('ccionpermitidaHasPlantilla/crear', AccionpermitidaHasPlantillaCrear.as_view(template_name = "crud\ccionpermitidaHasPlantilla\crear.html"), name='crearplan'),
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Contratos o registro 
    path('ccionpermitidaHasPlantilla/detalle/<int:pk>', AccionpermitidaHasPlantillaDetalle.as_view(template_name = "crud\ccionpermitidaHasPlantilla\detalle.html"), name='detalleplan'),
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Contratos o registro de la Base de Datos 
    path('ccionpermitidaHasPlantilla/editar/<int:pk>', AccionpermitidaHasPlantillaActualizar.as_view(template_name = "crud\ccionpermitidaHasPlantilla\eactualizar.html"), name='actualizarplan'), 
    # La ruta 'eliminar' que usaremos para eliminar un Contratos o registro de la Base de Datos 
    path('ccionpermitidaHasPlantilla/eliminar/<int:pk>', AccionpermitidaHasPlantillaEliminar.as_view(), name="crud\ccionpermitidaHasPlantilla\eliminar.html"),  
    #---------------------------------------ccionpermitidaHasPlantilla---------------------------------------#
    
    #-------------------------------------------AccionpermitidaHasUsuario--------------------------------------------# 
     path('AccionpermitidaHasUsuario/', ListadoAccionpermitidaHasUsuario.as_view(template_name = "crud\ccionpermitidaHasUsuario\index.html"), name='leerplanUsuario'),
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Contratos o registro  
    path('AccionpermitidaHasUsuario/crear',  AccionpermitidaHasUsuarioCrear.as_view(template_name = "crud\ccionpermitidaHasUsuario\crear.html"), name='crearplanUsuario'),
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Contratos o registro 
    path('AccionpermitidaHasUsuario/detalle/<int:pk>', AccionpermitidaHasUsuarioDetalle.as_view(template_name = "crud\ccionpermitidaHasUsuario\detalle.html"), name='detalleplanUsuario'),
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Contratos o registro de la Base de Datos 
    path('AccionpermitidaHasUsuario/editar/<int:pk>', AccionpermitidaHasUsuarioActualizar.as_view(template_name = "crud\ccionpermitidaHasUsuario\eactualizar.html"), name='actualizarplanUsuario'), 
    # La ruta 'eliminar' que usaremos para eliminar un Contratos o registro de la Base de Datos 
    path('AccionpermitidaHasUsuario/eliminar/<int:pk>', AccionpermitidaHasUsuarioEliminar.as_view(), name="crud\ccionpermitidaHasUsuario\eliminar.html"),
    #---------------------------------------AccionpermitidaHasUsuario-------------------------------------------------#

 
    #---------------------------------------Cronograma-------------------------------------------------#
    path('Cronograma/',  ListadoCronograma.as_view(template_name = "crud\cronograma\index.html"), name='leerCronograma'),
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Contratos o registro  
    path('Cronograma/crear', CronogramaCrear.as_view(template_name = "crud\cronograma\crear.html"), name='crearCronograma'),
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Administradors o registro 
    path('Cronograma/detalle/<int:pk>', CronogramaDetalle.as_view(template_name = "crud\cronograma\detalle.html"), name='detalleCronograma'),
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Administradors o registro de la Base de Datos 
    path('Cronograma/editar/<int:pk>', CronogramaActualizar.as_view(template_name = "crud\cronograma\eactualizar.html"), name='actualizarCronograma'), 
    # La ruta 'eliminar' que usaremos para eliminar un Administradors o registro de la Base de Datos 
    path('Cronograma/eliminar/<int:pk>', CronogramaEliminar.as_view(), name="crud\cronograma\eliminar.html"),

    #-----------------------------------Cronograma-------------------------------------------------#

    #------------------Departamento--------------------------------------------------------#
    path('epartamento/',  ListadoDepartamento.as_view(template_name = "crud\epartamento\index.html"), name='leeroti'),
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Contratos o registro  
    path('epartamento/crear', DepartamentoCrear.as_view(template_name = "crud\epartamento\crear.html"), name='crearoti'),
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Notificacioness o registro 
    path('epartamento/detalle/<int:pk>', DepartamentoDetalle.as_view(template_name = "crud\epartamento\detalle.html"), name='detalleoti'),
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Notificacioness o registro de la Base de Datos 
    path('epartamento/editar/<int:pk>', DepartamentoActualizar.as_view(template_name = "crud\epartamento\eactualizar.html"), name='actualizaroti'), 
    # La ruta 'eliminar' que usaremos para eliminar un Notificacioness o registro de la Base de Datos 
    path('epartamento/eliminar/<int:pk>', DepartamentoEliminar.as_view(), name="crud\epartamento\eliminar.html"),
#-------------------------------------Departamento-----------------------------------------------------#

#---------------------------------------Reserva-----------------------------------------------------#
    path('eserva/',  ListadoReserva.as_view(template_name = "crud\eserva\index.html"), name='leereserva'),
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Contratos o registro  
    path('eserva/crear', ReservaCrear.as_view(template_name = "crud\eserva\crear.html"), name='creareserva'),
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Permisoss o registro 
    path('eserva/detalle/<int:pk>', ReservaDetalle.as_view(template_name = "crud\eserva\detalle.html"), name='detalleeserva'),
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Permisoss o registro de la Base de Datos 
    path('eserva/editar/<int:pk>', ReservaActualizar.as_view(template_name = "crud\eserva\eactualizar.html"), name='actualizareserva'), 
    # La ruta 'eliminar' que usaremos para eliminar un Permisoss o registro de la Base de Datos 
    path('eserva/eliminar/<int:pk>', ReservaEliminar.as_view(), name="crud\eserva\eliminar.html"),
#------------------------------------------Reserva----------------------------------------------------#

#-----------------------------------Establecimiento-----------------------------------------------------#
    path('establecimiento/',  ListadoEstablecimiento.as_view(template_name = "crud\establecimiento\index.html"), name='leerestable'),
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Contratos o registro  
    path('establecimiento/crear', EstablecimientoCrear.as_view(template_name = "crud\establecimiento\crear.html"), name='crearestable'),
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Alarmass o registro 
    path('establecimiento/detalle/<int:pk>', EstablecimientoDetalle.as_view(template_name = "crud\establecimiento\detalle.html"), name='detalleestable'),
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Alarmass o registro de la Base de Datos 
    path('establecimiento/editar/<int:pk>', EstablecimientoActualizar.as_view(template_name = "crud\establecimiento\eactualizar.html"), name='actualizarestable'), 
    # La ruta 'eliminar' que usaremos para eliminar un Alarmass o registro de la Base de Datos 
    path('establecimiento/eliminar/<int:pk>', EstablecimientoEliminar.as_view(), name="crud\establecimiento\eliminar.html"),
#-----------------------------------alarmas-----------------------------------------------------#

#---------------------------------------------Establedispo---------------------------------------------#
    path('establedispo/',  ListadoEstabledispo.as_view(template_name = "crud\establedispo\index.html"), name='leerestabledis'),
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Contratos o registro  
    path('establedispo/crear', EstabledispoCrear.as_view(template_name = "crud\establedispo\crear.html"), name='crearestabledis'),
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Reportess o registro 
    path('establedispo/detalle/<int:pk>', EstabledispoDetalle.as_view(template_name = "crud\establedispo\detalle.html"), name='detalleestabledis'),
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Reportess o registro de la Base de Datos 
    path('Establedispo/editar/<int:pk>', EstabledispoActualizar.as_view(template_name = "crud\establedispo\eactualizar.html"), name='actualizarestabledis'), 
    # La ruta 'eliminar' que usaremos para eliminar un Reportess o registro de la Base de Datos 
    path('establedispo/eliminar/<int:pk>', EstabledispoEliminar.as_view(), name="crud\establedispo\eliminar.html"),
#-----------------------------------------Establedispo---------------------------------------------------------#

#---------------------------------------------estado---------------------------------------------#
    path('estado/',  ListadoEstado.as_view(template_name = "crud\estado\index.html"), name='leerestado'),
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Contratos o registro  
    path('estado/crear', EstadoCrear.as_view(template_name = "crud\estado\crear.html"), name='crearestado'),
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Casosemergencias o registro 
    path('estado/detalle/<int:pk>', EstadoDetalle.as_view(template_name = "crud\estado\detalle.html"), name='detalleestado'),
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Casosemergencias o registro de la Base de Datos 
    path('estado/editar/<int:pk>', EstadoActualizar.as_view(template_name = "crud\estado\eactualizar.html"), name='actualizarestado'), 
    # La ruta 'eliminar' que usaremos para eliminar un Casosemergencias o registro de la Base de Datos 
    path('estado/eliminar/<int:pk>', EstadoEliminar.as_view(), name="crud\estado\eliminar.html"),
#-----------------------------------------estado---------------------------------------------------------#

#---------------------------------------------Dispositivos---------------------------------------------#
    path('estadocivil/',  ListadoEstadocivil.as_view(template_name = "crud\estadocivil\index.html"), name='leerestadocivil'),
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Contratos o registro  
    path('estadocivil/crear', EstadocivilCrear.as_view(template_name = "crud\estadocivil\crear.html"), name='crearestadocivil'),
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Estadocivils o registro 
    path('estadocivil/detalle/<int:pk>', EstadocivilDetalle.as_view(template_name = "crud\estadocivil\detalle.html"), name='detalleestadocivil'),
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Estadocivils o registro de la Base de Datos 
    path('estadocivil/editar/<int:pk>', EstadocivilActualizar.as_view(template_name = "crud\estadocivil\eactualizar.html"), name='actualizarestadocivil'), 
    # La ruta 'eliminar' que usaremos para eliminar un Estadocivils o registro de la Base de Datos 
    path('estadocivil/eliminar/<int:pk>', EstadocivilEliminar.as_view(), name="crud\estadocivil\eliminar.html"),
#-----------------------------------------Estadocivil---------------------------------------------------------#


#---------------------------------------------Estagenemusi---------------------------------------------#
    path('estagenemusi/',  ListadoEstagenemusi.as_view(template_name = "crud\estagenemusi\index.html"), name='leerestagenemusi'),
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Contratos o registro  
    path('estagenemusi/crear', EstagenemusiCrear.as_view(template_name = "crud\estagenemusi\crear.html"), name='crearEstagenemusi'),
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Estagenemusis o registro 
    path('estagenemusi/detalle/<int:pk>', EstagenemusiDetalle.as_view(template_name = "crud\estagenemusi\detalle.html"), name='detalleestagenemusi'),
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Estagenemusis o registro de la Base de Datos 
    path('estagenemusi/editar/<int:pk>', EstagenemusiActualizar.as_view(template_name = "crud\estagenemusi\eactualizar.html"), name='actualizarestagenemusi'), 
    # La ruta 'eliminar' que usaremos para eliminar un Estagenemusis o registro de la Base de Datos 
    path('estagenemusi/eliminar/<int:pk>', EstagenemusiEliminar.as_view(), name="crud\estagenemusi\eliminar.html"),
#-----------------------------------------Estagenemusi---------------------------------------------------------#


#---------------------------------------------Estatipgen---------------------------------------------#
    path('estatipgen/',  ListadoEstatipgen.as_view(template_name = "crud\estatipgen\index.html"), name='leerestatipgen'),
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Contratos o registro  
    path('estatipgen/crear', EstatipgenCrear.as_view(template_name = "crud\estatipgen\crear.html"), name='crearestatipgen'),
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Estatipgens o registro 
    path('estatipgen/detalle/<int:pk>', EstatipgenDetalle.as_view(template_name = "crud\estatipgen\detalle.html"), name='detalleestatipgen'),
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Estatipgens o registro de la Base de Datos 
    path('estatipgen/editar/<int:pk>', EstatipgenActualizar.as_view(template_name = "crud\estatipgen\eactualizar.html"), name='actualizarestatipgen'), 
    # La ruta 'eliminar' que usaremos para eliminar un Estatipgens o registro de la Base de Datos 
path('estatipgen/eliminar/<int:pk>', EstatipgenEliminar.as_view(), name="crud\estatipgen\eliminar.html"),
#-----------------------------------------Estatipgen---------------------------------------------------------#

#---------------------------------------------EventoHasArtista---------------------------------------------#
    path('eventoHasArtista/',  ListadoEventoHasArtista.as_view(template_name = "crud\eventoHasArtista\index.html"), name='leereventoHasArtista'),
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Contratos o registro  
    path('eventoHasArtista/crear', EventoHasArtistaCrear.as_view(template_name = "crud\eventoHasArtista\crear.html"), name='creareventoHasArtista'),
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un EventoHasArtistas o registro 
    path('eventoHasArtista/detalle/<int:pk>', EventoHasArtistaDetalle.as_view(template_name = "crud\eventoHasArtista\detalle.html"), name='detalleeventoHasArtista'),
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un EventoHasArtistas o registro de la Base de Datos 
    path('eventoHasArtista/editar/<int:pk>', EventoHasArtistaActualizar.as_view(template_name = "crud\eventoHasArtista\eactualizar.html"), name='actualizareventoHasArtista'), 
    # La ruta 'eliminar' que usaremos para eliminar un EventoHasArtistas o registro de la Base de Datos 
    path('eventoHasArtista/eliminar/<int:pk>', EventoHasArtistaEliminar.as_view(), name="crud\eventoHasArtista\eliminar.html"),
#-----------------------------------------EventoHasArtista---------------------------------------------------------#

#---------------------------------------------Genero---------------------------------------------#
    path('genero/',  ListadoGenero.as_view(template_name = "crud\genero\index.html"), name='leergenero'),
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Contratos o registro  
    path('genero/crear', GeneroCrear.as_view(template_name = "crud\genero\crear.html"), name='creargenero'),
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Generos o registro 
    path('genero/detalle/<int:pk>', GeneroDetalle.as_view(template_name = "crud\genero\detalle.html"), name='detallegenero'),
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Generos o registro de la Base de Datos 
    path('genero/editar/<int:pk>', GeneroActualizar.as_view(template_name = "crud\genero\eactualizar.html"), name='actualizargenero'), 
    # La ruta 'eliminar' que usaremos para eliminar un Genero o registro de la Base de Datos 
    path('genero/eliminar/<int:pk>', GeneroEliminar.as_view(), name="crud\genero\eliminar.html"),
#-----------------------------------------Genero---------------------------------------------------------#

#---------------------------------------------Generomusica---------------------------------------------#
    path('generomusica/',  ListadoGeneromusica.as_view(template_name = "crud\generomusica\index.html"), name='leergeneromusica'),
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Contratos o registro  
    path('generomusica/crear', GeneromusicaCrear.as_view(template_name = "crud\generomusica\crear.html"), name='creargeneromusica'),
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Generomusicas o registro 
    path('generomusica/detalle/<int:pk>', GeneromusicaDetalle.as_view(template_name = "crud\generomusica\detalle.html"), name='detallegeneromusica'),
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Generomusicas o registro de la Base de Datos 
    path('generomusica/editar/<int:pk>', GeneromusicaActualizar.as_view(template_name = "crud\generomusica\eactualizar.html"), name='actualizargeneromusica'), 
    # La ruta 'eliminar' que usaremos para eliminar un Generomusicas o registro de la Base de Datos 
    path('generomusica/eliminar/<int:pk>', GeneromusicaEliminar.as_view(), name="crud\generomusica\eliminar.html"),
#-----------------------------------------Generomusica---------------------------------------------------------#


#---------------------------------------------Municipio---------------------------------------------#
    path('municipio/',  ListadoMunicipio.as_view(template_name = "crud\municipio\index.html"), name='leermunicipio'),
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Contratos o registro  
    path('municipio/crear', MunicipioCrear.as_view(template_name = "crud\municipio\crear.html"), name='crearmunicipio'),
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Municipios o registro 
    path('municipio/detalle/<int:pk>', MunicipioDetalle.as_view(template_name = "crud\municipio\detalle.html"), name='detallemunicipio'),
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Municipio o registro de la Base de Datos 
    path('municipio/editar/<int:pk>', MunicipioActualizar.as_view(template_name = "crud\municipio\eactualizar.html"), name='actualizarmunicipio'), 
    # La ruta 'eliminar' que usaremos para eliminar un Municipios o registro de la Base de Datos 
    path('municipio/eliminar/<int:pk>', MunicipioEliminar.as_view(), name="crud\municipio\eliminar.html"),
#-----------------------------------------Municipio---------------------------------------------------------#

#---------------------------------------------Organizador---------------------------------------------#
    path('organizador/',  ListadoOrganizador.as_view(template_name = "crud\organizador\index.html"), name='leerorganizador'),
    # La Organizador a 'crear' en donde mostraremos un formulario para crear un nuevo Contratos o registro  
    path('organizador/crear', OrganizadorCrear.as_view(template_name = "crud\organizador\crear.html"), name='crearorganizador '),
    # La Organizador a 'detalles' en donde mostraremos una página con los detalles de un Organizadors o registro 
    path('organizador/detalle/<int:pk>', OrganizadorDetalle.as_view(template_name = "crud\organizador\detalle.html"), name='detalleorganizador'),
    # La Organizador a 'actualizar' en donde mostraremos un formulario para actualizar un Organizadors o registro de la Base de Datos 
    path('organizador/editar/<int:pk>', OrganizadorActualizar.as_view(template_name = "crud\organizador\eactualizar.html"), name='actualizarorganizador'), 
    # La Organizador a 'eliminar' que usaremos para eliminar un Organizadors o registro de la Base de Datos 
    path('organizador/eliminar/<int:pk>', OrganizadorEliminar.as_view(), name="crud\organizador\eliminar.html"),
#-----------------------------------------Organizador---------------------------------------------------------#

#---------------------------------------------Pais---------------------------------------------#
    path('pais/',  ListadoPais.as_view(template_name = "crud\pais\index.html"), name='leerpais'),
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Contratos o registro  
    path('pais/crear', PaisCrear.as_view(template_name = "crud\pais\crear.html"), name='crearpais'),
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Paiss o registro 
    path('pais/detalle/<int:pk>', PaisDetalle.as_view(template_name = "crud\pais\detalle.html"), name='detallepais'),
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Paiss o registro de la Base de Datos 
    path('pais/editar/<int:pk>', PaisActualizar.as_view(template_name = "crud\pais\eactualizar.html"), name='actualizarpais'), 
    # La ruta 'eliminar' que usaremos para eliminar un Paiss o registro de la Base de Datos 
    path('pais/eliminar/<int:pk>', PaisEliminar.as_view(), name="crud\pais\eliminar.html"),
#-----------------------------------------Pais---------------------------------------------------------#


#---------------------------------------------Persona---------------------------------------------#
    path('persona/',  ListadoPersona.as_view(template_name = "crud\persona\index.html"), name='leerpersona'),
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Contratos o Persona  
    path('persona/crear', PersonaCrear.as_view(template_name = "crud\persona\crear.html"), name='crear'),
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Personas o Persona 
    path('persona/detalle/<int:pk>', PersonaDetalle.as_view(template_name = "crud\persona\detalle.html"), name='detallepersona'),
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Personas o Persona de la Base de Datos 
    path('persona/editar/<int:pk>', PersonaActualizar.as_view(template_name = "crud\persona\eactualizar.html"), name='actualizarpersona'), 
    # La ruta 'eliminar' que usaremos para eliminar un Personas o Persona de la Base de Datos 
    path('persona/eliminar/<int:pk>', PersonaEliminar.as_view(), name="crud\persona\eliminar.html"),
#-----------------------------------------Persona---------------------------------------------------------#

#---------------------------------------------Plantilla---------------------------------------------#
    path('plantilla/',  ListadoPlantilla.as_view(template_name = "crud\plantilla\index.html"), name='leerplantilla'),
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Contratos o registro  
    path('plantilla/crear', PlantillaCrear.as_view(template_name = "crud\plantilla\crear.html"), name='crearplantilla'),
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Plantillas o registro 
    path('plantilla/detalle/<int:pk>', PlantillaDetalle.as_view(template_name = "crud\plantilla\detalle.html"), name='detalleplantilla'),
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Plantillas o registro de la Base de Datos 
    path('plantilla/editar/<int:pk>', PlantillaActualizar.as_view(template_name = "crud\plantilla\eactualizar.html"), name='actualizarplantilla'), 
    # La ruta 'eliminar' que usaremos para eliminar un Plantillas o registro de la Base de Datos 
    path('plantilla/eliminar/<int:pk>', PlantillaEliminar.as_view(), name="crud\plantilla\eliminar.html"),
#-----------------------------------------Plantilla---------------------------------------------------------#


#---------------------------------------------Artista---------------------------------------------#
    path('Artista/',  ListadoArtista.as_view(template_name = "crud\Artista\index.html"), name='leerArtista'),
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Contratos o registro  
    path('Artista/crear', ArtistaCrear.as_view(template_name = "crud\Artista\crear.html"), name='crearArtista'),
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Artistas o registro 
    path('Artista/detalle/<int:pk>', ArtistaDetalle.as_view(template_name = "crud\Artista\detalle.html"), name='detallerArtista'),
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Artistas o registro de la Base de Datos 
    path('Artista/editar/<int:pk>', ArtistaActualizar.as_view(template_name = "crud\Artista\eactualizar.html"), name='actualizarArtista'), 
    # La ruta 'eliminar' que usaremos para eliminar un Artistas o registro de la Base de Datos 
    path('Artista/eliminar/<int:pk>', ArtistaEliminar.as_view(), name="crud\Artista\eliminar.html"),
#-----------------------------------------Artista---------------------------------------------------------#

#---------------------------------------------Asiste---------------------------------------------#
    path('Asiste/',  ListadoAsiste.as_view(template_name = "crud\Asiste\index.html"), name='leerAsiste'),
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Contratos o registro  
    path('Asiste/crear', AsisteCrear.as_view(template_name = "crud\Asiste\crear.html"), name='crearAsiste'),
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Asistes o registro 
    path('Asiste/detalle/<int:pk>', AsisteDetalle.as_view(template_name = "crud\Asiste\detalle.html"), name='detalleAsiste'),
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Asistes o registro de la Base de Datos 
    path('Asiste/editar/<int:pk>', AsisteActualizar.as_view(template_name = "crud\Asiste\eactualizar.html"), name='actualizarAsiste'), 
    # La ruta 'eliminar' que usaremos para eliminar un Asistes o registro de la Base de Datos 
    path('Asiste/eliminar/<int:pk>', AsisteEliminar.as_view(), name="crud\Asiste\eliminar.html"),
#-----------------------------------------Asiste---------------------------------------------------------#

#---------------------------------------------Cliente---------------------------------------------#
    path('cliente/',  ListadoCliente.as_view(template_name = "crud\cliente\index.html"), name='leercliente'),
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Contratos o registro  
    path('cliente/crear', ClienteCrear.as_view(template_name = "crud\cliente\crear.html"), name='crearcliente'),
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Clientes o registro 
    path('cliente/detalle/<int:pk>', ClienteDetalle.as_view(template_name = "crud\liente\detalle.html"), name='detallecliente'),
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Clientes o registro de la Base de Datos 
    path('Cliente/editar/<int:pk>', ClienteActualizar.as_view(template_name = "crud\cliente\eactualizar.html"), name='actualizarcliente'), 
    # La ruta 'eliminar' que usaremos para eliminar un Clientes o registro de la Base de Datos 
    path('cliente/eliminar/<int:pk>', ClienteEliminar.as_view(), name="crud\cliente\eliminar.html"),
#-----------------------------------------Cliente---------------------------------------------------------#

#---------------------------------------------Reserva---------------------------------------------#
    path('eserva/',  ListadoReserva.as_view(template_name = "crud\eserva\index.html"), name='leereserva'),
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Contratos o registro  
    path('eserva/crear', ReservaCrear.as_view(template_name = "crud\eserva\crear.html"), name='creareserva'),
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Reservas o registro 
    path('eserva/detalle/<int:pk>', ReservaDetalle.as_view(template_name = "crud\eserva\detalle.html"), name='detalleeserva'),
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Reservas o registro de la Base de Datos 
    path('Reserva/editar/<int:pk>', ReservaActualizar.as_view(template_name = "crud\eserva\eactualizar.html"), name='actualizareserva'), 
    # La ruta 'eliminar' que usaremos para eliminar un Reservas o registro de la Base de Datos 
    path('eserva/eliminar/<int:pk>', ReservaEliminar.as_view(), name="crud\eserva\eliminar.html"),
#-----------------------------------------Reserva---------------------------------------------------------#  

#---------------------------------------------Telefono---------------------------------------------#
    path('Telefono/',  ListadoTelefono.as_view(template_name = "crud\Telefono\index.html"), name='leerTelefono'),
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Contratos o registro  
    path('Telefono/crear', TelefonoCrear.as_view(template_name = "crud\Telefono\crear.html"), name='crearTelefono'),
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Telefonos o registro 
    path('Telefono/detalle/<int:pk>', TelefonoDetalle.as_view(template_name = "crud\Telefono\detalle.html"), name='detalleTelefono'),
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Telefonos o registro de la Base de Datos 
    path('Telefono/editar/<int:pk>', TelefonoActualizar.as_view(template_name = "crud\Telefono\eactualizar.html"), name='actualizarTelefono'), 
    # La ruta 'eliminar' que usaremos para eliminar un Telefonos o registro de la Base de Datos 
    path('Telefono/eliminar/<int:pk>', TelefonoEliminar.as_view(), name="crud\Telefono\eliminar.html"),
#-----------------------------------------Telefono---------------------------------------------------------# 

# #---------------------------------------------Tipoartista---------------------------------------------#
    path('Tipoartista/',  ListadoTipoartista.as_view(template_name = "crud\Tipoartista\index.html"), name='leerTipoartista'),
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Contratos o registro  
    path('Tipoartista/crear', TipoartistaCrear.as_view(template_name = "crud\Tipoartista\crear.html"), name='crearTipoartista'),
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Tipoartistas o registro 
    path('Tipoartista/detalle/<int:pk>', TipoartistaDetalle.as_view(template_name = "crud\Tipoartista\detalle.html"), name='detalleTipoartista'),
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Tipoartistas o registro de la Base de Datos 
    path('Tipoartista/editar/<int:pk>', TipoartistaActualizar.as_view(template_name = "crud\Tipoartista\eactualizar.html"), name='actualizarTipoartista'), 
    # La ruta 'eliminar' que usaremos para eliminar un Tipoartistas o registro de la Base de Datos 
    path('Tipoartista/eliminar/<int:pk>', TipoartistaEliminar.as_view(), name="crud\Tipoartista\eliminar.html"),
#-----------------------------------------Tipoartista---------------------------------------------------------# 

# #---------------------------------------------Tipoevento---------------------------------------------#
    path('Tipoevento/',  ListadoTipoevento.as_view(template_name = "crud\Tipoevento\index.html"), name='leerTipoevento'),
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Contratos o registro  
    path('Tipoevento/crear', TipoeventoCrear.as_view(template_name = "crud\Tipoevento\crear.html"), name='crearTipoevento'),
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Tipoeventos o registro 
    path('Tipoevento/detalle/<int:pk>', TipoeventoDetalle.as_view(template_name = "crud\Tipoevento\detalle.html"), name='detalleTipoevento'),
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Tipoeventos o registro de la Base de Datos 
    path('Tipoevento/editar/<int:pk>', TipoeventoActualizar.as_view(template_name = "crud\Tipoevento\eactualizar.html"), name='actualizarTipoevento'), 
    # La ruta 'eliminar' que usaremos para eliminar un Tipoeventos o registro de la Base de Datos 
    path('Tipoevento/eliminar/<int:pk>', TipoeventoEliminar.as_view(), name="crud\Tipoevento\eliminar.html"),
#-----------------------------------------Tipoevento---------------------------------------------------------# 

# #---------------------------------------------Tipogenero---------------------------------------------#
    path('Tipogenero/',  ListadoTipogenero.as_view(template_name = "crud\Tipogenero\index.html"), name='leerTipogenero'),
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Contratos o registro  
    path('Tipogenero/crear', TipogeneroCrear.as_view(template_name = "crud\Tipogenero\crear.html"), name='crearTipogenero'),
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Tipogeneros o registro 
    path('Tipogenero/detalle/<int:pk>', TipogeneroDetalle.as_view(template_name = "crud\Tipogenero\detalle.html"), name='detalleTipogenero'),
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Tipogeneros o registro de la Base de Datos 
    path('Tipogenero/editar/<int:pk>', TipogeneroActualizar.as_view(template_name = "crud\Tipogenero\eactualizar.html"), name='actualizarTipogenero'), 
    # La ruta 'eliminar' que usaremos para eliminar un Tipogeneros o registro de la Base de Datos 
    path('Tipogenero/eliminar/<int:pk>', TipogeneroEliminar.as_view(), name="crud\Tipogenero\eliminar.html"),
#-----------------------------------------Tipogenero---------------------------------------------------------# 

# #---------------------------------------------Tipoidentificacion---------------------------------------------#
    path('Tipoidentificacion/',  ListadoTipoidentificacion.as_view(template_name = "crud\Tipoidentificacion\index.html"), name='leerTipoidentificacion'),
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Contratos o registro  
    path('Tipoidentificacion/crear', TipoidentificacionCrear.as_view(template_name = "crud\Tipoidentificacion\crear.html"), name='crearTipoidentificacion'),
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Tipoidentificacions o registro 
    path('Tipoidentificacion/detalle/<int:pk>', TipoidentificacionDetalle.as_view(template_name = "crud\Tipoidentificacion\detalle.html"), name='detalleTipoidentificacion'),
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Tipoidentificacions o registro de la Base de Datos 
    path('Tipoidentificacion/editar/<int:pk>', TipoidentificacionActualizar.as_view(template_name = "crud\Tipoidentificacion\eactualizar.html"), name='actualizarTipoidentificacion'), 
    # La ruta 'eliminar' que usaremos para eliminar un Tipoidentificacions o registro de la Base de Datos 
    path('Tipoidentificacion/eliminar/<int:pk>', TipoidentificacionEliminar.as_view(), name="crud\Tipoidentificacion\eliminar.html"),
#-----------------------------------------Tipoidentificacion---------------------------------------------------------# 

# #---------------------------------------------Tipotelefono---------------------------------------------#
    path('Tipotelefono/',  ListadoTipotelefono.as_view(template_name = "crud\Tipotelefono\index.html"), name='leerTipotelefono'),
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Contratos o registro  
    path('Tipotelefono/crear', TipotelefonoCrear.as_view(template_name = "crud\Tipotelefono\crear.html"), name='crearTipotelefono'),
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Tipotelefonos o registro 
    path('Tipotelefono/detalle/<int:pk>', TipotelefonoDetalle.as_view(template_name = "crud\Tipotelefono\detalle.html"), name='detalleTipotelefono'),
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Tipotelefonos o registro de la Base de Datos 
    path('Tipotelefono/editar/<int:pk>', TipotelefonoActualizar.as_view(template_name = "crud\Tipotelefono\eactualizar.html"), name='actualizarTipotelefono'), 
    # La ruta 'eliminar' que usaremos para eliminar un Tipotelefonos o registro de la Base de Datos 
    path('Tipotelefono/eliminar/<int:pk>', TipotelefonoEliminar.as_view(), name="crud\Tipotelefono\eliminar.html"),
#-----------------------------------------Tipotelefono---------------------------------------------------------# 


 



]    

