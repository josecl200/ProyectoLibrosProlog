# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Regla5.ui'
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
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(540, 20, 101, 19))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 80, 616, 341))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.listSugerencias = QtWidgets.QTreeView(self.layoutWidget)
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
        self.listCarrito = QtWidgets.QTreeView(self.layoutWidget)
        self.listCarrito.setObjectName("listCarrito") 
        self.horizontalLayout.addWidget(self.listCarrito)
        self.layoutWidget1 = QtWidgets.QWidget(Dialog)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 10, 191, 30))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.spnRating = QtWidgets.QSpinBox(self.layoutWidget1)
        self.spnRating.setObjectName("spnRating")
        self.horizontalLayout_2.addWidget(self.spnRating)
        self.layoutWidget2 = QtWidgets.QWidget(Dialog)
        self.layoutWidget2.setGeometry(QtCore.QRect(20, 50, 201, 29))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.cbxCategoria = QtWidgets.QComboBox(self.layoutWidget2)
        self.cbxCategoria.setObjectName("cbxCategoria")
        self.horizontalLayout_3.addWidget(self.cbxCategoria)
        self.layoutWidget3 = QtWidgets.QWidget(Dialog)
        self.layoutWidget3.setGeometry(QtCore.QRect(230, 10, 161, 30))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.layoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.layoutWidget_2.setGeometry(QtCore.QRect(420, 10, 181, 31))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.linePresupuesto = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.linePresupuesto.setObjectName("linePresupuesto")
        self.horizontalLayout_5.addWidget(self.linePresupuesto)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Libros por Rating y Categoria"))
        self.pbAdd.setText(_translate("Dialog", ">>"))
        self.pbBuscar.setText(_translate("Dialog", "Buscar"))
        self.pbRemove.setText(_translate("Dialog", "<<"))
        self.label.setText(_translate("Dialog", "Rating"))
        self.label_4.setText(_translate("Dialog", "Categoria"))
        self.label_5.setText(_translate("Dialog", "Antes de:"))
        self.label_6.setText(_translate("Dialog", "Presupuesto:"))
