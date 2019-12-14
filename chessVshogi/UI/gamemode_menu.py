# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gamemode_menu.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Gamemode_Menu(object):
    def setupUi(self, Gamemode_Menu):
        Gamemode_Menu.setObjectName("Gamemode_Menu")
        Gamemode_Menu.resize(462, 286)
        self.verticalLayout = QtWidgets.QVBoxLayout(Gamemode_Menu)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Gamemode_Menu)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.buttonChess = QtWidgets.QPushButton(Gamemode_Menu)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.buttonChess.setFont(font)
        self.buttonChess.setObjectName("buttonChess")
        self.horizontalLayout.addWidget(self.buttonChess)
        self.buttonShogi = QtWidgets.QPushButton(Gamemode_Menu)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.buttonShogi.setFont(font)
        self.buttonShogi.setObjectName("buttonShogi")
        self.horizontalLayout.addWidget(self.buttonShogi)
        self.buttonHybrid = QtWidgets.QPushButton(Gamemode_Menu)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.buttonHybrid.setFont(font)
        self.buttonHybrid.setObjectName("buttonHybrid")
        self.horizontalLayout.addWidget(self.buttonHybrid)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.buttonCustom = QtWidgets.QPushButton(Gamemode_Menu)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.buttonCustom.setFont(font)
        self.buttonCustom.setObjectName("buttonCustom")
        self.horizontalLayout_2.addWidget(self.buttonCustom)
        self.buttonVersus = QtWidgets.QPushButton(Gamemode_Menu)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.buttonVersus.setFont(font)
        self.buttonVersus.setObjectName("buttonVersus")
        self.horizontalLayout_2.addWidget(self.buttonVersus)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Gamemode_Menu)
        QtCore.QMetaObject.connectSlotsByName(Gamemode_Menu)

    def retranslateUi(self, Gamemode_Menu):
        _translate = QtCore.QCoreApplication.translate
        Gamemode_Menu.setWindowTitle(_translate("Gamemode_Menu", "Form"))
        self.label.setText(_translate("Gamemode_Menu", "Choose a Game Mode"))
        self.buttonChess.setText(_translate("Gamemode_Menu", "Chess"))
        self.buttonShogi.setText(_translate("Gamemode_Menu", "Shogi"))
        self.buttonHybrid.setText(_translate("Gamemode_Menu", "Hybrid"))
        self.buttonCustom.setText(_translate("Gamemode_Menu", "Custom"))
        self.buttonVersus.setText(_translate("Gamemode_Menu", "Versus"))
