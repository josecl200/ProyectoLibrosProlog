import sys
from PyQt5.QtWidgets import  QDialog, QApplication, QMainWindow, QListWidgetItem, QListWidget, QErrorMessage
from PyQt5 import QtGui
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
            for libro in libros:
                item = QtGui.QStandardItem(libro)
                self.modelSugerencias.appendRow(item)
            self.ui.pbAdd.setEnabled(True)
            self.ui.pbRemove.setEnabled(True)

        


    
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
    
    def llenarListas(self):
        if self.modelSugerencias.rowCount()>0:
            self.modelSugerencias.removeRows(0,self.modelSugerencias.rowCount())
        libros, combinaciones = final.regla2(prologa, final.getClavo(prologa), self.ui.cbxCategoria.currentText(), self.ui.spnRating.value())
        if(len(libros) == 0):
            error_dialog = QErrorMessage(self)
            error_dialog.showMessage('No existen libros con estos parametros')
            error_dialog.exec_()
        else:
            for libro in libros:
                item = QtGui.QStandardItem(libro)
                self.modelSugerencias.appendRow(item)
            self.ui.pbAdd.setEnabled(True)
            self.ui.pbRemove.setEnabled(True)

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
    
    def llenarListas(self):
        if self.modelSugerencias.rowCount()>0:
            self.modelSugerencias.removeRows(0,self.modelSugerencias.rowCount())
        percent = int(self.ui.spnPorcentaje.value())
        estado = "_"
        if (self.ui.chkNuevo.isChecked() and (not self.ui.chkUsado.isChecked())):
            estado="nuevo"
        elif ((not self.ui.chkNuevo.isChecked()) and self.ui.chkUsado.isChecked()):
            estado="usado"

        libros, combinaciones = final.regla3(prologa,estado,percent)
        if(len(libros) == 0):
            error_dialog = QErrorMessage(self)
            error_dialog.showMessage('No existen libros con estos parametros')
            error_dialog.exec_()
        else:
            for libro in libros:
                item = QtGui.QStandardItem(libro)
                self.modelSugerencias.appendRow(item)
            self.ui.pbAdd.setEnabled(True)
            self.ui.pbRemove.setEnabled(True)


class WinRegla4(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Regla4.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pbAdd.setDisabled(True)
        self.ui.pbRemove.setDisabled(True)
        self.ui.pbBuscar.clicked.connect(self.llenarListas)
        self.modelSugerencias = QtGui.QStandardItemModel()
        self.ui.listSugerencias.setModel(self.modelSugerencias)
    
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
            for libro in libros:
                item = QtGui.QStandardItem(libro)
                self.modelSugerencias.appendRow(item)
            self.ui.pbAdd.setEnabled(True)
            self.ui.pbRemove.setEnabled(True)

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
    
    def llenarListas(self):
        if self.modelSugerencias.rowCount()>0:
            self.modelSugerencias.removeRows(0,self.modelSugerencias.rowCount())
        categoria = self.ui.cbxCategoria.currentText()
        rating = self.ui.spnRating.value()
        fecha = self.ui.dateAntesDe.date()
        dias = fecha.day()
        meses = fecha.month()
        anio = fecha.year()
        fechapl = "date("+str(anio)+","+str(meses)+","+str(dias)+")"
        
        libros, combinaciones = final.regla5(prologa,categoria,rating,fechapl)
        if(len(libros) == 0):
            error_dialog = QErrorMessage(self)
            error_dialog.showMessage('No existen libros con estos parametros')
            error_dialog.exec_()
        else:
            for libro in libros:
                item = QtGui.QStandardItem(libro)
                self.modelSugerencias.appendRow(item)
            self.ui.pbAdd.setEnabled(True)
            self.ui.pbRemove.setEnabled(True)
        

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
    
    def llenarListas(self):
        if self.modelSugerencias.rowCount()>0:
            self.modelSugerencias.removeRows(0,self.modelSugerencias.rowCount())
        libros, combinaciones = final.regla6(prologa,self.ui.cbxCondicion.currentText(),self.ui.spnCosto.value())
        if(len(libros) == 0):
            error_dialog = QErrorMessage(self)
            error_dialog.showMessage('No existen libros con estos parametros')
            error_dialog.exec_()
        else:
            for libro in libros:
                item = QtGui.QStandardItem(libro)
                self.modelSugerencias.appendRow(item)
            self.ui.pbAdd.setEnabled(True)
            self.ui.pbRemove.setEnabled(True)

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
            for libro in libros:
                item = QtGui.QStandardItem(libro)
                self.modelSugerencias.appendRow(item)
            self.ui.pbAdd.setEnabled(True)
            self.ui.pbRemove.setEnabled(True)

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
            for libro in libros:
                item = QtGui.QStandardItem(libro)
                self.modelSugerencias.appendRow(item)
            self.ui.pbAdd.setEnabled(True)
            self.ui.pbRemove.setEnabled(True)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.getComprados
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
