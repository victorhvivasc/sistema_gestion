# -*- coding: utf-8 -*-
# modelo para hacer seguimiento del avance de la produccion
from peewee import *

produccion_db = SqliteDatabase('./produccion.db')


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

    #def __str__(self, ):
    #    return f"Maquina numero: {self.numero}, marca: {self.fabricante}, capacidad: {self.capacidad}, " \
    #           f"¿Disponible?: {self.disponible}, ¿Requiere mantenimiento?: {self.mantenimiento}"


class MateriaPrima(Produccion):
    verbose_name = 'Materia Prima'
    codigo_interno = CharField(max_length=255, null=False)
    codigo_prov = CharField(max_length=255, null=False)
    tipo = CharField(max_length=255, null=False)
    origen = CharField(max_length=255, null=False)
    disponible = BooleanField(default=False)
    proveedor = CharField(max_length=255, null=False)
    reciclado = BooleanField(default=False)
    ubicacion = CharField(max_length=255, null=False)
    cantidad = FloatField(default=0, help_text='Cargar peso en kilogramos')

    def __str__(self, ):
        return f"Objeto {self.verbose_name}, codigo interno: {self.codigo_interno}, " \
               f"cantidad: {self.cantidad}, ¿Disponible?: {self.disponible}"


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
    alto = FloatField(null=False)
    ancho = FloatField(null=False)
    profundo = FloatField(null=False)
    horas_en_produccion = IntegerField(default=0)
    ultimo_ciclo = FloatField(null=False)
    materia_prima = CharField(max_length=255, null=False)
    peso_molde = IntegerField(null=False, help_text='Peso en Kilogramos')
    peso_pieza = IntegerField(null=False, help_text='Peso en gramos')

    def __str__(self, ):
        return f"Nombre: {self.nombre}, " \
               f"Codigo: {self.numero}, Materia Prima: {self.materia_prima}"


class Periferico(Produccion):
    verbose_name = 'Perifericos'
    codigo = CharField(max_length=255, unique=True)
    nombre = CharField(max_length=255, null=False)
    modelo = CharField(max_length=255, null=False)
    marca = CharField(max_length=255, null=False)
    operativo = BooleanField(default=True)
    mantenimiento = BooleanField(default=False, help_text='True indica que requiere mantenimiento')

    def __str__(self, ):
        return f"Periferico: {self.codigo}, {self.nombre}, {self.marca}.  ¿Esta operativo?: {self.operativo}"


class Planificacion(Produccion):
    verbose_name = 'Planificaciones'
    codigo = AutoField(verbose_name='Orden de Produccion')
    prioridad = IntegerField(null=False)
    fecha_montaje = DateTimeField(null=False, verbose_name='Cambio de molde')
    fecha_inicio = DateTimeField(null=False, verbose_name='Arranque de produccion')
    piezas = IntegerField(null=False)
    molde = ForeignKeyField(Molde, field=Molde.numero, backref='Planificaciones', verbose_name='Molde')
    mantenimiento_molde = BooleanField(default=True, help_text='True indica que va a mantenimiento '
                                                               'al final de produccion')
    maquina = ForeignKeyField(Maquina, field=Maquina.numero, backref='Planificaciones', verbose_name='Maquina')
    mantenimiento_maq = BooleanField(default=False, help_text='True indica que va a mantenimiento '
                                                              'al final de produccion')
    material1 = CharField(default='No indicado', max_length=255, null=False)
    material2 = CharField(default='No indicado', max_length=255, null=False)
    material3 = CharField(default='No indicado', max_length=255, null=False)
    pm1 = FloatField(default='No indicado', null=False)
    pm2 = FloatField(default='No indicado', null=False)
    pm3 = FloatField(default='No indicado', null=False)
    color = CharField(default='No indicado', max_length=255, null=False)
    porc_color = FloatField(default='No indicado', null=False)
    fecha_fin = DateTimeField(null=False, verbose_name='Fin de produccion estimado')

    def __str__(self, ):

        return f"Objeto {self.verbose_name}, Codigo de producto: {self.molde}, Maquina: {self.maquina}," \
               f"Mantenimiento de maquina al final de la produccion: {self.mantenimiento_maq}, " \
               f"Mantenimiento de molde al final de la produccion: {self.mantenimiento_molde}, Material: " \
               f"{self.material1}+{self.material2}+{self.material3}, color: {self.color}, porcentajes: " \
               f"{self.pm1}+{self.pm2}+{self.pm3} correspondientemente, porcentaje color: {self.porc_color}"


class Registro(Produccion):
    orden_numero = ForeignKeyField(Planificacion,
                                   field=Planificacion.codigo, backref='Orden_produccion', verbose_name='Ordenes')
    lote_numero = CharField(max_length=255, null=True, default='Pedir a Calidad', verbose_name='Lotes')
    fecha = DateTimeField(null=False, help_text='Indicar fecha real de produccion', verbose_name='Fechas')
    turno = CharField(max_length=255, null=False, help_text="Usar categorias inconfundibles ej. Mañana, Tarde, Noche",
                      verbose_name='Turnos')
    produccion = IntegerField(null=False, verbose_name='Produccion')
    unidad = CharField(null=False, help_text='Unidad del volumen de produccion registrado', verbose_name='Unidades')
    malas = FloatField(null=False, help_text='Kilogramos de Piezas que fueron descartados')
    molido = BooleanField(default=False, null=False)
    porcentaje_molido = IntegerField(default=0, help_text='Porcentaje de molinda utilizado')
    falla = BooleanField(default=False, help_text='Indicar si hubo parada por fallas', verbose_name='Fallas')
    novedad = BlobField(null=False, verbose_name='Novedades')

    def __str__(self, ):
        return f"Para la orden # {self.orden_numero.id}, de cliente: {self.orden_numero.cliente.razon_social}," \
               f" se produjeron {self.produccion} {self.unidad}s el dia {self.falla}, en el turno: {self.turno}"


produccion_db.connect()
produccion_db.create_tables([Maquina, Molde, Planificacion, MateriaPrima, Registro, Periferico])
produccion_db.close()
