# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ikinci.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(387, 191)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        Dialog.setFont(font)
        Dialog.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 0, 0);")
        self.BtnKayit2 = QtWidgets.QPushButton(Dialog)
        self.BtnKayit2.setGeometry(QtCore.QRect(70, 110, 241, 61))
        self.BtnKayit2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.BtnKayit2.setObjectName("BtnKayit2")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(90, 30, 201, 51))
        self.comboBox.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.comboBox.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.comboBox.setAcceptDrops(True)
        self.comboBox.setToolTipDuration(-1)
        self.comboBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"alternate-background-color: rgb(0, 170, 255);")
        self.comboBox.setEditable(False)
        self.comboBox.setDuplicatesEnabled(False)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "HOSFACE"))
        self.BtnKayit2.setText(_translate("Dialog", "Get Sequence Number"))
        self.comboBox.setCurrentText(_translate("Dialog", "Dentist"))
        self.comboBox.setItemText(0, _translate("Dialog", "Dentist"))
        self.comboBox.setItemText(1, _translate("Dialog", "General Surgeon"))
        self.comboBox.setItemText(2, _translate("Dialog", "Dermotology"))
        self.comboBox.setItemText(3, _translate("Dialog", "Psychiatry"))
        self.comboBox.setItemText(4, _translate("Dialog", "Infectious Diseases"))