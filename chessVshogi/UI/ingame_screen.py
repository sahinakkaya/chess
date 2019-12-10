# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ingame_screen.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Ingame_screen(object):
    def setupUi(self, Ingame_screen):
        Ingame_screen.setObjectName("Ingame_screen")
        Ingame_screen.resize(477, 356)
        self.ingame = QtWidgets.QLabel(Ingame_screen)
        self.ingame.setGeometry(QtCore.QRect(10, 20, 308, 321))
        self.ingame.setText("")
        self.ingame.setPixmap(QtGui.QPixmap("../resources/in-game-initial.png"))
        self.ingame.setScaledContents(True)
        self.ingame.setObjectName("ingame")
        self.timeEdit = QtWidgets.QTimeEdit(Ingame_screen)
        self.timeEdit.setGeometry(QtCore.QRect(320, 130, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.timeEdit.setFont(font)
        self.timeEdit.setFrame(True)
        self.timeEdit.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.timeEdit.setObjectName("timeEdit")
        self.label_2 = QtWidgets.QLabel(Ingame_screen)
        self.label_2.setGeometry(QtCore.QRect(330, 170, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.timeEdit_2 = QtWidgets.QTimeEdit(Ingame_screen)
        self.timeEdit_2.setGeometry(QtCore.QRect(320, 210, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.timeEdit_2.setFont(font)
        self.timeEdit_2.setFrame(True)
        self.timeEdit_2.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.timeEdit_2.setObjectName("timeEdit_2")
        self.frame = QtWidgets.QFrame(Ingame_screen)
        self.frame.setGeometry(QtCore.QRect(320, 20, 151, 101))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(Ingame_screen)
        self.frame_2.setGeometry(QtCore.QRect(320, 250, 151, 101))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.timeEdit.raise_()
        self.label_2.raise_()
        self.timeEdit_2.raise_()
        self.frame.raise_()
        self.frame_2.raise_()
        self.ingame.raise_()

        self.retranslateUi(Ingame_screen)
        QtCore.QMetaObject.connectSlotsByName(Ingame_screen)

    def retranslateUi(self, Ingame_screen):
        _translate = QtCore.QCoreApplication.translate
        Ingame_screen.setWindowTitle(_translate("Ingame_screen", "Form"))
        self.label_2.setText(_translate("Ingame_screen", "Turn: White"))

