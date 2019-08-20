import sys
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QListWidgetItem, QListWidget, QErrorMessage, QDialogButtonBox
from PyQt5 import QtGui
from PyQt5.QtCore import *
from PantallaPincipal import Ui_MainWindow
import Regla1, Regla2, Regla3, Regla4, Regla5, Regla6, Regla7, Regla8
import final

prologa = final.getProlog()

class WinRegla1(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Regla1.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pbAdd.setDisabled(True)
        self.ui.pbRemove.setDisabled(True)
        self.ui.lblPresupuesto.setText(str(final.getClavo(prologa)))
        self.ui.pbBuscar.clicked.connect(self.llenarListas)
        self.modelSugerencias = QtGui.QStandardItemModel()
        self.ui.listSugerencias.setModel(self.modelSugerencias)
        self.modelCarrito = QtGui.QStandardItemModel()
        self.ui.listCarrito.setModel(self.modelCarrito)
        self.ui.pbAdd.clicked.connect(self.itemACarrito)
        self.ui.pbRemove.clicked.connect(self.itemASeleccion)
        self.ui.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)
        self.ui.buttonBox.button(QDialogButtonBox.Ok).clicked.connect(self.assertBoughtBooks)
        
    def llenarListas(self):
        if self.modelSugerencias.rowCount()>0:
            self.modelSugerencias.removeRows(0,self.modelSugerencias.rowCount())
        dias = int(self.ui.spnDias.value())
        libros, combinaciones = final.regla1(prologa, final.getClavo(prologa), dias)
        if(len(libros) == 0):
            error_dialog = QErrorMessage(self)
            error_dialog.showMessage('No existen libros con estos parametros')
            error_dialog.exec_()
        else:
            for combo in combinaciones:
                combineshan = QtGui.QStandardItem("Combinacion " + str(combinaciones.index(combo)))
                for book in combo:
                    print(book)
                    item = QtGui.QStandardItem(str(book))
                    combineshan.appendRow(item)
                if combo.__len__()>0:
                    self.modelSugerencias.appendRow(combineshan)
                
            self.ui.pbAdd.setEnabled(True)
            self.ui.pbRemove.setEnabled(True)
            self.ui.buttonBox.button(QDialogButtonBox.Ok).setEnabled(True)
    
    
    def itemACarrito(self):
        self.modelCarrito.appendRow(self.modelSugerencias.takeItem(self.ui.listSugerencias.currentIndex().row()))
    def itemASeleccion(self):
        self.modelSugerencias.appendRow(self.modelCarrito.takeItem(self.ui.listCarrito.currentIndex().row()))
    def assertBoughtBooks(self):
        for index in range(self.modelCarrito.rowCount()):
            item = self.modelCarrito.item(index)
            for libroIndex in range(item.rowCount()):
                libro = item.child(libroIndex)
                final.buyBook(prologa,libro.text())
            
