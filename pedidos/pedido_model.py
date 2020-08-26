# -*- coding: utf-8 -*-
# modelo para registro de pedidos de producción
from peewee import *
import datetime
from produccion.produccion_model import Molde

pedido_db = SqliteDatabase('../pedido.db')


class Pedido(Model):

    class Meta:
        database = pedido_db


class Cliente(Pedido):
    """Clase que determina la tabla de clientes de la base de datos"""
    razon_social = CharField(max_length=255, verbose_name='Cliente', unique=True, null=False)
    cuit = IntegerField(null=False, unique=True, verbose_name='CUIT')
    telefono = IntegerField(null=False, verbose_name='Teléfono')
    direccion = CharField(max_length=255, null=False, verbose_name='Dirección')

    def __str__(self, ):
        return f"Cliente: {self.razon_social}, CUIT: {self.cuit}, Teléfono: {self.telefono}\n " \
               f"Direccion: {self.direccion}"


class Producto(Pedido):
    """Clase para almacenar la lista de productos disponibles para la venta"""
    codigo = ForeignKeyField(Molde, field=Molde.numero, verbose_name='codigo')
    # codigo = CharField(max_length=255, verbose_name='Producto', null=False, unique=True)
    nombre = CharField(max_length=255, verbose_name='Nombre del Producto', null=False)
    color = CharField(max_length=255, null=False)
    costo_produccion = IntegerField(default='no disponible', null=False)
    precio_venta = IntegerField(default='no disponible', verbose_name='Precio de Venta')


class Orden(Pedido):
    """Clase para crear tabla de registro de los items solicitados por los clientes"""
    cliente = ForeignKeyField(Cliente, field=Cliente.razon_social, backref='ordenes')
    creado = DateTimeField(default=datetime.datetime.now())
    compromiso = DateTimeField(null=False)
    producto = ForeignKeyField(Producto, field=Producto.codigo)


pedido_db.connect()
pedido_db.create_tables([Cliente, Producto, Orden])
