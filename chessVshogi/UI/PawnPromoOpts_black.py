# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PawnPromoOpts_black.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(220, 54)
        self.gridLayout = QtWidgets.QGridLayout(Frame)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.toolButton = QtWidgets.QToolButton(Frame)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Chess/resources/chess_48/Chess_rdt48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(48, 48))
        self.toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.toolButton.setArrowType(QtCore.Qt.NoArrow)
        self.toolButton.setObjectName("toolButton")
        self.gridLayout.addWidget(self.toolButton, 0, 0, 1, 1)
        self.toolButton_4 = QtWidgets.QToolButton(Frame)
        self.toolButton_4.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Chess/resources/chess_48/Chess_ndt48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_4.setIcon(icon1)
        self.toolButton_4.setIconSize(QtCore.QSize(48, 48))
        self.toolButton_4.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.toolButton_4.setArrowType(QtCore.Qt.NoArrow)
        self.toolButton_4.setObjectName("toolButton_4")
        self.gridLayout.addWidget(self.toolButton_4, 0, 1, 1, 1)
        self.toolButton_2 = QtWidgets.QToolButton(Frame)
        self.toolButton_2.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Chess/resources/chess_48/Chess_bdt48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_2.setIcon(icon2)
        self.toolButton_2.setIconSize(QtCore.QSize(48, 48))
        self.toolButton_2.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.toolButton_2.setArrowType(QtCore.Qt.NoArrow)
        self.toolButton_2.setObjectName("toolButton_2")
        self.gridLayout.addWidget(self.toolButton_2, 0, 2, 1, 1)
        self.toolButton_3 = QtWidgets.QToolButton(Frame)
        self.toolButton_3.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/Chess/resources/chess_48/Chess_qdt48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_3.setIcon(icon3)
        self.toolButton_3.setIconSize(QtCore.QSize(48, 48))
        self.toolButton_3.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.toolButton_3.setArrowType(QtCore.Qt.NoArrow)
        self.toolButton_3.setObjectName("toolButton_3")
        self.gridLayout.addWidget(self.toolButton_3, 0, 3, 1, 1)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
import rsrc_rc
