# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ilk.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.resize(1103, 513)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setMouseTracking(False)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.BKayit = QtWidgets.QPushButton(MainWindow)
        self.BKayit.setGeometry(QtCore.QRect(30, 430, 331, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.BKayit.setFont(font)
        self.BKayit.setStyleSheet(" background-color:rgb(255, 255, 255)")
        self.BKayit.setObjectName("BKayit")
        self.verticalLayoutWidget = QtWidgets.QWidget(MainWindow)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 70, 151, 331))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(1, 0, 1, 3)
        self.verticalLayout.setSpacing(18)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_4 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.horizontalLayoutWidget = QtWidgets.QWidget(MainWindow)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(180, 330, 221, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.LineDay = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.LineDay.setEnabled(True)
        self.LineDay.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.LineDay.setFont(font)
        self.LineDay.setToolTip("")
        self.LineDay.setToolTipDuration(-1)
        self.LineDay.setStatusTip("")
        self.LineDay.setWhatsThis("")
        self.LineDay.setStyleSheet(" background-color:rgb(255, 255, 255)")
        self.LineDay.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.LineDay.setInputMask("")
        self.LineDay.setText("")
        self.LineDay.setMaxLength(2)
        self.LineDay.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.LineDay.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.LineDay.setClearButtonEnabled(False)
        self.LineDay.setObjectName("LineDay")
        self.horizontalLayout.addWidget(self.LineDay)
        self.LineMounth = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.LineMounth.setFont(font)
        self.LineMounth.setStyleSheet(" background-color:rgb(255, 255, 255)")
        self.LineMounth.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.LineMounth.setMaxLength(2)
        self.LineMounth.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.LineMounth.setClearButtonEnabled(False)
        self.LineMounth.setObjectName("LineMounth")
        self.horizontalLayout.addWidget(self.LineMounth)
        self.LineYear = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.LineYear.setFont(font)
        self.LineYear.setStyleSheet(" background-color:rgb(255, 255, 255)")
        self.LineYear.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.LineYear.setMaxLength(4)
        self.LineYear.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.LineYear.setClearButtonEnabled(False)
        self.LineYear.setObjectName("LineYear")
        self.horizontalLayout.addWidget(self.LineYear)
        self.progressBar = QtWidgets.QProgressBar(MainWindow)
        self.progressBar.setGeometry(QtCore.QRect(20, 20, 361, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.progressBar.setFont(font)
        self.progressBar.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.progressBar.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);")
        self.progressBar.setMaximum(10)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName("progressBar")
        self.BKayit_2 = QtWidgets.QPushButton(MainWindow)
        self.BKayit_2.setGeometry(QtCore.QRect(450, 10, 591, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.BKayit_2.setFont(font)
        self.BKayit_2.setStyleSheet(" background-color:rgb(255, 255, 255)")
        self.BKayit_2.setObjectName("BKayit_2")
        self.LineTc = QtWidgets.QLineEdit(MainWindow)
        self.LineTc.setEnabled(True)
        self.LineTc.setGeometry(QtCore.QRect(180, 100, 219, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.LineTc.setFont(font)
        self.LineTc.setStyleSheet(" background-color:rgb(255, 255, 255)")
        self.LineTc.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.LineTc.setText("")
        self.LineTc.setMaxLength(11)
        self.LineTc.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.LineTc.setCursorPosition(0)
        self.LineTc.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.LineTc.setDragEnabled(False)
        self.LineTc.setReadOnly(False)
        self.LineTc.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.LineTc.setClearButtonEnabled(False)
        self.LineTc.setObjectName("LineTc")
        self.LineAd = QtWidgets.QLineEdit(MainWindow)
        self.LineAd.setGeometry(QtCore.QRect(180, 180, 219, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.LineAd.setFont(font)
        self.LineAd.setStyleSheet(" background-color:rgb(255, 255, 255)")
        self.LineAd.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.LineAd.setClearButtonEnabled(False)
        self.LineAd.setObjectName("LineAd")
        self.LineSoyad = QtWidgets.QLineEdit(MainWindow)
        self.LineSoyad.setGeometry(QtCore.QRect(180, 260, 219, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.LineSoyad.setFont(font)
        self.LineSoyad.setStyleSheet(" background-color:rgb(255, 255, 255)")
        self.LineSoyad.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.LineSoyad.setClearButtonEnabled(False)
        self.LineSoyad.setObjectName("LineSoyad")
        self.label = QtWidgets.QLabel(MainWindow)
        self.label.setGeometry(QtCore.QRect(440, 60, 621, 431))
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label.setText("")
        self.label.setObjectName("label")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "HOSFACE"))
        self.BKayit.setText(_translate("MainWindow", "Patient Registration"))
        self.pushButton_2.setText(_translate("MainWindow", "TC"))
        self.pushButton_4.setText(_translate("MainWindow", "NAME"))
        self.pushButton_3.setText(_translate("MainWindow", "SURNAME"))
        self.pushButton.setText(_translate("MainWindow", "DATE OF BIRTH"))
        self.LineDay.setPlaceholderText(_translate("MainWindow", "Day-gg"))
        self.LineMounth.setPlaceholderText(_translate("MainWindow", "Mount-aa"))
        self.LineYear.setPlaceholderText(_translate("MainWindow", "Year-Y"))
        self.BKayit_2.setText(_translate("MainWindow", "Camera"))
        self.LineTc.setPlaceholderText(_translate("MainWindow", "Only Numbers"))
        self.LineAd.setPlaceholderText(_translate("MainWindow", "Your Name"))
        self.LineSoyad.setPlaceholderText(_translate("MainWindow", "Your Surname"))
