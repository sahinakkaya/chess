# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(352, 294)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButtonChess = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButtonChess.setFont(font)
        self.pushButtonChess.setObjectName("pushButtonChess")
        self.horizontalLayout.addWidget(self.pushButtonChess)
        self.pushButton_hybrid = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_hybrid.setFont(font)
        self.pushButton_hybrid.setObjectName("pushButton_hybrid")
        self.horizontalLayout.addWidget(self.pushButton_hybrid)
        self.pushButton_shogi = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_shogi.setFont(font)
        self.pushButton_shogi.setObjectName("pushButton_shogi")
        self.horizontalLayout.addWidget(self.pushButton_shogi)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_custom = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_custom.setFont(font)
        self.pushButton_custom.setObjectName("pushButton_custom")
        self.horizontalLayout_2.addWidget(self.pushButton_custom)
        self.pushButton_versus = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_versus.setFont(font)
        self.pushButton_versus.setObjectName("pushButton_versus")
        self.horizontalLayout_2.addWidget(self.pushButton_versus)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Choose a Game Mode"))
        self.pushButtonChess.setText(_translate("Form", "Chess"))
        self.pushButton_hybrid.setText(_translate("Form", "Hybrid"))
        self.pushButton_shogi.setText(_translate("Form", "Shogi"))
        self.pushButton_custom.setText(_translate("Form", "Custom"))
        self.pushButton_versus.setText(_translate("Form", "Versus"))

