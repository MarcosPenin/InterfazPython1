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
