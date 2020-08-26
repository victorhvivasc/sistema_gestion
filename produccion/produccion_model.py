# -*- coding: utf-8 -*-
# modelo para hacer seguimiento del avance de la produccion
from peewee import *

produccion_db = SqliteDatabase('../produccion.db')


class Produccion(Model):

    class Meta:
        database = produccion_db


class Maquina(Produccion):
    verbose_name = 'Maquinas'
    numero = IntegerField(unique=True, null=False, verbose_name='Numero de Maquina')
    tipo = CharField(max_length=255, null=False)
    modelo = CharField(max_length=255, null=False)
    fabricante = CharField(max_length=255)
    ano = IntegerField(null=False)
    capacidad = IntegerField(null=False, default='Ejemplo 250 toneladas', verbose_name='Capacidad')
    planta = CharField(max_length=255, null=False)
    disponible = BooleanField(default=True, verbose_name='Operativa')
    mantenimiento = BooleanField(default=False, help_text='False indica que no requiere mantenimiento')


class Molde(Produccion):
    verbose_name = 'Moldes'
    numero = CharField(max_length=255, unique=True)
    nombre = CharField(max_length=255, verbose_name='Nombre del Producto')
    fabricante = CharField(max_length=255, null=False)
    noyo = BooleanField(default=False, help_text='False indica que no usa noyos')
    mantenimiento = BooleanField(default=False, help_text='False indica que no requiere mantenimiento')
    disponible = BooleanField(default=True)
    colada_caliente = BooleanField(default=True)
    n_cavidades = IntegerField(null=False)
    cavidades_disponibles = IntegerField(null=False)
    alto = IntegerField(null=False)
    ancho = IntegerField(null=False)
    profundo = IntegerField(null=False)
    horas_en_produccion = IntegerField(default=0)
    ultimo_ciclo = IntegerField(null=False)
    materia_prima = CharField(max_length=255, null=False)


class Planificacion(Produccion):
    verbose_name = 'Planificaciones'
    codigo = AutoField(verbose_name='Orden de Produccion')
    fecha_montaje = DateTimeField(null=False, verbose_name='Cambio de molde')
    fecha_inicio = DateTimeField(null=False, verbose_name='Arranque de produccion')
    piezas = IntegerField(null=False)
    molde = ForeignKeyField(Molde, field=Molde.numero, backref='Planificaciones', verbose_name='Molde')
    mantenimiento_molde = BooleanField(default=True, help_text='True indica que va a mantenimiento '
                                                               'al final de produccion')
    maquina = ForeignKeyField(Maquina, field=Maquina.numero, backref='Planificaciones', verbose_name='Maquina')
    mantenimiento_maq = BooleanField(default=False, help_text='True indica que va a mantenimiento '
                                                              'al final de produccion')
    prioridad = IntegerField(null=False)
    fecha_fin = DateTimeField(null=False, verbose_name='Fin de produccion estimado')


produccion_db.connect()
produccion_db.create_tables([Maquina, Molde, Planificacion])