# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'custom_game_1.ui'
#
# Created by: PyQt6 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Custom_Game_1(object):
    def setupUi(self, Custom_Game_1):
        Custom_Game_1.setObjectName("Custom_Game_1")
        Custom_Game_1.resize(673, 469)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(Custom_Game_1)
        self.verticalLayout_7.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label = QtWidgets.QLabel(Custom_Game_1)
        self.label.setMinimumSize(QtCore.QSize(641, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_7.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.GrpGameOpts = QtWidgets.QGroupBox(Custom_Game_1)
        self.GrpGameOpts.setMaximumSize(QtCore.QSize(202, 392))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.GrpGameOpts.setFont(font)
        self.GrpGameOpts.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.GrpGameOpts.setFlat(False)
        self.GrpGameOpts.setObjectName("GrpGameOpts")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.GrpGameOpts)
        self.verticalLayout_3.setContentsMargins(9, 6, 9, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.BoardOpts = QtWidgets.QGroupBox(self.GrpGameOpts)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.BoardOpts.setFont(font)
        self.BoardOpts.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.BoardOpts.setFlat(False)
        self.BoardOpts.setObjectName("BoardOpts")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.BoardOpts)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Board_8x8 = QtWidgets.QRadioButton(self.BoardOpts)
        self.Board_8x8.setChecked(True)
        self.Board_8x8.setObjectName("Board_8x8")
        self.verticalLayout_2.addWidget(self.Board_8x8)
        self.Board_9x9 = QtWidgets.QRadioButton(self.BoardOpts)
        self.Board_9x9.setEnabled(False)
        self.Board_9x9.setObjectName("Board_9x9")
        self.verticalLayout_2.addWidget(self.Board_9x9)
        self.verticalLayout_3.addWidget(self.BoardOpts)
        self.e_promodrop = QtWidgets.QCheckBox(self.GrpGameOpts)
        self.e_promodrop.setEnabled(False)
        self.e_promodrop.setObjectName("e_promodrop")
        self.verticalLayout_3.addWidget(self.e_promodrop)
        self.e_menpassant = QtWidgets.QCheckBox(self.GrpGameOpts)
        self.e_menpassant.setEnabled(False)
        self.e_menpassant.setChecked(False)
        self.e_menpassant.setObjectName("e_menpassant")
        self.verticalLayout_3.addWidget(self.e_menpassant)
        self.e_mdoublemove = QtWidgets.QCheckBox(self.GrpGameOpts)
        self.e_mdoublemove.setEnabled(False)
        self.e_mdoublemove.setObjectName("e_mdoublemove")
        self.verticalLayout_3.addWidget(self.e_mdoublemove)
        self.CaptureOpts = QtWidgets.QGroupBox(self.GrpGameOpts)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.CaptureOpts.setFont(font)
        self.CaptureOpts.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.CaptureOpts.setFlat(False)
        self.CaptureOpts.setObjectName("CaptureOpts")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.CaptureOpts)
        self.verticalLayout.setContentsMargins(-1, -1, 0, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.c_crazyhouse = QtWidgets.QRadioButton(self.CaptureOpts)
        self.c_crazyhouse.setEnabled(False)
        self.c_crazyhouse.setChecked(False)
        self.c_crazyhouse.setObjectName("c_crazyhouse")
        self.verticalLayout.addWidget(self.c_crazyhouse)
        self.c_graveyard = QtWidgets.QRadioButton(self.CaptureOpts)
        self.c_graveyard.setChecked(True)
        self.c_graveyard.setObjectName("c_graveyard")
        self.verticalLayout.addWidget(self.c_graveyard)
        self.c_shogionly = QtWidgets.QRadioButton(self.CaptureOpts)
        self.c_shogionly.setEnabled(False)
        self.c_shogionly.setObjectName("c_shogionly")
        self.verticalLayout.addWidget(self.c_shogionly)
        self.verticalLayout_3.addWidget(self.CaptureOpts)
        self.horizontalLayout.addWidget(self.GrpGameOpts)
        self.verticalFrame = QtWidgets.QFrame(Custom_Game_1)
        self.verticalFrame.setMaximumSize(QtCore.QSize(253, 392))
        self.verticalFrame.setObjectName("verticalFrame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalFrame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.GrpPlayerOpts = QtWidgets.QGroupBox(self.verticalFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.GrpPlayerOpts.sizePolicy().hasHeightForWidth())
        self.GrpPlayerOpts.setSizePolicy(sizePolicy)
        self.GrpPlayerOpts.setMinimumSize(QtCore.QSize(251, 390))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.GrpPlayerOpts.setFont(font)
        self.GrpPlayerOpts.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.GrpPlayerOpts.setFlat(False)
        self.GrpPlayerOpts.setObjectName("GrpPlayerOpts")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.GrpPlayerOpts)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.P1Side = QtWidgets.QGroupBox(self.GrpPlayerOpts)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.P1Side.sizePolicy().hasHeightForWidth())
        self.P1Side.setSizePolicy(sizePolicy)
        self.P1Side.setMinimumSize(QtCore.QSize(0, 58))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.P1Side.setFont(font)
        self.P1Side.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.P1Side.setFlat(False)
        self.P1Side.setObjectName("P1Side")
        self.P1_Chess = QtWidgets.QRadioButton(self.P1Side)
        self.P1_Chess.setEnabled(False)
        self.P1_Chess.setGeometry(QtCore.QRect(10, 30, 71, 19))
        self.P1_Chess.setChecked(False)
        self.P1_Chess.setObjectName("P1_Chess")
        self.P1_Shogi = QtWidgets.QRadioButton(self.P1Side)
        self.P1_Shogi.setGeometry(QtCore.QRect(130, 30, 61, 19))
        self.P1_Shogi.setChecked(True)
        self.P1_Shogi.setObjectName("P1_Shogi")
        self.verticalLayout_5.addWidget(self.P1Side)
        self.Lineup = QtWidgets.QGroupBox(self.GrpPlayerOpts)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Lineup.sizePolicy().hasHeightForWidth())
        self.Lineup.setSizePolicy(sizePolicy)
        self.Lineup.setMinimumSize(QtCore.QSize(0, 151))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Lineup.setFont(font)
        self.Lineup.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Lineup.setFlat(False)
        self.Lineup.setObjectName("Lineup")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Lineup)
        self.horizontalLayout_2.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.L_Shogi = QtWidgets.QGroupBox(self.Lineup)
        self.L_Shogi.setMinimumSize(QtCore.QSize(101, 121))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.L_Shogi.setFont(font)
        self.L_Shogi.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.L_Shogi.setFlat(False)
        self.L_Shogi.setObjectName("L_Shogi")
        self.SL_Default = QtWidgets.QRadioButton(self.L_Shogi)
        self.SL_Default.setGeometry(QtCore.QRect(10, 30, 81, 19))
        self.SL_Default.setChecked(True)
        self.SL_Default.setObjectName("SL_Default")
        self.SL_Mirror = QtWidgets.QRadioButton(self.L_Shogi)
        self.SL_Mirror.setGeometry(QtCore.QRect(10, 60, 71, 19))
        self.SL_Mirror.setObjectName("SL_Mirror")
        self.SL_Outpost = QtWidgets.QRadioButton(self.L_Shogi)
        self.SL_Outpost.setEnabled(False)
        self.SL_Outpost.setGeometry(QtCore.QRect(10, 90, 81, 19))
        self.SL_Outpost.setObjectName("SL_Outpost")
        self.horizontalLayout_2.addWidget(self.L_Shogi)
        self.L_Chess = QtWidgets.QGroupBox(self.Lineup)
        self.L_Chess.setEnabled(False)
        self.L_Chess.setMinimumSize(QtCore.QSize(131, 121))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.L_Chess.setFont(font)
        self.L_Chess.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.L_Chess.setFlat(False)
        self.L_Chess.setObjectName("L_Chess")
        self.CL_Default = QtWidgets.QRadioButton(self.L_Chess)
        self.CL_Default.setGeometry(QtCore.QRect(10, 30, 121, 19))
        self.CL_Default.setChecked(True)
        self.CL_Default.setObjectName("CL_Default")
        self.CL_QDown = QtWidgets.QRadioButton(self.L_Chess)
        self.CL_QDown.setGeometry(QtCore.QRect(10, 60, 121, 19))
        self.CL_QDown.setObjectName("CL_QDown")
        self.CL_RKnight = QtWidgets.QRadioButton(self.L_Chess)
        self.CL_RKnight.setGeometry(QtCore.QRect(10, 90, 121, 19))
        self.CL_RKnight.setObjectName("CL_RKnight")
        self.horizontalLayout_2.addWidget(self.L_Chess)
        self.verticalLayout_5.addWidget(self.Lineup)
        self.GrpTimerOpts = QtWidgets.QGroupBox(self.GrpPlayerOpts)
        self.GrpTimerOpts.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.GrpTimerOpts.sizePolicy().hasHeightForWidth())
        self.GrpTimerOpts.setSizePolicy(sizePolicy)
        self.GrpTimerOpts.setMinimumSize(QtCore.QSize(0, 130))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.GrpTimerOpts.setFont(font)
        self.GrpTimerOpts.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.GrpTimerOpts.setFlat(False)
        self.GrpTimerOpts.setCheckable(True)
        self.GrpTimerOpts.setObjectName("GrpTimerOpts")
        self.gridLayout = QtWidgets.QGridLayout(self.GrpTimerOpts)
        self.gridLayout.setContentsMargins(9, -1, -1, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.checkByoyomi = QtWidgets.QCheckBox(self.GrpTimerOpts)
        self.checkByoyomi.setEnabled(False)
        self.checkByoyomi.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.checkByoyomi.setAutoRepeat(False)
        self.checkByoyomi.setObjectName("checkByoyomi")
        self.gridLayout.addWidget(self.checkByoyomi, 4, 0, 1, 1)
        self.checkIncrement = QtWidgets.QCheckBox(self.GrpTimerOpts)
        self.checkIncrement.setEnabled(False)
        self.checkIncrement.setObjectName("checkIncrement")
        self.gridLayout.addWidget(self.checkIncrement, 2, 0, 1, 1)
        self.timeDelay = QtWidgets.QTimeEdit(self.GrpTimerOpts)
        self.timeDelay.setFrame(True)
        self.timeDelay.setObjectName("timeDelay")
        self.gridLayout.addWidget(self.timeDelay, 3, 1, 1, 1)
        self.timeIncrement = QtWidgets.QTimeEdit(self.GrpTimerOpts)
        self.timeIncrement.setFrame(True)
        self.timeIncrement.setObjectName("timeIncrement")
        self.gridLayout.addWidget(self.timeIncrement, 2, 1, 1, 1)
        self.checkDelay = QtWidgets.QCheckBox(self.GrpTimerOpts)
        self.checkDelay.setEnabled(False)
        self.checkDelay.setObjectName("checkDelay")
        self.gridLayout.addWidget(self.checkDelay, 3, 0, 1, 1)
        self.timeByoyomi = QtWidgets.QTimeEdit(self.GrpTimerOpts)
        self.timeByoyomi.setFrame(True)
        self.timeByoyomi.setObjectName("timeByoyomi")
        self.gridLayout.addWidget(self.timeByoyomi, 4, 1, 1, 1)
        self.timeTimer = QtWidgets.QTimeEdit(self.GrpTimerOpts)
        self.timeTimer.setTime(QtCore.QTime(0, 10, 0))
        self.timeTimer.setObjectName("timeTimer")
        self.gridLayout.addWidget(self.timeTimer, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.GrpTimerOpts)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.verticalLayout_5.addWidget(self.GrpTimerOpts)
        self.verticalLayout_4.addWidget(self.GrpPlayerOpts)
        self.horizontalLayout.addWidget(self.verticalFrame)
        self.verticalFrame_2 = QtWidgets.QFrame(Custom_Game_1)
        self.verticalFrame_2.setMaximumSize(QtCore.QSize(213, 392))
        self.verticalFrame_2.setObjectName("verticalFrame_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalFrame_2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.groupBox_5 = QtWidgets.QGroupBox(self.verticalFrame_2)
        self.groupBox_5.setMinimumSize(QtCore.QSize(211, 251))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.groupBox_5.setObjectName("groupBox_5")
        self.lineup_preview = QtWidgets.QLabel(self.groupBox_5)
        self.lineup_preview.setGeometry(QtCore.QRect(10, 40, 191, 191))
        self.lineup_preview.setText("")
        self.lineup_preview.setPixmap(QtGui.QPixmap("../resources/board_minimal.png"))
        self.lineup_preview.setScaledContents(True)
        self.lineup_preview.setObjectName("lineup_preview")
        self.verticalLayout_6.addWidget(self.groupBox_5)
        self.buttonAdvOpts = QtWidgets.QPushButton(self.verticalFrame_2)
        self.buttonAdvOpts.setEnabled(False)
        self.buttonAdvOpts.setMinimumSize(QtCore.QSize(201, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.buttonAdvOpts.setFont(font)
        self.buttonAdvOpts.setObjectName("buttonAdvOpts")
        self.verticalLayout_6.addWidget(self.buttonAdvOpts)
        self.buttonStart = QtWidgets.QPushButton(self.verticalFrame_2)
        self.buttonStart.setMinimumSize(QtCore.QSize(201, 91))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.buttonStart.setFont(font)
        self.buttonStart.setObjectName("buttonStart")
        self.verticalLayout_6.addWidget(self.buttonStart)
        self.horizontalLayout.addWidget(self.verticalFrame_2)
        self.verticalLayout_7.addLayout(self.horizontalLayout)

        self.retranslateUi(Custom_Game_1)
        QtCore.QMetaObject.connectSlotsByName(Custom_Game_1)

    def retranslateUi(self, Custom_Game_1):
        _translate = QtCore.QCoreApplication.translate
        Custom_Game_1.setWindowTitle(_translate("Custom_Game_1", "Form"))
        self.label.setText(_translate("Custom_Game_1", "Versus Mode"))
        self.GrpGameOpts.setTitle(_translate("Custom_Game_1", "Game Options"))
        self.BoardOpts.setTitle(_translate("Custom_Game_1", "Board Selection"))
        self.Board_8x8.setText(_translate("Custom_Game_1", "Chess [ 8x8 ]"))
        self.Board_9x9.setText(_translate("Custom_Game_1", "Shogi [ 9x9 ]"))
        self.e_promodrop.setText(_translate("Custom_Game_1", "Promoted Drop"))
        self.e_menpassant.setText(_translate("Custom_Game_1", "Metal Piece\n"
"en-passant"))
        self.e_mdoublemove.setText(_translate("Custom_Game_1", "Metal Piece\n"
"Double initial move"))
        self.CaptureOpts.setTitle(_translate("Custom_Game_1", "Capture Mode"))
        self.c_crazyhouse.setText(_translate("Custom_Game_1", "Crazyhouse"))
        self.c_graveyard.setText(_translate("Custom_Game_1", "Graveyard"))
        self.c_shogionly.setText(_translate("Custom_Game_1", "Shogi Pieces Only"))
        self.GrpPlayerOpts.setTitle(_translate("Custom_Game_1", "Player Options"))
        self.P1Side.setTitle(_translate("Custom_Game_1", "Player 1 Side"))
        self.P1_Chess.setText(_translate("Custom_Game_1", "Chess"))
        self.P1_Shogi.setText(_translate("Custom_Game_1", "Shogi"))
        self.Lineup.setTitle(_translate("Custom_Game_1", "Lineup"))
        self.L_Shogi.setTitle(_translate("Custom_Game_1", "Shogi"))
        self.SL_Default.setText(_translate("Custom_Game_1", "Default"))
        self.SL_Mirror.setText(_translate("Custom_Game_1", "Mirror"))
        self.SL_Outpost.setText(_translate("Custom_Game_1", "Outpost"))
        self.L_Chess.setTitle(_translate("Custom_Game_1", " Chess"))
        self.CL_Default.setText(_translate("Custom_Game_1", "Default"))
        self.CL_QDown.setText(_translate("Custom_Game_1", "Queen Down"))
        self.CL_RKnight.setText(_translate("Custom_Game_1", "Royal Knight"))
        self.GrpTimerOpts.setTitle(_translate("Custom_Game_1", "Timer"))
        self.checkByoyomi.setText(_translate("Custom_Game_1", "Byoyomi"))
        self.checkIncrement.setText(_translate("Custom_Game_1", "Increment"))
        self.checkDelay.setText(_translate("Custom_Game_1", "Delay"))
        self.timeTimer.setDisplayFormat(_translate("Custom_Game_1", "mm:ss"))
        self.label_2.setText(_translate("Custom_Game_1", "Duration"))
        self.groupBox_5.setTitle(_translate("Custom_Game_1", "Lineup Preview"))
        self.buttonAdvOpts.setText(_translate("Custom_Game_1", "Advanced Options"))
        self.buttonStart.setText(_translate("Custom_Game_1", "Start Playing"))