class WinRegla2(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Regla2.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pbAdd.setDisabled(True)
        self.ui.pbRemove.setDisabled(True)        
        self.ui.cbxCategoria.addItems(final.getCategories(prologa))
        self.ui.lblPresupuesto.setText(str(final.getClavo(prologa)))
        self.ui.pbBuscar.clicked.connect(self.llenarListas)
        self.modelSugerencias = QtGui.QStandardItemModel()
        self.ui.listSugerencias.setModel(self.modelSugerencias)
        self.modelCarrito = QtGui.QStandardItemModel()
        self.ui.listCarrito.setModel(self.modelCarrito)
        self.ui.pbAdd.clicked.connect(self.itemACarrito)
        self.ui.pbRemove.clicked.connect(self.itemASeleccion)
        self.ui.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)
        self.ui.buttonBox.button(QDialogButtonBox.Ok).clicked.connect(self.assertBoughtBooks)
    
    def llenarListas(self):
        if self.modelSugerencias.rowCount()>0:
            self.modelSugerencias.removeRows(0,self.modelSugerencias.rowCount())
        libros, combinaciones = final.regla2(prologa, final.getClavo(prologa), self.ui.cbxCategoria.currentText(), self.ui.spnRating.value())
        if(len(libros) == 0):
            error_dialog = QErrorMessage(self)
            error_dialog.showMessage('No existen libros con estos parametros')
            error_dialog.exec_()
        else:
            for combo in combinaciones:
                combineshan = QtGui.QStandardItem("Combinacion " + str(combinaciones.index(combo)))
                for book in combo:
                    print(book)
                    item = QtGui.QStandardItem(str(book))
                    combineshan.appendRow(item)
                if combo.__len__()>0:
                    self.modelSugerencias.appendRow(combineshan)
            self.ui.pbAdd.setEnabled(True)
            self.ui.pbRemove.setEnabled(True)
            self.ui.buttonBox.button(QDialogButtonBox.Ok).setEnabled(True)

    def itemACarrito(self):
        self.modelCarrito.appendRow(self.modelSugerencias.takeItem(self.ui.listSugerencias.currentIndex().row()))
    def itemASeleccion(self):
        self.modelSugerencias.appendRow(self.modelCarrito.takeItem(self.ui.listCarrito.currentIndex().row()))
    def assertBoughtBooks(self):
        for index in range(self.modelCarrito.rowCount()):
            item = self.modelCarrito.item(index)
            for libroIndex in range(item.rowCount()):
                libro = item.child(libroIndex)
                final.buyBook(prologa,libro.text())

class WinRegla3(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Regla3.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pbAdd.setDisabled(True)
        self.ui.pbRemove.setDisabled(True)
        self.ui.lblPresupuesto.setText(str(final.getClavo(prologa) + final.getSalary(prologa)))
        self.ui.pbBuscar.clicked.connect(self.llenarListas)
        self.modelSugerencias = QtGui.QStandardItemModel()
        self.ui.listSugerencias.setModel(self.modelSugerencias)
        self.modelCarrito = QtGui.QStandardItemModel()
        self.ui.listCarrito.setModel(self.modelCarrito)
        self.ui.pbAdd.clicked.connect(self.itemACarrito)
        self.ui.pbRemove.clicked.connect(self.itemASeleccion)
        self.ui.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)
        self.ui.buttonBox.button(QDialogButtonBox.Ok).clicked.connect(self.assertBoughtBooks)
    
    def llenarListas(self):
        if self.modelSugerencias.rowCount()>0:
            self.modelSugerencias.removeRows(0,self.modelSugerencias.rowCount())
        percent = int(self.ui.spnPorcentaje.value())
        estado = "_"
        if (self.ui.chkNuevo.isChecked() and (not self.ui.chkUsado.isChecked())):
            estado="nuevo"
        elif ((not self.ui.chkNuevo.isChecked()) and self.ui.chkUsado.isChecked()):
            estado="usado"
        else:
            estado = "_"

        libros, combinaciones = final.regla3(prologa,estado,percent)
        if(len(libros) == 0):
            error_dialog = QErrorMessage(self)
            error_dialog.showMessage('No existen libros con estos parametros')
            error_dialog.exec_()
        else:
            for combo in combinaciones:
                combineshan = QtGui.QStandardItem("Combinacion " + str(combinaciones.index(combo)))
                for book in combo:
                    print(book)
                    item = QtGui.QStandardItem(str(book))
                    combineshan.appendRow(item)
                if combo.__len__()>0:
                    self.modelSugerencias.appendRow(combineshan)
            self.ui.pbAdd.setEnabled(True)
            self.ui.pbRemove.setEnabled(True)
            self.ui.buttonBox.button(QDialogButtonBox.Ok).setEnabled(True)
    def itemACarrito(self):
        self.modelCarrito.appendRow(self.modelSugerencias.takeItem(self.ui.listSugerencias.currentIndex().row()))
    def itemASeleccion(self):
        self.modelSugerencias.appendRow(self.modelCarrito.takeItem(self.ui.listCarrito.currentIndex().row()))
    def assertBoughtBooks(self):
        for index in range(self.modelCarrito.rowCount()):
            item = self.modelCarrito.item(index)
            for libroIndex in range(item.rowCount()):
                libro = item.child(libroIndex)
                final.buyBook(prologa,libro.text())

