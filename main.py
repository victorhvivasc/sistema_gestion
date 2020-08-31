from produccion.produccion_model import *
from pedidos.pedido_model import *
from mantenimiento.mtto_model import *


def maquina_nueva(numero=None, ):
    m_n = Maquina()
    m_n.numero = numero
    m_n.fabricante = "Battenfeld"
    m_n.modelo = "125t"
    m_n.ano = 2010
    m_n.planta = 'Inyeccion'
    m_n.disponible = False
    m_n.capacidad = 125
    m_n.mantenimiento = True
    m_n.tipo = 'Inyeccion'
    m_n.save()


e = Orden.select()
for x in e:
    print(x)
