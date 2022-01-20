import sys

import var

class Eventos():

    def Saludo():
        try:
            var.ui.label.setText("Has pulsado el botón")
        except Exception as error:
            print("Error: %s",str(error))


    def Salir (self):
        try:
            sys.exit()
        except Exception as error:
            print("Error: %s", str(error))


    def Salir2(self):
        try:
            var.dlgSlr.show()
            if var.dlgSlr.exec():
                sys.exit()
            else:
                var.dlgSlr.hide()
        except Exception as error:
            print("Error: %s", str(error))