class WinRegla4(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Regla4.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pbAdd.setDisabled(True)
        self.ui.pbRemove.setDisabled(True)
        self.ui.pbBuscar.clicked.connect(self.llenarListas)
        self.ui.cbxCategoria.addItems(final.getCategories(prologa))
        self.modelSugerencias = QtGui.QStandardItemModel()
        self.ui.listSugerencias.setModel(self.modelSugerencias)
        self.modelCarrito = QtGui.QStandardItemModel()
        self.ui.listCarrito.setModel(self.modelCarrito)
        self.ui.pbAdd.clicked.connect(self.itemACarrito)
        self.ui.pbRemove.clicked.connect(self.itemASeleccion)
        self.ui.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)
        self.ui.buttonBox.button(QDialogButtonBox.Ok).clicked.connect(self.assertBoughtBooks)
    
    def llenarListas(self):
        if self.modelSugerencias.rowCount()>0:
            self.modelSugerencias.removeRows(0,self.modelSugerencias.rowCount())
        
        percentSueldo = int(self.ui.spnPorcentajeSueldo.value())
        autor = self.ui.txtAutor.text()
        categoria = self.ui.cbxCategoria.currentText()
        frase = self.ui.linePalabra.text()

        libros, combinaciones = final.regla4(prologa,percentSueldo,autor,categoria,frase)

        if(len(libros) == 0):
            error_dialog = QErrorMessage(self)
            error_dialog.showMessage('No existen libros con estos parametros')
            error_dialog.exec_()
        else:
            for combo in combinaciones:
                combineshan = QtGui.QStandardItem("Combinacion " + str(combinaciones.index(combo)))
                for book in combo:
                    print(book)
                    item = QtGui.QStandardItem(str(book))
                    combineshan.appendRow(item)
                if combo.__len__()>0:
                    self.modelSugerencias.appendRow(combineshan)
            self.ui.pbAdd.setEnabled(True)
            self.ui.pbRemove.setEnabled(True)
            self.ui.buttonBox.button(QDialogButtonBox.Ok).setEnabled(True)
    def itemACarrito(self):
        self.modelCarrito.appendRow(self.modelSugerencias.takeItem(self.ui.listSugerencias.currentIndex().row()))
    def itemASeleccion(self):
        self.modelSugerencias.appendRow(self.modelCarrito.takeItem(self.ui.listCarrito.currentIndex().row()))
    def assertBoughtBooks(self):
        for index in range(self.modelCarrito.rowCount()):
            item = self.modelCarrito.item(index)
            for libroIndex in range(item.rowCount()):
                libro = item.child(libroIndex)
                final.buyBook(prologa,libro.text())

