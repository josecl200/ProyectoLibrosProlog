import sys
from PyQt5.QtWidgets import  QDialog, QApplication, QMainWindow
from PantallaPincipal import Ui_MainWindow
import Regla1, Regla2, Regla3, Regla4, Regla5, Regla6, Regla7, Regla8
import final

class WinRegla1(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Regla1.Ui_Dialog()
        self.ui.setupUi(self)
        #self.show()    
class WinRegla2(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Regla2.Ui_Dialog()
        self.ui.setupUi(self)
class WinRegla3(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Regla3.Ui_Dialog()
        self.ui.setupUi(self)
class WinRegla4(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Regla4.Ui_Dialog()
        self.ui.setupUi(self)
class WinRegla5(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Regla5.Ui_Dialog()
        self.ui.setupUi(self)
class WinRegla6(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Regla6.Ui_Dialog()
        self.ui.setupUi(self)
class WinRegla7(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Regla7.Ui_Dialog()
        self.ui.setupUi(self)
class WinRegla8(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Regla8.Ui_Dialog()
        self.ui.setupUi(self)  

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #self.actionLibrosRecientesConEntradasExtraRegla1
        
        self.ui.actionLibrosRecientesConEntradasExtraRegla1.triggered.connect(lambda: self.on_clicked(WinRegla1))
        self.ui.actionLibrosDeFiccinDe4OMsEstrellasConEntradasExtrasY10DeDescuento.triggered.connect(lambda: self.on_clicked(WinRegla2))
        self.ui.actionRegla3.triggered.connect(lambda: self.on_clicked(WinRegla3))
        self.ui.actionRegla4.triggered.connect(lambda: self.on_clicked(WinRegla4))
        self.ui.actionRegla5.triggered.connect(lambda: self.on_clicked(WinRegla5))
        self.ui.actionLibrosQueCuestenMenosQueX.triggered.connect(lambda: self.on_clicked(WinRegla6))
        self.ui.actionLibrosDeUnRatingYUnAutorEnEspecifico.triggered.connect(lambda: self.on_clicked(WinRegla7))
        self.ui.actionLibrosDeUnAutorQueNoPasenDeXPrecioYHayanSalidoEnUnAoX.triggered.connect(lambda: self.on_clicked(WinRegla8))
        self.show()
    
    def on_clicked(self,dialog):
        self.win=dialog()
        self.win.show()

                                              

app = QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec_())
