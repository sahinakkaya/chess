# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gamemode_menu.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
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
        self.pushButton_chess = QtWidgets.QPushButton(Gamemode_Menu)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_chess.setFont(font)
        self.pushButton_chess.setObjectName("pushButton_chess")
        self.horizontalLayout.addWidget(self.pushButton_chess)
        self.pushButton_shogi = QtWidgets.QPushButton(Gamemode_Menu)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_shogi.setFont(font)
        self.pushButton_shogi.setObjectName("pushButton_shogi")
        self.horizontalLayout.addWidget(self.pushButton_shogi)
        self.pushButton_hybrid = QtWidgets.QPushButton(Gamemode_Menu)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_hybrid.setFont(font)
        self.pushButton_hybrid.setObjectName("pushButton_hybrid")
        self.horizontalLayout.addWidget(self.pushButton_hybrid)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_custom = QtWidgets.QPushButton(Gamemode_Menu)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_custom.setFont(font)
        self.pushButton_custom.setObjectName("pushButton_custom")
        self.horizontalLayout_2.addWidget(self.pushButton_custom)
        self.pushButton_versus = QtWidgets.QPushButton(Gamemode_Menu)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_versus.setFont(font)
        self.pushButton_versus.setObjectName("pushButton_versus")
        self.horizontalLayout_2.addWidget(self.pushButton_versus)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Gamemode_Menu)
        QtCore.QMetaObject.connectSlotsByName(Gamemode_Menu)

    def retranslateUi(self, Gamemode_Menu):
        _translate = QtCore.QCoreApplication.translate
        Gamemode_Menu.setWindowTitle(_translate("Gamemode_Menu", "Form"))
        self.label.setText(_translate("Gamemode_Menu", "Choose a Game Mode"))
        self.pushButton_chess.setText(_translate("Gamemode_Menu", "Chess"))
        self.pushButton_shogi.setText(_translate("Gamemode_Menu", "Shogi"))
        self.pushButton_hybrid.setText(_translate("Gamemode_Menu", "Hybrid"))
        self.pushButton_custom.setText(_translate("Gamemode_Menu", "Custom"))
        self.pushButton_versus.setText(_translate("Gamemode_Menu", "Versus"))