class WinRegla5(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Regla5.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pbAdd.setDisabled(True)
        self.ui.pbRemove.setDisabled(True)
        self.ui.cbxCategoria.addItems(final.getCategories(prologa))
        self.ui.pbBuscar.clicked.connect(self.llenarListas)
        self.modelSugerencias = QtGui.QStandardItemModel()
        self.ui.listSugerencias.setModel(self.modelSugerencias)
        self.modelCarrito = QtGui.QStandardItemModel()
        self.ui.listCarrito.setModel(self.modelCarrito)
        self.ui.pbAdd.clicked.connect(self.itemACarrito)
        self.ui.pbRemove.clicked.connect(self.itemASeleccion)
        self.ui.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)
        self.ui.buttonBox.button(QDialogButtonBox.Ok).clicked.connect(self.assertBoughtBooks)
    
    def llenarListas(self):
        if self.modelSugerencias.rowCount()>0:
            self.modelSugerencias.removeRows(0,self.modelSugerencias.rowCount())
        categoria = self.ui.cbxCategoria.currentText()
        rating = self.ui.spnRating.value()
        
        libros, combinaciones = final.regla5(prologa,categoria,rating)
        if(len(libros) == 0):
            error_dialog = QErrorMessage(self)
            error_dialog.showMessage('No existen libros con estos parametros')
            error_dialog.exec_()
        else:
            for combo in combinaciones:
                combineshan = QtGui.QStandardItem("Combinacion " + str(combinaciones.index(combo)))
                for book in combo:
                    print(book)
                    item = QtGui.QStandardItem(str(book))
                    combineshan.appendRow(item)
                if combo.__len__()>0:
                    self.modelSugerencias.appendRow(combineshan)
            self.ui.pbAdd.setEnabled(True)
            self.ui.pbRemove.setEnabled(True)
            self.ui.buttonBox.button(QDialogButtonBox.Ok).setEnabled(True)

    def itemACarrito(self):
        self.modelCarrito.appendRow(self.modelSugerencias.takeItem(self.ui.listSugerencias.currentIndex().row()))
    def itemASeleccion(self):
        self.modelSugerencias.appendRow(self.modelCarrito.takeItem(self.ui.listCarrito.currentIndex().row()))
    def assertBoughtBooks(self):
        for index in range(self.modelCarrito.rowCount()):
            item = self.modelCarrito.item(index)
            for libroIndex in range(item.rowCount()):
                libro = item.child(libroIndex)
                final.buyBook(prologa,libro.text())
        
class WinRegla6(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Regla6.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pbAdd.setDisabled(True)
        self.ui.pbRemove.setDisabled(True)
        self.ui.pbBuscar.clicked.connect(self.llenarListas)
        self.modelSugerencias = QtGui.QStandardItemModel()
        self.ui.listSugerencias.setModel(self.modelSugerencias)
        self.modelCarrito = QtGui.QStandardItemModel()
        self.ui.listCarrito.setModel(self.modelCarrito)
        self.ui.pbAdd.clicked.connect(self.itemACarrito)
        self.ui.pbRemove.clicked.connect(self.itemASeleccion)
        self.ui.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)
        self.ui.buttonBox.button(QDialogButtonBox.Ok).clicked.connect(self.assertBoughtBooks)
        
    def llenarListas(self):
        condicion = "_"

        if (self.ui.cbxCondicion.currentText() == "Nuevos"):
            condicion = "nuevo"
        elif (self.ui.cbxCondicion.currentText() == "Usados"):
            condicion = "usado"
        if self.modelSugerencias.rowCount()>0:
            self.modelSugerencias.removeRows(0,self.modelSugerencias.rowCount())
        libros, combinaciones = final.regla6(prologa,condicion,self.ui.spnCosto.value())
        if(len(libros) == 0):
            error_dialog = QErrorMessage(self)
            error_dialog.showMessage('No existen libros con estos parametros')
            error_dialog.exec_()
        else:
            for combo in combinaciones:
                combineshan = QtGui.QStandardItem("Combinacion " + str(combinaciones.index(combo)))
                for book in combo:
                    print(book)
                    item = QtGui.QStandardItem(str(book))
                    combineshan.appendRow(item)
                if combo.__len__()>0:
                    self.modelSugerencias.appendRow(combineshan)
            self.ui.pbAdd.setEnabled(True)
            self.ui.pbRemove.setEnabled(True)
            self.ui.buttonBox.button(QDialogButtonBox.Ok).setEnabled(True)
    def itemACarrito(self):
        self.modelCarrito.appendRow(self.modelSugerencias.takeItem(self.ui.listSugerencias.currentIndex().row()))
    def itemASeleccion(self):
        self.modelSugerencias.appendRow(self.modelCarrito.takeItem(self.ui.listCarrito.currentIndex().row()))
    def assertBoughtBooks(self):
        for index in range(self.modelCarrito.rowCount()):
            item = self.modelCarrito.item(index)
            for libroIndex in range(item.rowCount()):
                libro = item.child(libroIndex)
                final.buyBook(prologa,libro.text())
                
