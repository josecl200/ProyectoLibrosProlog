# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PantallaPincipal.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(545, 490)
        MainWindow.setAcceptDrops(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setEnabled(True)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 521, 431))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.listaComprados = QtWidgets.QListView(self.groupBox)
        self.listaComprados.setGeometry(QtCore.QRect(10, 50, 256, 361))
        self.listaComprados.setObjectName("listaComprados")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 20, 231, 16))
        self.label.setObjectName("label")
        self.verticalScrollBar = QtWidgets.QScrollBar(self.groupBox)
        self.verticalScrollBar.setGeometry(QtCore.QRect(240, 60, 20, 341))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(290, 20, 111, 16))
        self.label_2.setObjectName("label_2")
        self.txtFondos = QtWidgets.QTextEdit(self.groupBox)
        self.txtFondos.setGeometry(QtCore.QRect(290, 50, 221, 31))
        self.txtFondos.setObjectName("txtFondos")
        self.pbFondos = QtWidgets.QPushButton(self.groupBox)
        self.pbFondos.setGeometry(QtCore.QRect(290, 90, 221, 31))
        self.pbFondos.setObjectName("pbFondos")
        self.pbExit = QtWidgets.QPushButton(self.groupBox)
        self.pbExit.setGeometry(QtCore.QRect(310, 340, 171, 61))
        self.pbExit.setObjectName("pbExit")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(290, 140, 141, 19))
        self.label_3.setObjectName("label_3")
        self.txtEntradas = QtWidgets.QTextEdit(self.groupBox)
        self.txtEntradas.setGeometry(QtCore.QRect(290, 170, 221, 31))
        self.txtEntradas.setObjectName("txtEntradas")
        self.pbBonos = QtWidgets.QPushButton(self.groupBox)
        self.pbBonos.setGeometry(QtCore.QRect(290, 210, 221, 31))
        self.pbBonos.setObjectName("pbBonos")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(270, 280, 101, 19))
        self.label_4.setObjectName("label_4")
        self.lblFondosTotales = QtWidgets.QLabel(self.groupBox)
        self.lblFondosTotales.setGeometry(QtCore.QRect(400, 280, 67, 19))
        self.lblFondosTotales.setText("")
        self.lblFondosTotales.setObjectName("lblFondosTotales")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 545, 24))
        self.menubar.setObjectName("menubar")
        self.menuConsultasPredeterminadas = QtWidgets.QMenu(self.menubar)
        self.menuConsultasPredeterminadas.setObjectName("menuConsultasPredeterminadas")
        self.menuConsultasNuevas = QtWidgets.QMenu(self.menubar)
        self.menuConsultasNuevas.setObjectName("menuConsultasNuevas")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionLibrosRecientesConEntradasExtraRegla1 = QtWidgets.QAction(MainWindow)
        self.actionLibrosRecientesConEntradasExtraRegla1.setObjectName("actionLibrosRecientesConEntradasExtraRegla1")
        self.actionLibrosDeFiccinDe4OMsEstrellasConEntradasExtrasY10DeDescuento = QtWidgets.QAction(MainWindow)
        self.actionLibrosDeFiccinDe4OMsEstrellasConEntradasExtrasY10DeDescuento.setObjectName("actionLibrosDeFiccinDe4OMsEstrellasConEntradasExtrasY10DeDescuento")
        self.actionRegla3 = QtWidgets.QAction(MainWindow)
        self.actionRegla3.setObjectName("actionRegla3")
        self.actionRegla4 = QtWidgets.QAction(MainWindow)
        self.actionRegla4.setObjectName("actionRegla4")
        self.actionRegla5 = QtWidgets.QAction(MainWindow)
        self.actionRegla5.setObjectName("actionRegla5")
        self.actionLibrosQueCuestenMenosQueX = QtWidgets.QAction(MainWindow)
        self.actionLibrosQueCuestenMenosQueX.setObjectName("actionLibrosQueCuestenMenosQueX")
        self.actionLibrosDeUnRatingYUnAutorEnEspecifico = QtWidgets.QAction(MainWindow)
        self.actionLibrosDeUnRatingYUnAutorEnEspecifico.setObjectName("actionLibrosDeUnRatingYUnAutorEnEspecifico")
        self.actionLibrosDeUnAutorQueNoPasenDeXPrecioYHayanSalidoEnUnAoX = QtWidgets.QAction(MainWindow)
        self.actionLibrosDeUnAutorQueNoPasenDeXPrecioYHayanSalidoEnUnAoX.setObjectName("actionLibrosDeUnAutorQueNoPasenDeXPrecioYHayanSalidoEnUnAoX")
        self.menuConsultasPredeterminadas.addAction(self.actionLibrosRecientesConEntradasExtraRegla1)
        self.menuConsultasPredeterminadas.addAction(self.actionLibrosDeFiccinDe4OMsEstrellasConEntradasExtrasY10DeDescuento)
        self.menuConsultasPredeterminadas.addAction(self.actionRegla3)
        self.menuConsultasPredeterminadas.addAction(self.actionRegla4)
        self.menuConsultasPredeterminadas.addAction(self.actionRegla5)
        self.menuConsultasNuevas.addAction(self.actionLibrosQueCuestenMenosQueX)
        self.menuConsultasNuevas.addAction(self.actionLibrosDeUnRatingYUnAutorEnEspecifico)
        self.menuConsultasNuevas.addAction(self.actionLibrosDeUnAutorQueNoPasenDeXPrecioYHayanSalidoEnUnAoX)
        self.menubar.addAction(self.menuConsultasPredeterminadas.menuAction())
        self.menubar.addAction(self.menuConsultasNuevas.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Bookeeper"))
        self.label.setText(_translate("MainWindow", "Libros Comprados Recientemente"))
        self.label_2.setText(_translate("MainWindow", "Fondos Actuales"))
        self.pbFondos.setText(_translate("MainWindow", "Ingresar Fondos"))
        self.pbExit.setText(_translate("MainWindow", "Salir"))
        self.label_3.setText(_translate("MainWindow", "Entradas adicionales"))
        self.pbBonos.setText(_translate("MainWindow", "Bonos"))
        self.label_4.setText(_translate("MainWindow", "Fondos totales"))
        self.menuConsultasPredeterminadas.setTitle(_translate("MainWindow", "Consultas Predeterminadas"))
        self.menuConsultasNuevas.setTitle(_translate("MainWindow", "Consultas nuevas"))
        self.actionLibrosRecientesConEntradasExtraRegla1.setText(_translate("MainWindow", "Libros recientes con entradas extra (Regla #1)"))
        self.actionLibrosDeFiccinDe4OMsEstrellasConEntradasExtrasY10DeDescuento.setText(_translate("MainWindow", "Regla #2"))
        self.actionRegla3.setText(_translate("MainWindow", "Regla #3"))
        self.actionRegla4.setText(_translate("MainWindow", "Regla #4"))
        self.actionRegla5.setText(_translate("MainWindow", "Regla #5"))
        self.actionLibrosQueCuestenMenosQueX.setText(_translate("MainWindow", "Libros que cuesten menos que X"))
        self.actionLibrosDeUnRatingYUnAutorEnEspecifico.setText(_translate("MainWindow", "Libros de un rating y un autor en especifico"))
        self.actionLibrosDeUnAutorQueNoPasenDeXPrecioYHayanSalidoEnUnAoX.setText(_translate("MainWindow", "Libros de un autor que no pasen de X precio y hayan salido en un año X"))
