# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Accionpermitida(models.Model):
    pkaccionpermitida = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=500)
    ruta = models.CharField(max_length=500)
    accionpermitida_pkaccionpermitida = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'accionpermitida'
        unique_together = (('pkaccionpermitida', 'accionpermitida_pkaccionpermitida'),)


class AccionpermitidaHasPlantilla(models.Model):
    accionpermitida_pkaccionpermitida = models.IntegerField(primary_key=True)
    plantilla_pkplantilla = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'accionpermitida_has_plantilla'
        unique_together = (('accionpermitida_pkaccionpermitida', 'plantilla_pkplantilla'),)


class AccionpermitidaHasUsuario(models.Model):
    accionpermitida_pkaccionpermitida = models.IntegerField(primary_key=True)
    accionpermitida_accionpermitida_pkaccionpermitida = models.IntegerField()
    usuario_pkusuario = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'accionpermitida_has_usuario'
        unique_together = (('accionpermitida_pkaccionpermitida', 'accionpermitida_accionpermitida_pkaccionpermitida', 'usuario_pkusuario'),)


class Artista(models.Model):
    pkartista = models.AutoField(primary_key=True)
    nombreartistico = models.CharField(max_length=100)
    generomusical = models.CharField(max_length=100)
    trayectoriaartistica = models.CharField(max_length=100)
    usuario_pkusuario = models.IntegerField()
    tipoartista_pktipoartista = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'artista'
        unique_together = (('pkartista', 'usuario_pkusuario', 'tipoartista_pktipoartista'),)


class Asiste(models.Model):
    cliente_pkcliente = models.IntegerField(primary_key=True)
    evento_pkevento = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'asiste'
        unique_together = (('cliente_pkcliente', 'evento_pkevento'),)


class Cliente(models.Model):
    pkcliente = models.AutoField(primary_key=True)
    usuario_pkusuario = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cliente'
        unique_together = (('pkcliente', 'usuario_pkusuario'),)


class Cronograma(models.Model):
    ipkcronograma = models.AutoField(primary_key=True)
    hora = models.DateTimeField()
    descripcion = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'cronograma'


class Departamento(models.Model):
    pkdepartamento = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=45)
    nombre = models.CharField(max_length=45)
    pais_pkpais = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'departamento'
        unique_together = (('pkdepartamento', 'pais_pkpais'),)


class Disponibilidad(models.Model):
    pkdisponibilidad = models.AutoField(primary_key=True)
    horario = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'disponibilidad'


class Establecimiento(models.Model):
    pkestablecimiento = models.AutoField(primary_key=True)
    fkduenio = models.IntegerField()
    fkmunlugar = models.IntegerField()
    direccion = models.CharField(max_length=45)
    nombre = models.CharField(max_length=45)
    nit = models.CharField(max_length=45)
    capacidad = models.IntegerField()
    precio = models.IntegerField()
    organizador_pkduenio = models.IntegerField()
    organizador_usuario_pkusuario = models.IntegerField()
    municipio_pkmunicipio = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'establecimiento'
        unique_together = (('pkestablecimiento', 'organizador_pkduenio', 'organizador_usuario_pkusuario', 'municipio_pkmunicipio'),)


class Establedispo(models.Model):
    pkestabledispo = models.AutoField(primary_key=True)
    disponibilidad_pkdisponibilidad = models.IntegerField()
    establecimiento_pkestablecimiento = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'establedispo'
        unique_together = (('pkestabledispo', 'disponibilidad_pkdisponibilidad', 'establecimiento_pkestablecimiento'),)


class Estado(models.Model):
    pkestado = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'estado'


class Estadocivil(models.Model):
    pkestadocivil = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estadocivil'


class Estagenemusi(models.Model):
    pkestagenemusi = models.AutoField(primary_key=True)
    generomusica_pkgeneromusica = models.IntegerField()
    establecimiento_pkestablecimiento = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'estagenemusi'
        unique_together = (('pkestagenemusi', 'generomusica_pkgeneromusica', 'establecimiento_pkestablecimiento'),)


class Estatipgen(models.Model):
    pkestatipgen = models.AutoField(primary_key=True)
    tipogenero_pktipogenero = models.IntegerField()
    establecimiento_pkestablecimiento = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'estatipgen'
        unique_together = (('pkestatipgen', 'tipogenero_pktipogenero', 'establecimiento_pkestablecimiento'),)


