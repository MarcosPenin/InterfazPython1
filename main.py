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