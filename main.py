import events
import ventana
import windowaviso
from ventana import *
import sys
import var
import clientes


class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        var.ui = ventana.Ui_Proxecto1()
        var.ui.setupUi(self)
        var.ui.salir.triggered.connect(events.Eventos.Salir)
        var.ui.dni.editingFinished.connect(clientes.Clientes.validarDni)
        var.ui.elegirSexo.buttonClicked.connect(clientes.Clientes.selSexo)
        var.chkPago = (var.ui.chkEfectivo, var.ui.chkTarjeta, var.ui.chkTransferencia)
        for i in var.chkPago:
            i.stateChanged.connect(clientes.Clientes.selPago)
        clientes.Clientes.cargarProv()
        var.ui.provincia.activated[str].connect(clientes.Clientes.selProv)

class DialogSalir(QtWidgets.QDialog):
    def __init__(self):
        super(DialogSalir, self).__init__()
        var.dlgSlr = windowaviso.Ui_Dialog()
        var.dlgSlr.setupUi(self)
        var.ui.aceptar_2.clicked.connect(events.Eventos.Salir2)

if __name__ == '__main__':
    app=QtWidgets.QApplication([])
    window=Main()
    var.dlgSlr=DialogSalir()
    window.show()
    sys.exit(app.exec())