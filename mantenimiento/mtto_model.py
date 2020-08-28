# -*- coding: utf-8 -*-
# modelo para gestion de mantenimiento
from peewee import *
from produccion.produccion_model import Produccion, Maquina, Molde, produccion_db


class Mantenimiento(Produccion):
    maquina = ForeignKeyField(Maquina, field=Maquina.numero, backref='mantenimientos')
    fecha_i = DateTimeField(null=False, help_text='Indicar fecha y hora inicial')
    fecha_f = DateTimeField(null=False, help_text='Indicar fecha y hora final')
    correctivo = BooleanField(default=True, null=False)
    planificado = BooleanField(default=False, null=False)
    en_produccion = BooleanField(default=False, null=True)
    producto = ForeignKeyField(Molde, field=Molde.numero, backref='mantenimiento',
                               help_text='Producto que se encontraba en produccion')
    personal = IntegerField(null=False)
    repuestos = BlobField(null=False)


class Repuesto(Produccion):
    codigo_interno = CharField(max_length=255, null=False)
    codigo_fabrica = CharField(max_length=255, null=False)
    descripcion = CharField(max_length=255, null=False)
    maquina = ForeignKeyField(Maquina, field=Maquina.numero, null=True, backref='Repuestos')
    cantidad = IntegerField(null=False)
    precio = IntegerField(null=True)
    fecha_ingreso = DateTimeField(null=False)
    proveedor = CharField(null=False, help_text='Recomiendo usar numero de identificacion')


class PersonalMtto(Produccion):
    legajo = CharField(max_length=255, null=False, verbose_name='codigo_empleado')
    nombre = CharField(max_length=255, null=False, verbose_name='Nombre y Apellido')
    especialidad = CharField(max_length=255, null=False)
    ano_ingreso = IntegerField(null=False)
    anos_experiencia = IntegerField(null=False)


produccion_db.create_tables([Mantenimiento, Repuesto, PersonalMtto])
#produccion_db.close()
