from moldeUI import *
from PyQt5.QtWidgets import QDialog, QMessageBox, QTableWidgetItem
from produccion.produccion_model import *
from pedidos.pedido_model import *
from mantenimiento.mtto_model import *


class ModuloMolde(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, ):
        super(ModuloMolde, self).__init__()
        self.setupUi(self)
        combo_si = ['Indique', 'Si', 'No']
        self.comboBox.addItems(combo_si)
        self.comboBox_2.addItems(combo_si)
        self.comboBox_3.addItems(combo_si)
        self.comboBox_4.addItems(combo_si)
        self.pushButton.clicked.connect(self.registrar_molde)

    def registrar_molde(self, ):
        molde_nuevo = Molde()
        molde_nuevo.nombre = self.lineEdit.text()
        molde_nuevo.fabricante = self.lineEdit_2.text()
        molde_nuevo.n_cavidades = int(self.lineEdit_3.text())
        molde_nuevo.cavidades_disponibles = int(self.lineEdit_4.text())
        molde_nuevo.ultimo_ciclo = float(self.lineEdit_5.text())
        molde_nuevo.alto = float(self.lineEdit_6.text())
        molde_nuevo.ancho = float(self.lineEdit_7.text())
        molde_nuevo.profundo = float(self.lineEdit_8.text())
        molde_nuevo.materia_prima = self.lineEdit_9.text()
        molde_nuevo.peso_molde = float(self.lineEdit_10.text())
        molde_nuevo.peso_pieza = float(self.lineEdit_11.text())
        molde_nuevo.noyo = self.comboBox.currentText()
        molde_nuevo.colada_caliente = self.comboBox_3.currentText()
        molde_nuevo.mantenimiento = self.comboBox_2.currentText()
        molde_nuevo.disponible = self.comboBox_4.currentText()
        molde_nuevo.save()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    windows = ModuloMolde()
    windows.show()
    app.exec_()


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


e = Molde.select()
for x in e:
    print(x)
