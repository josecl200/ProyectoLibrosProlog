import sys
from PyQt5.QtWidgets import  QDialog, QApplication, QMainWindow, QListWidgetItem, QListWidget
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
        self.ui.pbBuscar.clicked.connect()
    
    



class WinRegla2(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Regla2.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pbAdd.setDisabled(True)
        self.ui.pbRemove.setDisabled(True)        
        self.ui.cbxCategoria.addItems(final.getCategories(prologa))
        self.ui.lblPresupuesto.setText(str(final.getClavo(prologa)))

class WinRegla3(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Regla3.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pbAdd.setDisabled(True)
        self.ui.pbRemove.setDisabled(True)
        self.ui.lblPresupuesto.setText(str(final.getClavo(prologa) + final.getSalary(prologa)))


class WinRegla4(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Regla4.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pbAdd.setDisabled(True)
        self.ui.pbRemove.setDisabled(True)

class WinRegla5(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Regla5.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pbAdd.setDisabled(True)
        self.ui.pbRemove.setDisabled(True)
        self.ui.cbxCategoria.addItems(final.getCategories(prologa))
        

class WinRegla6(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Regla6.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pbAdd.setDisabled(True)
        self.ui.pbRemove.setDisabled(True)

class WinRegla7(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Regla7.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pbAdd.setDisabled(True)
        self.ui.pbRemove.setDisabled(True)

class WinRegla8(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Regla8.Ui_Dialog()
        self.ui.setupUi(self)  
        self.ui.pbAdd.setDisabled(True)
        self.ui.pbRemove.setDisabled(True)

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
