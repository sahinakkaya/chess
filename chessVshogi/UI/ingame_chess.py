# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ingame_chess.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(580, 418)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridWidget = QtWidgets.QWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gridWidget.sizePolicy().hasHeightForWidth())
        self.gridWidget.setSizePolicy(sizePolicy)
        self.gridWidget.setMinimumSize(QtCore.QSize(400, 400))
        self.gridWidget.setMaximumSize(QtCore.QSize(400, 400))
        self.gridWidget.setStyleSheet("background-color: rgb(127, 127, 127);")
        self.gridWidget.setObjectName("gridWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.Tile_47 = QtWidgets.QLabel(self.gridWidget)
        self.Tile_47.setStyleSheet("")
        self.Tile_47.setText("")
        self.Tile_47.setAlignment(QtCore.Qt.AlignCenter)
        self.Tile_47.setProperty("Piece", "")
        self.Tile_47.setObjectName("Tile_47")
        self.gridLayout.addWidget(self.Tile_47, 3, 6, 1, 1)
        self.Tile_48 = QtWidgets.QLabel(self.gridWidget)
        self.Tile_48.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Tile_48.setText("")
        self.Tile_48.setAlignment(QtCore.Qt.AlignCenter)
        self.Tile_48.setProperty("Piece", "")
        self.Tile_48.setObjectName("Tile_48")
        self.gridLayout.addWidget(self.Tile_48, 3, 7, 1, 1)
        self.Tile_25 = QtWidgets.QLabel(self.gridWidget)
        self.Tile_25.setStyleSheet("")
        self.Tile_25.setText("")
        self.Tile_25.setAlignment(QtCore.Qt.AlignCenter)
        self.Tile_25.setObjectName("Tile_25")
        self.gridLayout.addWidget(self.Tile_25, 1, 4, 1, 1)
        self.Tile_17 = QtWidgets.QLabel(self.gridWidget)
        self.Tile_17.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Tile_17.setText("")
        self.Tile_17.setAlignment(QtCore.Qt.AlignCenter)
        self.Tile_17.setObjectName("Tile_17")
        self.gridLayout.addWidget(self.Tile_17, 0, 6, 1, 1)
        self.Tile_45 = QtWidgets.QLabel(self.gridWidget)
        self.Tile_45.setStyleSheet("")
        self.Tile_45.setText("")
        self.Tile_45.setAlignment(QtCore.Qt.AlignCenter)
        self.Tile_45.setProperty("Piece", "")
        self.Tile_45.setObjectName("Tile_45")
        self.gridLayout.addWidget(self.Tile_45, 3, 4, 1, 1)
        self.Tile_32 = QtWidgets.QLabel(self.gridWidget)
        self.Tile_32.setStyleSheet("")
        self.Tile_32.setText("")
        self.Tile_32.setAlignment(QtCore.Qt.AlignCenter)
        self.Tile_32.setProperty("Piece", "")
        self.Tile_32.setObjectName("Tile_32")
        self.gridLayout.addWidget(self.Tile_32, 2, 1, 1, 1)
        self.Tile_88 = QtWidgets.QLabel(self.gridWidget)
        self.Tile_88.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Tile_88.setText("")
        self.Tile_88.setAlignment(QtCore.Qt.AlignCenter)
        self.Tile_88.setObjectName("Tile_88")
        self.gridLayout.addWidget(self.Tile_88, 7, 7, 1, 1)
        self.Tile_87 = QtWidgets.QLabel(self.gridWidget)
        self.Tile_87.setStyleSheet("")
        self.Tile_87.setText("")
        self.Tile_87.setAlignment(QtCore.Qt.AlignCenter)
        self.Tile_87.setObjectName("Tile_87")
        self.gridLayout.addWidget(self.Tile_87, 7, 6, 1, 1)
        self.Tile_84 = QtWidgets.QLabel(self.gridWidget)
        self.Tile_84.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Tile_84.setText("")
        self.Tile_84.setAlignment(QtCore.Qt.AlignCenter)
        self.Tile_84.setObjectName("Tile_84")
        self.gridLayout.addWidget(self.Tile_84, 7, 3, 1, 1)
        self.Tile_16 = QtWidgets.QLabel(self.gridWidget)
        self.Tile_16.setStyleSheet("")
        self.Tile_16.setText("")
        self.Tile_16.setAlignment(QtCore.Qt.AlignCenter)
        self.Tile_16.setObjectName("Tile_16")
        self.gridLayout.addWidget(self.Tile_16, 0, 5, 1, 1)
        self.Tile_81 = QtWidgets.QLabel(self.gridWidget)
        self.Tile_81.setStyleSheet("")
        self.Tile_81.setText("")
        self.Tile_81.setAlignment(QtCore.Qt.AlignCenter)
        self.Tile_81.setObjectName("Tile_81")
        self.gridLayout.addWidget(self.Tile_81, 7, 0, 1, 1)
        self.Tile_11 = QtWidgets.QLabel(self.gridWidget)
        self.Tile_11.setAutoFillBackground(False)
        self.Tile_11.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Tile_11.setText("")
        self.Tile_11.setAlignment(QtCore.Qt.AlignCenter)
        self.Tile_11.setObjectName("Tile_11")
        self.gridLayout.addWidget(self.Tile_11, 0, 0, 1, 1)
        self.Tile_68 = QtWidgets.QLabel(self.gridWidget)
        self.Tile_68.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Tile_68.setText("")
        self.Tile_68.setAlignment(QtCore.Qt.AlignCenter)
        self.Tile_68.setProperty("Piece", "")
        self.Tile_68.setObjectName("Tile_68")
        self.gridLayout.addWidget(self.Tile_68, 5, 7, 1, 1)
        self.Tile_85 = QtWidgets.QLabel(self.gridWidget)
        self.Tile_85.setStyleSheet("")
        self.Tile_85.setText("")
        self.Tile_85.setAlignment(QtCore.Qt.AlignCenter)
        self.Tile_85.setObjectName("Tile_85")
        self.gridLayout.addWidget(self.Tile_85, 7, 4, 1, 1)
        self.Tile_78 = QtWidgets.QLabel(self.gridWidget)
        self.Tile_78.setStyleSheet("")
        self.Tile_78.setText("")
        self.Tile_78.setAlignment(QtCore.Qt.AlignCenter)
        self.Tile_78.setObjectName("Tile_78")
        self.gridLayout.addWidget(self.Tile_78, 6, 7, 1, 1)
        self.Tile_82 = QtWidgets.QLabel(self.gridWidget)
        self.Tile_82.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Tile_82.setText("")
        self.Tile_82.setAlignment(QtCore.Qt.AlignCenter)
        self.Tile_82.setObjectName("Tile_82")
        self.gridLayout.addWidget(self.Tile_82, 7, 1, 1, 1)
        self.Tile_31 = QtWidgets.QLabel(self.gridWidget)
        self.Tile_31.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Tile_31.setText("")
        self.Tile_31.setAlignment(QtCore.Qt.AlignCenter)
        self.Tile_31.setProperty("Piece", "")
        self.Tile_31.setObjectName("Tile_31")
        self.gridLayout.addWidget(self.Tile_31, 2, 0, 1, 1)
        self.Tile_58 = QtWidgets.QLabel(self.gridWidget)
        self.Tile_58.setStyleSheet("")
        self.Tile_58.setText("")
        self.Tile_58.setAlignment(QtCore.Qt.AlignCenter)
        self.Tile_58.setProperty("Piece", "")
        self.Tile_58.setObjectName("Tile_58")
        self.gridLayout.addWidget(self.Tile_58, 4, 7, 1, 1)
        self.Tile_65 = QtWidgets.QLabel(self.gridWidget)
        self.Tile_65.setStyleSheet("")
        self.Tile_65.setText("")
        self.Tile_65.setAlignment(QtCore.Qt.AlignCenter)
        self.Tile_65.setProperty("Piece", "")
        self.Tile_65.setObjectName("Tile_65")
        self.gridLayout.addWidget(self.Tile_65, 5, 4, 1, 1)
        self.Tile_83 = QtWidgets.QLabel(self.gridWidget)
        self.Tile_83.setStyleSheet("")
        self.Tile_83.setText("")
        self.Tile_83.setAlignment(QtCore.Qt.AlignCenter)
        self.Tile_83.setObjectName("Tile_83")
        self.gridLayout.addWidget(self.Tile_83, 7, 2, 1, 1)
        self.Tile_72 = QtWidgets.QLabel(self.gridWidget)
        self.Tile_72.setStyleSheet("")
        self.Tile_72.setText("")
        self.Tile_72.setAlignment(QtCore.Qt.AlignCenter)
        self.Tile_72.setObjectName("Tile_72")
        self.gridLayout.addWidget(self.Tile_72, 6, 1, 1, 1)
        self.Tile_52 = QtWidgets.QLabel(self.gridWidget)
        self.Tile_52.setStyleSheet("")
        self.Tile_52.setText("")
        self.Tile_52.setAlignment(QtCore.Qt.AlignCenter)
        self.Tile_52.setProperty("Piece", "")
        self.Tile_52.setObjectName("Tile_52")
        self.gridLayout.addWidget(self.Tile_52, 4, 1, 1, 1)
        self.Tile_86 = QtWidgets.QLabel(self.gridWidget)
        self.Tile_86.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Tile_86.setText("")
        self.Tile_86.setAlignment(QtCore.Qt.AlignCenter)
        self.Tile_86.setObjectName("Tile_86")
        self.gridLayout.addWidget(self.Tile_86, 7, 5, 1, 1)
        self.Tile_75 = QtWidgets.QLabel(self.gridWidget)
        self.Tile_75.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Tile_75.setText("")
        self.Tile_75.setAlignment(QtCore.Qt.AlignCenter)
        self.Tile_75.setObjectName("Tile_75")
        self.gridLayout.addWidget(self.Tile_75, 6, 4, 1, 1)
        self.Tile_12 = QtWidgets.QLabel(self.gridWidget)
        self.Tile_12.setStyleSheet("")
        self.Tile_12.setText("")
        self.Tile_12.setAlignment(QtCore.Qt.AlignCenter)
        self.Tile_12.setObjectName("Tile_12")
        self.gridLayout.addWidget(self.Tile_12, 0, 1, 1, 1)
        self.Tile_62 = QtWidgets.QLabel(self.gridWidget)
        self.Tile_62.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Tile_62.setText("")
        self.Tile_62.setAlignment(QtCore.Qt.AlignCenter)
        self.Tile_62.setProperty("Piece", "")
        self.Tile_62.setObjectName("Tile_62")
        self.gridLayout.addWidget(self.Tile_62, 5, 1, 1, 1)
        self.Tile_67 = QtWidgets.QLabel(self.gridWidget)
        self.Tile_67.setStyleSheet("")
        self.Tile_67.setText("")
        self.Tile_67.setAlignment(QtCore.Qt.AlignCenter)
        self.Tile_67.setProperty("Piece", "")
        self.Tile_67.setObjectName("Tile_67")
        self.gridLayout.addWidget(self.Tile_67, 5, 6, 1, 1)
        self.Tile_77 = QtWidgets.QLabel(self.gridWidget)
        self.Tile_77.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Tile_77.setText("")
        self.Tile_77.setAlignment(QtCore.Qt.AlignCenter)
        self.Tile_77.setObjectName("Tile_77")
        self.gridLayout.addWidget(self.Tile_77, 6, 6, 1, 1)
        self.Tile_61 = QtWidgets.QLabel(self.gridWidget)
        self.Tile_61.setStyleSheet("")
        self.Tile_61.setText("")
        self.Tile_61.setAlignment(QtCore.Qt.AlignCenter)
        self.Tile_61.setProperty("Piece", "")
        self.Tile_61.setObjectName("Tile_61")
        self.gridLayout.addWidget(self.Tile_61, 5, 0, 1, 1)
        self.Tile_44 = QtWidgets.QLabel(self.gridWidget)
        self.Tile_44.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Tile_44.setText("")
        self.Tile_44.setAlignment(QtCore.Qt.AlignCenter)
        self.Tile_44.setProperty("Piece", "")
        self.Tile_44.setObjectName("Tile_44")
        self.gridLayout.addWidget(self.Tile_44, 3, 3, 1, 1)
        self.Tile_28 = QtWidgets.QLabel(self.gridWidget)
        self.Tile_28.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Tile_28.setText("")
        self.Tile_28.setAlignment(QtCore.Qt.AlignCenter)
        self.Tile_28.setObjectName("Tile_28")
        self.gridLayout.addWidget(self.Tile_28, 1, 7, 1, 1)
        self.Tile_21 = QtWidgets.QLabel(self.gridWidget)
        self.Tile_21.setStyleSheet("")
        self.Tile_21.setText("")
        self.Tile_21.setAlignment(QtCore.Qt.AlignCenter)
        self.Tile_21.setObjectName("Tile_21")
        self.gridLayout.addWidget(self.Tile_21, 1, 0, 1, 1)
        self.Tile_54 = QtWidgets.QLabel(self.gridWidget)
        self.Tile_54.setStyleSheet("")
        self.Tile_54.setText("")
        self.Tile_54.setAlignment(QtCore.Qt.AlignCenter)
        self.Tile_54.setProperty("Piece", "")
        self.Tile_54.setObjectName("Tile_54")
        self.gridLayout.addWidget(self.Tile_54, 4, 3, 1, 1)
        self.Tile_53 = QtWidgets.QLabel(self.gridWidget)
        self.Tile_53.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Tile_53.setText("")
        self.Tile_53.setAlignment(QtCore.Qt.AlignCenter)
        self.Tile_53.setProperty("Piece", "")
        self.Tile_53.setObjectName("Tile_53")
        self.gridLayout.addWidget(self.Tile_53, 4, 2, 1, 1)
        self.Tile_55 = QtWidgets.QLabel(self.gridWidget)
        self.Tile_55.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Tile_55.setText("")
        self.Tile_55.setAlignment(QtCore.Qt.AlignCenter)
        self.Tile_55.setProperty("Piece", "")
        self.Tile_55.setObjectName("Tile_55")
        self.gridLayout.addWidget(self.Tile_55, 4, 4, 1, 1)
        self.Tile_35 = QtWidgets.QLabel(self.gridWidget)
        self.Tile_35.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Tile_35.setText("")
        self.Tile_35.setAlignment(QtCore.Qt.AlignCenter)
        self.Tile_35.setProperty("Piece", "")
        self.Tile_35.setObjectName("Tile_35")
        self.gridLayout.addWidget(self.Tile_35, 2, 4, 1, 1)
        self.Tile_14 = QtWidgets.QLabel(self.gridWidget)
        self.Tile_14.setStyleSheet("")
        self.Tile_14.setText("")
        self.Tile_14.setAlignment(QtCore.Qt.AlignCenter)
        self.Tile_14.setObjectName("Tile_14")
        self.gridLayout.addWidget(self.Tile_14, 0, 3, 1, 1)
        self.Tile_51 = QtWidgets.QLabel(self.gridWidget)
        self.Tile_51.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Tile_51.setText("")
        self.Tile_51.setAlignment(QtCore.Qt.AlignCenter)
        self.Tile_51.setProperty("Piece", "")
        self.Tile_51.setObjectName("Tile_51")
        self.gridLayout.addWidget(self.Tile_51, 4, 0, 1, 1)
        self.Tile_64 = QtWidgets.QLabel(self.gridWidget)
        self.Tile_64.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Tile_64.setText("")
        self.Tile_64.setAlignment(QtCore.Qt.AlignCenter)
        self.Tile_64.setProperty("Piece", "")
        self.Tile_64.setObjectName("Tile_64")
        self.gridLayout.addWidget(self.Tile_64, 5, 3, 1, 1)
        self.Tile_73 = QtWidgets.QLabel(self.gridWidget)
        self.Tile_73.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Tile_73.setText("")
        self.Tile_73.setAlignment(QtCore.Qt.AlignCenter)
        self.Tile_73.setObjectName("Tile_73")
        self.gridLayout.addWidget(self.Tile_73, 6, 2, 1, 1)
        self.Tile_57 = QtWidgets.QLabel(self.gridWidget)
        self.Tile_57.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Tile_57.setText("")
        self.Tile_57.setAlignment(QtCore.Qt.AlignCenter)
        self.Tile_57.setProperty("Piece", "")
        self.Tile_57.setObjectName("Tile_57")
        self.gridLayout.addWidget(self.Tile_57, 4, 6, 1, 1)
        self.Tile_66 = QtWidgets.QLabel(self.gridWidget)
        self.Tile_66.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Tile_66.setText("")
        self.Tile_66.setAlignment(QtCore.Qt.AlignCenter)
        self.Tile_66.setProperty("Piece", "")
        self.Tile_66.setObjectName("Tile_66")
        self.gridLayout.addWidget(self.Tile_66, 5, 5, 1, 1)
        self.Tile_33 = QtWidgets.QLabel(self.gridWidget)
        self.Tile_33.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Tile_33.setText("")
        self.Tile_33.setAlignment(QtCore.Qt.AlignCenter)
        self.Tile_33.setProperty("Piece", "")
        self.Tile_33.setObjectName("Tile_33")
        self.gridLayout.addWidget(self.Tile_33, 2, 2, 1, 1)
        self.Tile_24 = QtWidgets.QLabel(self.gridWidget)
        self.Tile_24.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Tile_24.setText("")
        self.Tile_24.setAlignment(QtCore.Qt.AlignCenter)
        self.Tile_24.setObjectName("Tile_24")
        self.gridLayout.addWidget(self.Tile_24, 1, 3, 1, 1)
        self.Tile_27 = QtWidgets.QLabel(self.gridWidget)
        self.Tile_27.setStyleSheet("")
        self.Tile_27.setText("")
        self.Tile_27.setAlignment(QtCore.Qt.AlignCenter)
        self.Tile_27.setObjectName("Tile_27")
        self.gridLayout.addWidget(self.Tile_27, 1, 6, 1, 1)
        self.Tile_36 = QtWidgets.QLabel(self.gridWidget)
        self.Tile_36.setStyleSheet("")
        self.Tile_36.setText("")
        self.Tile_36.setAlignment(QtCore.Qt.AlignCenter)
        self.Tile_36.setProperty("Piece", "")
        self.Tile_36.setObjectName("Tile_36")
        self.gridLayout.addWidget(self.Tile_36, 2, 5, 1, 1)
        self.Tile_22 = QtWidgets.QLabel(self.gridWidget)
        self.Tile_22.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Tile_22.setText("")
        self.Tile_22.setAlignment(QtCore.Qt.AlignCenter)
        self.Tile_22.setObjectName("Tile_22")
        self.gridLayout.addWidget(self.Tile_22, 1, 1, 1, 1)
        self.Tile_63 = QtWidgets.QLabel(self.gridWidget)
        self.Tile_63.setStyleSheet("")
        self.Tile_63.setText("")
        self.Tile_63.setAlignment(QtCore.Qt.AlignCenter)
        self.Tile_63.setProperty("Piece", "")
        self.Tile_63.setObjectName("Tile_63")
        self.gridLayout.addWidget(self.Tile_63, 5, 2, 1, 1)
        self.Tile_76 = QtWidgets.QLabel(self.gridWidget)
        self.Tile_76.setStyleSheet("")
        self.Tile_76.setText("")
        self.Tile_76.setAlignment(QtCore.Qt.AlignCenter)
        self.Tile_76.setObjectName("Tile_76")
        self.gridLayout.addWidget(self.Tile_76, 6, 5, 1, 1)
        self.Tile_41 = QtWidgets.QLabel(self.gridWidget)
        self.Tile_41.setStyleSheet("")
        self.Tile_41.setText("")
        self.Tile_41.setAlignment(QtCore.Qt.AlignCenter)
        self.Tile_41.setProperty("Piece", "")
        self.Tile_41.setObjectName("Tile_41")
        self.gridLayout.addWidget(self.Tile_41, 3, 0, 1, 1)
        self.Tile_38 = QtWidgets.QLabel(self.gridWidget)
        self.Tile_38.setStyleSheet("")
        self.Tile_38.setText("")
        self.Tile_38.setAlignment(QtCore.Qt.AlignCenter)
        self.Tile_38.setProperty("Piece", "")
        self.Tile_38.setObjectName("Tile_38")
        self.gridLayout.addWidget(self.Tile_38, 2, 7, 1, 1)
        self.Tile_71 = QtWidgets.QLabel(self.gridWidget)
        self.Tile_71.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Tile_71.setText("")
        self.Tile_71.setAlignment(QtCore.Qt.AlignCenter)
        self.Tile_71.setObjectName("Tile_71")
        self.gridLayout.addWidget(self.Tile_71, 6, 0, 1, 1)
        self.Tile_15 = QtWidgets.QLabel(self.gridWidget)
        self.Tile_15.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Tile_15.setText("")
        self.Tile_15.setAlignment(QtCore.Qt.AlignCenter)
        self.Tile_15.setObjectName("Tile_15")
        self.gridLayout.addWidget(self.Tile_15, 0, 4, 1, 1)
        self.Tile_23 = QtWidgets.QLabel(self.gridWidget)
        self.Tile_23.setStyleSheet("")
        self.Tile_23.setText("")
        self.Tile_23.setAlignment(QtCore.Qt.AlignCenter)
        self.Tile_23.setObjectName("Tile_23")
        self.gridLayout.addWidget(self.Tile_23, 1, 2, 1, 1)
        self.Tile_34 = QtWidgets.QLabel(self.gridWidget)
        self.Tile_34.setStyleSheet("")
        self.Tile_34.setText("")
        self.Tile_34.setAlignment(QtCore.Qt.AlignCenter)
        self.Tile_34.setProperty("Piece", "")
        self.Tile_34.setObjectName("Tile_34")
        self.gridLayout.addWidget(self.Tile_34, 2, 3, 1, 1)
        self.Tile_13 = QtWidgets.QLabel(self.gridWidget)
        self.Tile_13.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Tile_13.setText("")
        self.Tile_13.setAlignment(QtCore.Qt.AlignCenter)
        self.Tile_13.setObjectName("Tile_13")
        self.gridLayout.addWidget(self.Tile_13, 0, 2, 1, 1)
        self.Tile_43 = QtWidgets.QLabel(self.gridWidget)
        self.Tile_43.setStyleSheet("")
        self.Tile_43.setText("")
        self.Tile_43.setAlignment(QtCore.Qt.AlignCenter)
        self.Tile_43.setProperty("Piece", "")
        self.Tile_43.setObjectName("Tile_43")
        self.gridLayout.addWidget(self.Tile_43, 3, 2, 1, 1)
        self.Tile_74 = QtWidgets.QLabel(self.gridWidget)
        self.Tile_74.setStyleSheet("")
        self.Tile_74.setText("")
        self.Tile_74.setAlignment(QtCore.Qt.AlignCenter)
        self.Tile_74.setObjectName("Tile_74")
        self.gridLayout.addWidget(self.Tile_74, 6, 3, 1, 1)
        self.Tile_37 = QtWidgets.QLabel(self.gridWidget)
        self.Tile_37.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Tile_37.setText("")
        self.Tile_37.setAlignment(QtCore.Qt.AlignCenter)
        self.Tile_37.setProperty("Piece", "")
        self.Tile_37.setObjectName("Tile_37")
        self.gridLayout.addWidget(self.Tile_37, 2, 6, 1, 1)
        self.Tile_56 = QtWidgets.QLabel(self.gridWidget)
        self.Tile_56.setStyleSheet("")
        self.Tile_56.setText("")
        self.Tile_56.setAlignment(QtCore.Qt.AlignCenter)
        self.Tile_56.setProperty("Piece", "")
        self.Tile_56.setObjectName("Tile_56")
        self.gridLayout.addWidget(self.Tile_56, 4, 5, 1, 1)
        self.Tile_26 = QtWidgets.QLabel(self.gridWidget)
        self.Tile_26.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Tile_26.setText("")
        self.Tile_26.setAlignment(QtCore.Qt.AlignCenter)
        self.Tile_26.setObjectName("Tile_26")
        self.gridLayout.addWidget(self.Tile_26, 1, 5, 1, 1)
        self.Tile_42 = QtWidgets.QLabel(self.gridWidget)
        self.Tile_42.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Tile_42.setText("")
        self.Tile_42.setAlignment(QtCore.Qt.AlignCenter)
        self.Tile_42.setProperty("Piece", "")
        self.Tile_42.setObjectName("Tile_42")
        self.gridLayout.addWidget(self.Tile_42, 3, 1, 1, 1)
        self.Tile_46 = QtWidgets.QLabel(self.gridWidget)
        self.Tile_46.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Tile_46.setText("")
        self.Tile_46.setAlignment(QtCore.Qt.AlignCenter)
        self.Tile_46.setProperty("Piece", "")
        self.Tile_46.setObjectName("Tile_46")
        self.gridLayout.addWidget(self.Tile_46, 3, 5, 1, 1)
        self.Tile_18 = QtWidgets.QLabel(self.gridWidget)
        self.Tile_18.setStyleSheet("")
        self.Tile_18.setText("")
        self.Tile_18.setAlignment(QtCore.Qt.AlignCenter)
        self.Tile_18.setObjectName("Tile_18")
        self.gridLayout.addWidget(self.Tile_18, 0, 7, 1, 1)
        self.horizontalLayout.addWidget(self.gridWidget)
        self.verticalFrame = QtWidgets.QFrame(Form)
        self.verticalFrame.setMinimumSize(QtCore.QSize(150, 0))
        self.verticalFrame.setMaximumSize(QtCore.QSize(250, 16777215))
        self.verticalFrame.setObjectName("verticalFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalFrame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.verticalFrame)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.timeEdit_2 = QtWidgets.QTimeEdit(self.verticalFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.timeEdit_2.sizePolicy().hasHeightForWidth())
        self.timeEdit_2.setSizePolicy(sizePolicy)
        self.timeEdit_2.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.timeEdit_2.setObjectName("timeEdit_2")
        self.verticalLayout.addWidget(self.timeEdit_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.verticalFrame)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.label_3 = QtWidgets.QLabel(self.verticalFrame)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.timeEdit = QtWidgets.QTimeEdit(self.verticalFrame)
        self.timeEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.timeEdit.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.timeEdit.setObjectName("timeEdit")
        self.verticalLayout.addWidget(self.timeEdit)
        self.horizontalLayout.addWidget(self.verticalFrame)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Tile_25.setProperty("Piece", _translate("Form", "C_BP"))
        self.Tile_17.setProperty("Piece", _translate("Form", "C_BN"))
        self.Tile_88.setProperty("Piece", _translate("Form", "C_WR"))
        self.Tile_87.setProperty("Piece", _translate("Form", "C_WN"))
        self.Tile_84.setProperty("Piece", _translate("Form", "C_WQ"))
        self.Tile_16.setProperty("Piece", _translate("Form", "C_BB"))
        self.Tile_81.setProperty("Piece", _translate("Form", "C_WR"))
        self.Tile_11.setProperty("Piece", _translate("Form", "C_BR"))
        self.Tile_85.setProperty("Piece", _translate("Form", "C_WK"))
        self.Tile_78.setProperty("Piece", _translate("Form", "C_WP"))
        self.Tile_82.setProperty("Piece", _translate("Form", "C_WN"))
        self.Tile_83.setProperty("Piece", _translate("Form", "C_WB"))
        self.Tile_72.setProperty("Piece", _translate("Form", "C_WP"))
        self.Tile_86.setProperty("Piece", _translate("Form", "C_WB"))
        self.Tile_75.setProperty("Piece", _translate("Form", "C_WP"))
        self.Tile_12.setProperty("Piece", _translate("Form", "C_BN"))
        self.Tile_77.setProperty("Piece", _translate("Form", "C_WP"))
        self.Tile_28.setProperty("Piece", _translate("Form", "C_BP"))
        self.Tile_21.setProperty("Piece", _translate("Form", "C_BP"))
        self.Tile_14.setProperty("Piece", _translate("Form", "C_BQ"))
        self.Tile_73.setProperty("Piece", _translate("Form", "C_WP"))
        self.Tile_24.setProperty("Piece", _translate("Form", "C_BP"))
        self.Tile_27.setProperty("Piece", _translate("Form", "C_BP"))
        self.Tile_22.setProperty("Piece", _translate("Form", "C_BP"))
        self.Tile_76.setProperty("Piece", _translate("Form", "C_WP"))
        self.Tile_71.setProperty("Piece", _translate("Form", "C_WP"))
        self.Tile_15.setProperty("Piece", _translate("Form", "C_BK"))
        self.Tile_23.setProperty("Piece", _translate("Form", "C_BP"))
        self.Tile_13.setProperty("Piece", _translate("Form", "C_BB"))
        self.Tile_74.setProperty("Piece", _translate("Form", "C_WP"))
        self.Tile_26.setProperty("Piece", _translate("Form", "C_BP"))
        self.Tile_18.setProperty("Piece", _translate("Form", "C_BR"))
        self.label_2.setText(_translate("Form", "TextLabel"))
        self.label.setText(_translate("Form", "TextLabel"))
        self.label_3.setText(_translate("Form", "TextLabel"))

import rsrc_rc