class WinRegla7(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Regla7.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pbAdd.setDisabled(True)
        self.ui.pbRemove.setDisabled(True)
        self.ui.pbBuscar.clicked.connect(self.llenarListas)
        self.modelSugerencias = QtGui.QStandardItemModel()
        self.ui.listSugerencias.setModel(self.modelSugerencias)
        self.modelCarrito = QtGui.QStandardItemModel()
        self.ui.listCarrito.setModel(self.modelCarrito)
        self.ui.pbAdd.clicked.connect(self.itemACarrito)
        self.ui.pbRemove.clicked.connect(self.itemASeleccion)
        self.ui.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)
        self.ui.buttonBox.button(QDialogButtonBox.Ok).clicked.connect(self.assertBoughtBooks)
    
    def llenarListas(self):
        if self.modelSugerencias.rowCount()>0:
            self.modelSugerencias.removeRows(0,self.modelSugerencias.rowCount())
        autor = self.ui.lineAutor.text()
        libros, combinaciones = final.regla7(prologa,autor,self.ui.spnRating.value())
        if(len(libros) == 0):
            error_dialog = QErrorMessage(self)
            error_dialog.showMessage('No existen libros con estos parametros')
            error_dialog.exec_()
        else:
            for combo in combinaciones:
                combineshan = QtGui.QStandardItem("Combinacion " + str(combinaciones.index(combo)))
                for book in combo:
                    print(book)
                    item = QtGui.QStandardItem(str(book))
                    combineshan.appendRow(item)
                if combo.__len__()>0:
                    self.modelSugerencias.appendRow(combineshan)
            self.ui.pbAdd.setEnabled(True)
            self.ui.pbRemove.setEnabled(True)
            self.ui.buttonBox.button(QDialogButtonBox.Ok).setEnabled(True)
    def itemACarrito(self):
        self.modelCarrito.appendRow(self.modelSugerencias.takeItem(self.ui.listSugerencias.currentIndex().row()))
    def itemASeleccion(self):
        self.modelSugerencias.appendRow(self.modelCarrito.takeItem(self.ui.listCarrito.currentIndex().row()))
    def assertBoughtBooks(self):
        for index in range(self.modelCarrito.rowCount()):
            item = self.modelCarrito.item(index)
            for libroIndex in range(item.rowCount()):
                libro = item.child(libroIndex)
                final.buyBook(prologa,libro.text())

