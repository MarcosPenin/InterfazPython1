import var

class Clientes():

    def validarDni():
        try:
            tabla = "TRWAGMYFPDXBNJZSQVHLCKE"
            numeros = "1234567890"
            dni=var.ui.dni.text()
            if (len(dni) == 9):
                letraControl = dni[8].upper()
                dni = dni[:8]
                if (len(dni) == len([n for n in dni if n in numeros])):
                    if tabla[int(dni) % 23] == letraControl:
                        var.ui.label.setText('V')
                        var.ui.label.setStyleSheet('QLabel{color:green;font-size:14pt;font-weight:bold;}')
                    else:
                        var.ui.label.setStyleSheet('QLabel{color:red;font-size:14pt;font-weight:bold;}')
                        var.ui.label.setText('X')
            else:
                var.ui.label.setText('X')
                var.ui.label.setStyleSheet('QLabel {color:red;font-size:14pt;font-weight:bold;}')

        except Exception as error:
            print('Error en módulo validar DNI', error)

    def selSexo(self):
        try:
            if var.ui.femenino.isChecked():
                print("Seleccionado femenino")
            if var.ui.masculino.isChecked():
                print("Seleccionado masculino")
        except Exception as error:
            print("Error en módulo de selección de sexo:", error)

    def selPago(self):
        try:
            if var.ui.chkEfectivo.isChecked():
                print("Pagas en efectivo")
            if var.ui.chkTarjeta.isChecked():
                print("Pagas con tarjeta")
            if var.ui.chkTransferencia.isChecked():
                print("Pagas mediante transferencia")
        except Exception as error:
            print("Error en módulo de selección de sexo:", error)

    def cargarProv():
        try:
            prov=['','A Coruña','Lugo','Ourense','Pontevedra']
            for i in prov:
                var.ui.provincia.addItem(i)
        except Exception as error:
            print("Error en módulo de selección de sexo:", error)


    def selProv(prov):
        try:
            print("Ha seleccionado la provincia de ",prov)
        except Exception as error:
            print("Error en módulo de selección de sexo:", error)
