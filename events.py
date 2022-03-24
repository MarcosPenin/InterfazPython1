import os.path
import shutil
import sys
import zipfile
from datetime import datetime


from PyQt5 import QtWidgets

import Conexion
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

        print(filename.__getitem__(0))

        var.filedb=shutil.unpack_archive(filename.__getitem__(0))

        Conexion.Conexion.db_connect(var.filedb)

        Conexion.Conexion.mostrarClientes(self)











