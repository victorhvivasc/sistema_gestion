# -*- coding: utf-8 -*-
# modelo para registro de pedidos de producción
from peewee import *
import datetime
from produccion.produccion_model import Produccion, Molde, produccion_db


class Cliente(Produccion):
    """Clase que determina la tabla de clientes de la base de datos"""
    razon_social = CharField(max_length=255, verbose_name='Cliente', unique=True, null=False)
    cuit = IntegerField(null=False, unique=True, verbose_name='CUIT')
    telefono = IntegerField(null=False, verbose_name='Teléfono')
    direccion = CharField(max_length=255, null=False, verbose_name='Dirección')

    def __str__(self, ):
        return f"Cliente: {self.razon_social}, CUIT: {self.cuit}, Teléfono: {self.telefono}\n " \
               f"Direccion: {self.direccion}"


class Producto(Produccion):
    """Clase para almacenar la lista de productos disponibles para la venta"""
    codigo = ForeignKeyField(Molde, field=Molde.numero, backref='moldes', verbose_name='codigo')  # Moldes existentes
    # codigo = CharField(max_length=255, verbose_name='Producto', null=False, unique=True)
    nombre = CharField(max_length=255, verbose_name='Nombre del Producto', null=False)
    color = CharField(max_length=255, null=False)
    costo_produccion = IntegerField(default='no disponible', null=False)
    precio_venta = IntegerField(default='no disponible', verbose_name='Precio de Venta')


class Orden(Produccion):
    """Clase para crear tabla de registro de los items solicitados por los clientes"""
    cliente = ForeignKeyField(Cliente, field=Cliente.razon_social, backref='ordenes')  # Clientes existentes
    creado = DateTimeField(null=False)
    actualizado = DateTimeField(default=datetime.datetime.now())
    fecha_compromiso = DateTimeField(null=False, verbose_name='Fecha')
    cantidad_compromiso = IntegerField(null=False, verbose_name='Cantidad')
    producto = ForeignKeyField(Producto, field=Producto.codigo)  # Productos disponibles, indirectamente moldes


produccion_db.create_tables([Cliente, Producto, Orden])
produccion_db.close()
