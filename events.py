import os.path
import shutil
import sys
import zipfile
from datetime import datetime

from PyQt5 import QtWidgets
import xlrd
import Conexion
import clientes
import main
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

    def AbrirDir(selfself):
        try:
            var.filedlgabrir.show()
        except Exception as error:
            print("Error abrir explorardor: %s" %str(error))

    def Backup():
        try:
            fecha=datetime.today()
            fecha=fecha.strftime('%Y.%m.%d.%H.%M.%S')
            var.copia= (str(fecha)+'_backup.zip')
            option=QtWidgets.QFileDialog.Options()
            directorio,filename=var.filedlgabrir.getSaveFileName(None,'Guardar Copia',var.copia,'zip',options=option)
            if var.filedlgabrir.Accepted and filename !='':
                fichzip=zipfile.ZipFile(var.copia,'w')
                fichzip.write(var.filedb,os.path.basename(var.filedb),zipfile.ZIP_DEFLATED)
                fichzip.close()
                var.ui.mensajes.setText("Base de datos guardada")
                shutil.move(str(var.copia),str(directorio))
        except Exception as error:
            print('"Error: %s' % str(error))


    def recuperarBackup(self):
        ventana_restaurar = QtWidgets.QFileDialog
        filename = ventana_restaurar.getOpenFileName(None, 'Restaurar Copia', "Copia de seguridad BD",
                                                     "Archivos Zip (*.zip)")
        var.filedb=shutil.unpack_archive(filename.__getitem__(0))
        os.system('python "E:\Interfaces\InterfazPython1\main.py"')
        sys.exit()

    def recuperarExcel():
        documento=xlrd.open_workbook("datos.xls")
        clientesNuevos=documento.sheet_by_index(0)

        filasClientes=clientesNuevos.nrows
        fila=0

        while fila < filasClientes:
            dni=clientesNuevos.cell_value(fila,0)
            apellidos=clientesNuevos.cell_value(fila,1)
            nombre=clientesNuevos.cell_value(fila,2)
            direccion=clientesNuevos.cell_value(fila,3)
            provincia=clientesNuevos.cell_value(fila,4)
            formatopago = clientesNuevos.cell_value(fila, 5)
            sexo=clientesNuevos.cell_value(fila,6)
            envio=clientesNuevos.cell_value(fila,7)
            newcli=[dni,apellidos,nombre,direccion,provincia,sexo,formatopago,envio]
            fila+=1

            Conexion.Conexion.cargarCli2(newcli)





