class Evento(models.Model):
    pkevento = models.AutoField(primary_key=True)
    fecha = models.DateField()
    descripcion = models.CharField(max_length=100)
    capacidad = models.IntegerField()
    precio = models.IntegerField()
    tipoevento_pktipoevento = models.IntegerField()
    establecimiento_pkestablecimiento = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'evento'
        unique_together = (('pkevento', 'tipoevento_pktipoevento', 'establecimiento_pkestablecimiento'),)


class EventoHasArtista(models.Model):
    evento_pkevento = models.IntegerField(primary_key=True)
    artista_pkartista = models.IntegerField()
    artista_usuario_pkusuario = models.IntegerField()
    artista_tipoartista_pktipoartista = models.IntegerField()
    cronograma_ipkcronograma = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'evento_has_artista'
        unique_together = (('evento_pkevento', 'artista_pkartista', 'artista_usuario_pkusuario', 'artista_tipoartista_pktipoartista', 'cronograma_ipkcronograma'),)


class Genero(models.Model):
    pkgenero = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'genero'


class Generomusica(models.Model):
    pkgeneromusica = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'generomusica'


class Municipio(models.Model):
    pkmunicipio = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=20)
    nombre = models.CharField(max_length=100)
    departamento_pkdepartamento = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'municipio'
        unique_together = (('pkmunicipio', 'departamento_pkdepartamento'),)


class Organizador(models.Model):
    pkduenio = models.AutoField(primary_key=True)
    fkusuario = models.IntegerField()
    usuario_pkusuario = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'organizador'
        unique_together = (('pkduenio', 'usuario_pkusuario'),)


class Pais(models.Model):
    pkpais = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=45)
    nombre = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'pais'


class Persona(models.Model):
    pkpersona = models.AutoField(primary_key=True)
    identificacion = models.CharField(max_length=200)
    nombre = models.CharField(max_length=500)
    apellido = models.CharField(max_length=500)
    email = models.CharField(max_length=100)
    fechanacimiento = models.DateField()
    estadocivil_pkestadocivil = models.IntegerField()
    genero_pkgenero = models.IntegerField()
    tipoidentificacion_pktipoidentifi = models.IntegerField()
    municipio_pkmunicipio = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'persona'
        unique_together = (('pkpersona', 'estadocivil_pkestadocivil', 'genero_pkgenero', 'tipoidentificacion_pktipoidentifi', 'municipio_pkmunicipio'),)


class Plantilla(models.Model):
    pkplantilla = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'plantilla'


class Reserva(models.Model):
    pkreserva = models.AutoField(primary_key=True)
    hora = models.DateField()
    cantipersonas = models.IntegerField()
    cliente_pkcliente = models.IntegerField()
    evento_pkevento = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'reserva'
        unique_together = (('pkreserva', 'cliente_pkcliente', 'evento_pkevento'),)


class Telefono(models.Model):
    pktelefono = models.AutoField(primary_key=True)
    numero = models.IntegerField()
    tipotelefono_pktipotelefono = models.IntegerField()
    persona_pkpersona = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'telefono'
        unique_together = (('pktelefono', 'tipotelefono_pktipotelefono', 'persona_pkpersona'),)


class Tipoartista(models.Model):
    pktipoartista = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'tipoartista'


class Tipoevento(models.Model):
    pktipoevento = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'tipoevento'


class Tipogenero(models.Model):
    pktipogenero = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'tipogenero'


class Tipoidentificacion(models.Model):
    pktipoidentifi = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'tipoidentificacion'


class Tipotelefono(models.Model):
    pktipotelefono = models.IntegerField(primary_key=True)
    codigo = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'tipotelefono'


class Usuario(models.Model):
    pkusuario = models.AutoField(primary_key=True)
    nombreusuario = models.CharField(max_length=200)
    contrasenia = models.CharField(max_length=200)
    tipousuarioenum = models.IntegerField()
    ultimoacceso = models.DateField()
    codactivacion = models.CharField(max_length=45)
    persona_pkpersona = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'usuario'
        unique_together = (('pkusuario', 'persona_pkpersona'),)


class UsuarioHasEstado(models.Model):
    usuario_pkusuario = models.IntegerField(primary_key=True)
    usuario_persona_pkpersona = models.IntegerField()
    estado_pkestado = models.IntegerField()
    fechainicio = models.DateTimeField()
    fechafin = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'usuario_has_estado'
        unique_together = (('usuario_pkusuario', 'usuario_persona_pkpersona', 'estado_pkestado'),)
