# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'options_menu.ui'
#
# Created by: PyQt6 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Options_Menu(object):
    def setupUi(self, Options_Menu):
        Options_Menu.setObjectName("Options_Menu")
        Options_Menu.resize(490, 400)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Options_Menu)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(Options_Menu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(Options_Menu)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox.setGeometry(QtCore.QRect(20, 40, 201, 101))
        self.groupBox.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.PG_ChessStyle = QtWidgets.QRadioButton(self.groupBox)
        self.PG_ChessStyle.setGeometry(QtCore.QRect(10, 40, 111, 19))
        self.PG_ChessStyle.setChecked(True)
        self.PG_ChessStyle.setObjectName("PG_ChessStyle")
        self.PG_ShogiStyle = QtWidgets.QRadioButton(self.groupBox)
        self.PG_ShogiStyle.setGeometry(QtCore.QRect(10, 70, 111, 19))
        self.PG_ShogiStyle.setObjectName("PG_ShogiStyle")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 150, 221, 151))
        self.groupBox_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.groupBox_3.setObjectName("groupBox_3")
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 30, 81, 111))
        self.groupBox_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.groupBox_4.setFlat(False)
        self.groupBox_4.setObjectName("groupBox_4")
        self.Coords_H19 = QtWidgets.QRadioButton(self.groupBox_4)
        self.Coords_H19.setGeometry(QtCore.QRect(10, 30, 61, 19))
        self.Coords_H19.setObjectName("Coords_H19")
        self.Coords_Hai = QtWidgets.QRadioButton(self.groupBox_4)
        self.Coords_Hai.setGeometry(QtCore.QRect(10, 60, 51, 19))
        self.Coords_Hai.setChecked(True)
        self.Coords_Hai.setObjectName("Coords_Hai")
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox_5.setGeometry(QtCore.QRect(100, 30, 111, 111))
        self.groupBox_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.groupBox_5.setFlat(False)
        self.groupBox_5.setObjectName("groupBox_5")
        self.Coords_Vik = QtWidgets.QRadioButton(self.groupBox_5)
        self.Coords_Vik.setGeometry(QtCore.QRect(10, 60, 91, 41))
        self.Coords_Vik.setObjectName("Coords_Vik")
        self.Coords_V19 = QtWidgets.QRadioButton(self.groupBox_5)
        self.Coords_V19.setGeometry(QtCore.QRect(10, 30, 61, 19))
        self.Coords_V19.setChecked(True)
        self.Coords_V19.setObjectName("Coords_V19")
        self.horizontalLayout.addWidget(self.groupBox_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.board_preview = QtWidgets.QLabel(Options_Menu)
        self.board_preview.setText("")
        self.board_preview.setPixmap(QtGui.QPixmap("../resources/external-content.duckduckgo.png"))
        self.board_preview.setScaledContents(True)
        self.board_preview.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.board_preview.setObjectName("board_preview")
        self.verticalLayout.addWidget(self.board_preview)
        self.buttonPresets = QtWidgets.QPushButton(Options_Menu)
        self.buttonPresets.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.buttonPresets.setFont(font)
        self.buttonPresets.setObjectName("buttonPresets")
        self.verticalLayout.addWidget(self.buttonPresets)
        self.buttonReturn = QtWidgets.QPushButton(Options_Menu)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.buttonReturn.setFont(font)
        self.buttonReturn.setObjectName("buttonReturn")
        self.verticalLayout.addWidget(self.buttonReturn)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(Options_Menu)
        QtCore.QMetaObject.connectSlotsByName(Options_Menu)

    def retranslateUi(self, Options_Menu):
        _translate = QtCore.QCoreApplication.translate
        Options_Menu.setWindowTitle(_translate("Options_Menu", "Form"))
        self.label.setText(_translate("Options_Menu", "Options Menu"))
        self.groupBox_2.setTitle(_translate("Options_Menu", "Appearance"))
        self.groupBox.setTitle(_translate("Options_Menu", "Piece Graphics"))
        self.PG_ChessStyle.setText(_translate("Options_Menu", "Chess Style"))
        self.PG_ShogiStyle.setText(_translate("Options_Menu", "Shogi Style"))
        self.groupBox_3.setTitle(_translate("Options_Menu", "Coordinates"))
        self.groupBox_4.setTitle(_translate("Options_Menu", "Horizontal"))
        self.Coords_H19.setText(_translate("Options_Menu", "1 - 9"))
        self.Coords_Hai.setText(_translate("Options_Menu", "a - i"))
        self.groupBox_5.setTitle(_translate("Options_Menu", "Vertical"))
        self.Coords_Vik.setText(_translate("Options_Menu", "一  -   九"))
        self.Coords_V19.setText(_translate("Options_Menu", "1 - 9"))
        self.buttonPresets.setText(_translate("Options_Menu", "Gameplay Presets..."))
        self.buttonReturn.setText(_translate("Options_Menu", "Go Back"))