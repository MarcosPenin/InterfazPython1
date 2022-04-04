import os
import var
from reportlab.pdfgen import canvas
from PyQt5 import QtWidgets, QtSql
from datetime import *


class Printer():

    def reportCli(self):
        try:
            var.rep = canvas.Canvas('informes/listadoClientes.pdf')
            var.rep.drawString(235, 735, 'LISTADO DE CLIENTES')
            var.rep.line(45, 720, 525, 720)
            Printer.cabecera(self)
            Printer.cuerpo(self)
            Printer.pie(self)
            var.rep.save()
            rootPath = ".\\informes"
            cont = 0
            for file in os.listdir(rootPath):
                if file.endswith(".pdf"):
                    os.startfile("%s/%s" % (rootPath, file))
                    cont = cont + 1
        except Exception as error:
            print("Error reporcli %s" % str(error))

    def cabecera(self):
        try:
            var.rep.setTitle('INFORMES')
            var.rep.setAuthor('Administración')
            var.rep.setFont('Helvetica', size=10)
            var.rep.line(45, 820, 525, 820)
            var.rep.line(45, 820, 525, 820)
            textCif = "B17171717"
            textNom = "GESTIÓN DE CLIENTES EN PYTHON S.L."
            textDir = "Avenida del Álamo 18"
            textTlf = "986 56 56 56"
            var.rep.drawString(50, 805, textCif)
            var.rep.drawString(50, 790, textNom)
            var.rep.drawString(50, 775, textDir)
            var.rep.drawString(50, 760, textTlf)
        except Exception as error:
            print("Error reporcli %s" % str(error))

    def cuerpo(self):

        var.rep.setFont("Helvetica-Bold", size=9)
        itemCli = ["DNI", "APELLIDOS", "NOMBRE", "SEXO", "FORMATOPAGO"]
        var.rep.drawString(60, 705, itemCli[0])
        var.rep.drawString(130, 705, itemCli[1])
        var.rep.drawString(250, 705, itemCli[2])
        var.rep.drawString(350, 705, itemCli[3])
        var.rep.drawString(420, 705, itemCli[4])
        var.rep.line(45, 698, 525, 698)

        query = QtSql.QSqlQuery()
        query.prepare('select dni,apellidos,nombre,sexo,formatopago from clientes')
        if query.exec_():
            print("query ejecutada")
            i = 50
            j = 680
            while query.next():
                var.rep.drawString(i, j, str(query.value(0)))
                var.rep.drawString(i + 80, j, str(query.value(1)))
                var.rep.drawString(i + 205, j, str(query.value(2)))
                var.rep.drawString(i + 300, j, str(query.value(3)))
                var.rep.drawString(i + 380, j, str(query.value(4)))
                j = j - 30

    def pie(self):
        try:
            var.rep.line(50,50,525,50)
            fecha=datetime.today()
            fecha=fecha.strftime('%d.%m.%Y %H.%M.%S')
            var.rep.setFont('Helvetica-Oblique',size=7)
            var.rep.drawString(460,40,str(fecha))
            var.rep.drawString(275,40,str('Página %s' % var.rep.getPageNumber()))
        except Exception as error:
            print("Error pie del informe %s" % str(error))