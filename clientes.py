from PyQt5 import QtCore, QtGui, QtWidgets

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
            global sex
            if var.ui.femenino.isChecked():
                sex="Mujer"
            if var.ui.masculino.isChecked():
               sex="Hombre"
        except Exception as error:
            print("Error en módulo de selección de sexo:", error)

    def selPago(self):
        try:
            var.pay=[]
            if var.ui.chkEfectivo.isChecked():
                var.pay.append("Efectivo")
            if var.ui.chkTarjeta.isChecked():
                var.pay.append("Tarjeta")
            if var.ui.chkTransferencia.isChecked():
                var.pay.append("Transferencia")
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
            global vpro
            vpro= prov
        except Exception as error:
            print("Error en módulo de selección de sexo:", error)


    def abrirCalendar():
        try:
            var.dlgCalendar.show()
        except Exception as error:
            print("Error en módulo de selección de sexo:", error)

    def cargarFecha(qDate):
        try:
            data=('{0}/{1}/{2}'.format(qDate.day(),qDate.month(),qDate.year()))
            var.ui.fechaAlta.setText(str(data))
            var.dlgCalendar.hide()
        except Exception as error:
            print("Error en módulo de selección de sexo:", error)

    def showClients():
        try:
            newcli = []
            clitab = []
            client= [var.ui.dni, var.ui.apellidos, var.ui.nombre]
            k = 0

            for i in client:
                newcli.append(i.text())
                if(k<3):
                    clitab.append(i.text())
                    k += 1
            newcli.append(vpro)
            var.pay=set(var.pay)
            for j in var.pay:
                newcli.append(j)
            newcli.append(sex)
            print(newcli)
            print(clitab)
            row = 0
            column=0
            var.ui.tablaClientes.insertRow(row)
            for registro in clitab:
                cell=QtWidgets.QTableWidgetItem(registro)
                var.ui.tablaClientes.setItem(row,column,cell)
                column +=1
        except Exception as error:
            print("Error: %s", str(error))