class WinRegla8(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Regla8.Ui_Dialog()
        self.ui.setupUi(self)  
        self.ui.pbAdd.setDisabled(True)
        self.ui.pbRemove.setDisabled(True)
        self.ui.pbBuscar.clicked.connect(self.llenarListas)
        self.modelSugerencias = QtGui.QStandardItemModel()
        self.ui.listSugerencias.setModel(self.modelSugerencias)
        self.modelCarrito = QtGui.QStandardItemModel()
        self.ui.listCarrito.setModel(self.modelCarrito)
        self.ui.pbAdd.clicked.connect(self.itemACarrito)
        self.ui.pbRemove.clicked.connect(self.itemASeleccion)
        self.ui.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)
        self.ui.buttonBox.button(QDialogButtonBox.Ok).clicked.connect(self.assertBoughtBooks)
    
    def llenarListas(self):
        if self.modelSugerencias.rowCount()>0:
            self.modelSugerencias.removeRows(0,self.modelSugerencias.rowCount())
        fecha = self.ui.dateAntesDe.date()
        
        anio = fecha.year()
        print(anio)
        autor = self.ui.lineAutor.text()
        
        libros, combinaciones = final.regla8(prologa,autor,self.ui.spnPrecio.value(),str(anio))
        if(len(libros) == 0):
            error_dialog = QErrorMessage(self)
            error_dialog.showMessage('No existen libros con estos parametros')
            error_dialog.exec_()
        else:
            for combo in combinaciones:
                combineshan = QtGui.QStandardItem("Combinacion " + str(combinaciones.index(combo)))
                for book in combo:
                    print(book)
                    item = QtGui.QStandardItem(str(book))
                    combineshan.appendRow(item)
                if combo.__len__()>0:
                    self.modelSugerencias.appendRow(combineshan)
            self.ui.pbAdd.setEnabled(True)
            self.ui.pbRemove.setEnabled(True)
            self.ui.buttonBox.button(QDialogButtonBox.Ok).setEnabled(True)
    def itemACarrito(self):
        self.modelCarrito.appendRow(self.modelSugerencias.takeItem(self.ui.listSugerencias.currentIndex().row()))
    def itemASeleccion(self):
        self.modelSugerencias.appendRow(self.modelCarrito.takeItem(self.ui.listCarrito.currentIndex().row()))
    def assertBoughtBooks(self):
        for index in range(self.modelCarrito.rowCount()):
            item = self.modelCarrito.item(index)
            for libroIndex in range(item.rowCount()):
                libro = item.child(libroIndex)
                final.buyBook(prologa,libro.text())

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        
        #accion de los botones y menus        
        self.ui.actionLibrosRecientesConEntradasExtraRegla1.triggered.connect(lambda: self.on_clicked(WinRegla1))
        self.ui.actionLibrosDeFiccinDe4OMsEstrellasConEntradasExtrasY10DeDescuento.triggered.connect(lambda: self.on_clicked(WinRegla2))
        self.ui.actionRegla3.triggered.connect(lambda: self.on_clicked(WinRegla3))
        self.ui.actionRegla4.triggered.connect(lambda: self.on_clicked(WinRegla4))
        self.ui.actionRegla5.triggered.connect(lambda: self.on_clicked(WinRegla5))
        self.ui.actionLibrosQueCuestenMenosQueX.triggered.connect(lambda: self.on_clicked(WinRegla6))
        self.ui.actionLibrosDeUnRatingYUnAutorEnEspecifico.triggered.connect(lambda: self.on_clicked(WinRegla7))
        self.ui.actionLibrosDeUnAutorQueNoPasenDeXPrecioYHayanSalidoEnUnAoX.triggered.connect(lambda: self.on_clicked(WinRegla8))
        self.ui.pbFondos.clicked.connect(self.mandarSalario)
        self.ui.pbBonos.clicked.connect(self.mandarClavo)
        self.ui.pbExit.clicked.connect(self.close)
        
            
        self.show()
    
    def eventFilter(self, obj, event):
        if event.type() == QEvent.FocusIn:  
            self.getComprados()
            return True

        return super(MainWindow, self).eventFilter(obj, event)
    
    def on_clicked(self,dialog):
        self.win=dialog()
        self.win.show()
    
    def getComprados(self):
        listaLibros = final.getBoughtBooks(prologa)
        print(listaLibros)
        model = QtGui.QStandardItemModel()
        self.ui.listaComprados.setModel(model)
        for libro in listaLibros:
            item = QtGui.QStandardItem(libro)
            model.appendRow(item)     
            
    def mostrarDinero(self):
        cualto = final.getSalary(prologa)
        clavo = final.getClavo(prologa)
        total = str(cualto + clavo)
        self.ui.lblFondosTotales.setText(total)
    
    def mandarSalario(self):
        saldo = self.ui.txtFondos.toPlainText()
        final.setSalary(prologa,saldo)
        self.mostrarDinero()
    
    def mandarClavo(self):
        clavo = self.ui.txtEntradas.toPlainText()
        final.setClavo(prologa,clavo)
        self.mostrarDinero()
    
                    

app = QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec_())
