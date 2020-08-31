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

    def __str__(self, ):
        return f"Maquina #: {self.maquina}, tiene/tuvo mantenimiento desde {self.fecha_i} hasta {self.fecha_f};" \
               f"¿Correctivo? {self.correctivo}, ¿Planificado? {self.planificado}, ¿Estaba en producción el equipo?" \
               f"{self.en_produccion}, ¿con que producto? {self.producto}, ¿Quien se encarga de la actividad? " \
               f"{self.personal}, ¿Que repuestos estan implicados en el mantenimiento? {self.repuestos}"


class Repuesto(Produccion):
    codigo_interno = CharField(max_length=255, null=False)
    codigo_fabrica = CharField(max_length=255, null=False)
    descripcion = CharField(max_length=255, null=False)
    maquina = ForeignKeyField(Maquina, field=Maquina.numero, null=True, backref='Repuestos')
    cantidad = IntegerField(null=False)
    precio = IntegerField(null=True)
    fecha_ingreso = DateTimeField(null=False)
    proveedor = CharField(null=False, help_text='Recomiendo usar numero de identificacion')

    def __str__(self, ):
        return f"Repuesto: {self.descripcion}, modelo: {self.codigo_fabrica}, registrado con # " \
               f"{self.codigo_interno}, cantidad: {self.cantidad}, maquina asignada a la compra: {self.maquina}"


class PersonalMtto(Produccion):
    legajo = CharField(max_length=255, null=False, verbose_name='codigo_empleado')
    nombre = CharField(max_length=255, null=False, verbose_name='Nombre y Apellido')
    especialidad = CharField(max_length=255, null=False)
    ano_ingreso = IntegerField(null=False)
    anos_experiencia = IntegerField(null=False)

    def __str__(self, ):
        return f"Empleado # {self.legajo}, Nombre: {self.nombre}, Especialidad: {self.especialidad}"


produccion_db.create_tables([Mantenimiento, Repuesto, PersonalMtto])
produccion_db.close()
