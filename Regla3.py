# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Regla3.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog.resize(646, 486)
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(True)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(460, 440, 171, 32))
        self.buttonBox.setLocale(QtCore.QLocale(QtCore.QLocale.Spanish, QtCore.QLocale.DominicanRepublic))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(400, 20, 101, 19))
        self.label_2.setObjectName("label_2")
        self.lblPresupuesto = QtWidgets.QLabel(Dialog)
        self.lblPresupuesto.setGeometry(QtCore.QRect(510, 20, 101, 19))
        self.lblPresupuesto.setText("")
        self.lblPresupuesto.setObjectName("lblPresupuesto")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 80, 616, 341))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.listSugerencias = QtWidgets.QListView(self.layoutWidget)
        self.listSugerencias.setObjectName("listSugerencias")
        self.horizontalLayout.addWidget(self.listSugerencias)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pbAdd = QtWidgets.QPushButton(self.layoutWidget)
        self.pbAdd.setObjectName("pbAdd")
        self.verticalLayout.addWidget(self.pbAdd)
        self.pbBuscar = QtWidgets.QPushButton(self.layoutWidget)
        self.pbBuscar.setObjectName("pbBuscar")
        self.verticalLayout.addWidget(self.pbBuscar)
        self.pbRemove = QtWidgets.QPushButton(self.layoutWidget)
        self.pbRemove.setObjectName("pbRemove")
        self.verticalLayout.addWidget(self.pbRemove)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.listCarrito = QtWidgets.QListView(self.layoutWidget)
        self.listCarrito.setObjectName("listCarrito")
        self.horizontalLayout.addWidget(self.listCarrito)
        self.layoutWidget1 = QtWidgets.QWidget(Dialog)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 20, 191, 34))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.spnPorcentaje = QtWidgets.QSpinBox(self.layoutWidget1)
        self.spnPorcentaje.setObjectName("spnPorcentaje")
        self.horizontalLayout_2.addWidget(self.spnPorcentaje)
        self.splitter = QtWidgets.QSplitter(Dialog)
        self.splitter.setGeometry(QtCore.QRect(270, 10, 88, 44))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.chkNuevo = QtWidgets.QCheckBox(self.splitter)
        self.chkNuevo.setObjectName("chkNuevo")
        self.chkUsado = QtWidgets.QCheckBox(self.splitter)
        self.chkUsado.setObjectName("chkUsado")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "X% de libros en más de una categoria"))
        self.label_2.setText(_translate("Dialog", "Presupuesto:"))
        self.pbAdd.setText(_translate("Dialog", ">>"))
        self.pbBuscar.setText(_translate("Dialog", "Buscar"))
        self.pbRemove.setText(_translate("Dialog", "<<"))
        self.label.setText(_translate("Dialog", "Porcentaje de libros"))
        self.chkNuevo.setText(_translate("Dialog", "Nuevo"))
        self.chkUsado.setText(_translate("Dialog", "Usado"))
