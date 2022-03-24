from PyQt5 import QtWidgets,QtSql

import Conexion
import var

class Conexion():

    def db_connect(filename):
        db=QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName(filename)
        if not db.open():
            QtWidgets.QMessageBox.critical(None,'No se puede abrir la base de datos,'
                                                'No se puede establecer conexion.\n Haz Click para Cancelar',
                                           QtWidgets.QMessageBox.Cancel)
            return False
        else:
            print('Conexion establecida')

        return True

    def cargarCli(cliente):

            query=QtSql.QSqlQuery()
            query.prepare('insert into clientes(dni,apellidos,nombre,direccion,provincia,sexo,formatopago)'
                          'VALUES(:dni,:apellidos,:nombre,:direccion,:provincia,:sexo,:formatopago)')
            query.bindValue(':dni',str(cliente[0]))
            query.bindValue(':apellidos',str(cliente[1]))
            query.bindValue(':nombre',str(cliente[2]))
            query.bindValue(':direccion',str(cliente[3]))
            query.bindValue(':provincia',str(cliente[4]))
            query.bindValue(':formatopago', str(cliente[5]))
            query.bindValue(':sexo',str(cliente[6]))

            if query.exec_():
                var.ui.mensajes.setText('Cliente dado de alta')
                Conexion.mostrarClientes(self)
                Conexion.limpiarCli()
            else:
                var.ui.mensajes.setText('Error al cargar cliente')
                print("Error: ",query.lastError().text())

    def mostrarClientes(self):
        index=0
        query=QtSql.QSqlQuery()
        query.prepare('select dni,apellidos,nombre from clientes')
        if query.exec_():
            while query.next():
                dni=query.value(0)
                apellidos=query.value(1)
                nombre=query.value(2)
                var.ui.tablaClientes.setRowCount(index+1)
                var.ui.tablaClientes.setItem(index,0,QtWidgets.QTableWidgetItem(dni))
                var.ui.tablaClientes.setItem(index, 1, QtWidgets.QTableWidgetItem(apellidos))
                var.ui.tablaClientes.setItem(index, 2, QtWidgets.QTableWidgetItem(nombre))
                index+=1
        else:
            print("Error mostrar clientes: ",query.lastError().text())

    def bajaCli(dni):
        query= QtSql.QSqlQuery()
        query.prepare('delete from clientes where dni = :dni')
        query.bindValue(':dni',dni)
        if query.exec_():
            if(dni!=""):
                var.ui.mensajes.setText('Cliente con dni '+dni+' dado de baja')
        else:
            print("Error eliminar clientes: ", query.lastError().text())

    def limpiarCli(self):
        var.ui.dni.setText("")
        var.ui.fechaAlta.setText("")
        var.ui.apellidos.setText("")
        var.ui.nombre.setText("")
        var.ui.direccion.setText("")
        var.ui.label.setText("")
        var.ui.provincia.setCurrentIndex(0)
        var.ui.mensajes.setText("")

    def buscarCli(self):
        dni = var.ui.dni.text()
        query = QtSql.QSqlQuery()
        query.prepare('select apellidos,nombre, direccion,provincia,sexo,formatopago from clientes where dni= :dni')
        query.bindValue(':dni', dni)

        flag=False
        if query.exec_():
            while query.next():
                flag=True
                nombre=query.value(0)
                apellidos=query.value(1)
                direccion=query.value(2)
                provincia=query.value(3)
                sexo = query.value(4)
                formatopago = query.value(5)

                var.ui.nombre.setText(nombre)
                var.ui.apellidos.setText(apellidos)
                var.ui.direccion.setText(direccion)

                if(provincia=="A Coruña"):
                    var.ui.provincia.setCurrentIndex(1)
                if(provincia=="Lugo"):
                    var.ui.provincia.setCurrentIndex(2)
                if(provincia=="Ourense"):
                    var.ui.provincia.setCurrentIndex(3)
                if(provincia=="Pontevedra"):
                    var.ui.provincia.setCurrentIndex(4)
                if(sexo=="Mujer"):
                    var.ui.femenino.click()
                else:
                    var.ui.masculino.click()
                if(formatopago=="Efectivo"):
                    var.ui.chkEfectivo.click()
                if (formatopago == "Tarjeta"):
                    var.ui.chkEfectivo.click()
                if (formatopago == "Transferencia"):
                    var.ui.chkEfectivo.click()
            if flag==False:
                var.ui.mensajes.setText('DNI NO ENCONTRADO')
        else:
            print("Error buscar clientes: ",query.lastError().text())


    def modifCli(dni,newdata):
        query=QtSql.QSqlQuery()
        query.prepare('update clientes set apellidos=:apellidos,nombre=:nombre,direccion=:direccion,provincia=:provincia,sexo=:sexo,formatopago=:formatopago '
                      'where dni=:dni')
        query.bindValue(':dni', dni)
        query.bindValue(':apellidos', str(newdata[0]))
        query.bindValue(':nombre', str(newdata[1]))
        query.bindValue(':direccion', str(newdata[2]))
        query.bindValue(':provincia', str(newdata[3]))
        query.bindValue(':sexo', str(newdata[4]))
        query.bindValue(':formatopago', str(newdata[5]))

        if query.exec_():
            var.ui.mensajes.setText('Cliente con dni '+dni+ ' modificado')
        else:
            print("Error al modificar clientes: ", query.lastError().text())
            var.ui.mensajes.setText('Faltan datos')









