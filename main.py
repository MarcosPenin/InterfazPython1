import Conexion
import events
import venCalendar
import ventana
import windowaviso
from ventana import *
import sys
import var
import clientes
from datetime import datetime

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        var.ui = ventana.Ui_Proxecto1()
        var.ui.setupUi(self)
        var.dlgCalendar= DialogCalendar()
        var.ui.salir.triggered.connect(events.Eventos.Salir)
        var.ui.dni.editingFinished.connect(clientes.Clientes.validarDni)
        var.ui.elegirSexo.buttonClicked.connect(clientes.Clientes.selSexo)
        var.chkPago = (var.ui.chkEfectivo, var.ui.chkTarjeta, var.ui.chkTransferencia)
        for i in var.chkPago:
            i.stateChanged.connect(clientes.Clientes.selPago)
        clientes.Clientes.cargarProv()
        var.ui.provincia.activated[str].connect(clientes.Clientes.selProv)
        var.ui.fecha.clicked.connect(clientes.Clientes.abrirCalendar)
        var.ui.altaCliente.clicked.connect(clientes.Clientes.altaClientes)
        var.ui.limpiar.clicked.connect(Conexion.Conexion.limpiarCli)
        var.ui.limpiar2.clicked.connect(Conexion.Conexion.limpiarCli)
        var.ui.eliminar.clicked.connect(clientes.Clientes.bajaCliente)
        var.ui.buscar.clicked.connect(Conexion.Conexion.buscarCli)
        Conexion.Conexion.db_connect(var.filedb)
        Conexion.Conexion.mostrarClientes(self)







class DialogSalir(QtWidgets.QDialog):
    def __init__(self):
        super(DialogSalir, self).__init__()
        var.dlgSlr = windowaviso.Ui_Dialog()
        var.dlgSlr.setupUi(self)
        var.ui.botonSalir.clicked.connect(events.Eventos.Salir2)

class DialogCalendar(QtWidgets.QDialog):
    def __init__(self):
        super(DialogCalendar,self).__init__()
        var.dlgCalendar=venCalendar.Ui_Dialog()
        var.dlgCalendar.setupUi(self)
        diaActual = datetime.now().day
        mesActual = datetime.now().month
        anoActual = datetime.now().year
        var.dlgCalendar.calendarWidget.setSelectedDate(QtCore.QDate(anoActual,mesActual,diaActual))
        var.dlgCalendar.calendarWidget.clicked.connect(clientes.Clientes.cargarFecha)


if __name__ == '__main__':
    app=QtWidgets.QApplication([])
    window=Main()
    var.dlgSlr=DialogSalir()
    window.show()
    sys.exit(app.exec())