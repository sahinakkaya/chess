# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Shogi_Promo.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(110, 54)
        self.gridLayout = QtWidgets.QGridLayout(Frame)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.Unpromotion = QtWidgets.QToolButton(Frame)
        self.Unpromotion.setIconSize(QtCore.QSize(48, 48))
        self.Unpromotion.setObjectName("Unpromotion")
        self.gridLayout.addWidget(self.Unpromotion, 0, 1, 1, 1)
        self.Promotion = QtWidgets.QToolButton(Frame)
        self.Promotion.setIconSize(QtCore.QSize(48, 48))
        self.Promotion.setObjectName("Promotion")
        self.gridLayout.addWidget(self.Promotion, 0, 0, 1, 1)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
