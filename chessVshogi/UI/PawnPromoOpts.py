# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PawnPromoOpts.ui'
#
# Created by: PyQt6 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(220, 54)
        self.gridLayout = QtWidgets.QGridLayout(Frame)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.Bishop = QtWidgets.QToolButton(Frame)
        self.Bishop.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Chess/resources/chess_48/Chess_blt48.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.Bishop.setIcon(icon)
        self.Bishop.setIconSize(QtCore.QSize(48, 48))
        self.Bishop.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonIconOnly)
        self.Bishop.setArrowType(QtCore.Qt.ArrowType.NoArrow)
        self.Bishop.setObjectName("Bishop")
        self.gridLayout.addWidget(self.Bishop, 0, 2, 1, 1)
        self.Queen = QtWidgets.QToolButton(Frame)
        self.Queen.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Chess/resources/chess_48/Chess_qlt48.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.Queen.setIcon(icon1)
        self.Queen.setIconSize(QtCore.QSize(48, 48))
        self.Queen.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonIconOnly)
        self.Queen.setArrowType(QtCore.Qt.ArrowType.NoArrow)
        self.Queen.setObjectName("Queen")
        self.gridLayout.addWidget(self.Queen, 0, 3, 1, 1)
        self.Rook = QtWidgets.QToolButton(Frame)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Chess/resources/chess_48/Chess_rlt48.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.Rook.setIcon(icon2)
        self.Rook.setIconSize(QtCore.QSize(48, 48))
        self.Rook.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonIconOnly)
        self.Rook.setArrowType(QtCore.Qt.ArrowType.NoArrow)
        self.Rook.setObjectName("Rook")
        self.gridLayout.addWidget(self.Rook, 0, 0, 1, 1)
        self.Knight = QtWidgets.QToolButton(Frame)
        self.Knight.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/Chess/resources/chess_48/Chess_nlt48.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.Knight.setIcon(icon3)
        self.Knight.setIconSize(QtCore.QSize(48, 48))
        self.Knight.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonIconOnly)
        self.Knight.setArrowType(QtCore.Qt.ArrowType.NoArrow)
        self.Knight.setObjectName("Knight")
        self.gridLayout.addWidget(self.Knight, 0, 1, 1, 1)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Promotion"))
import rsrc_rc
