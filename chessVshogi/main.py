from PyQt5 import QtCore, QtGui, QtWidgets
from UI.mainwindow import Ui_MainWindow
from UI.gamemode_menu import Ui_Gamemode_Menu
from UI.options_menu import Ui_Options_Menu
from UI.ingame_shogi import Ui_IngameShogi
from UI.ingame_chess import Ui_IngameChess
from UI.ingame_ui import Piece_Resource_Corresp

class gamestate:
    def __init__(self, sz):
        super().__init__()
        self.boardsize = sz
        self.turn = "White"
        self.action = "Wait" # Wait - Hold
        self.latest_click = None
        self.wt = QtCore.QTimer()
        self.wt.setInterval(1000)
        self.bt = QtCore.QTimer()
        self.bt.setInterval(1000)

def ingame_wrapper(ui_class, boardsize):
    class window_ingame(QtWidgets.QWidget, ui_class):
        def __init__(self):
            super().__init__()
            self.setupUi(self)
            self.tiles = []
            self.state = gamestate(boardsize)
            self.timeEdit.setTime(QtCore.QTime(0, 10))
            self.timeEdit_2.setTime(QtCore.QTime(0, 10))
            self.state.wt.timeout.connect(self.whiteCD)
            self.state.bt.timeout.connect(self.blackCD)
            self.showEvent = self.showEvent
            # self.Ui_IngameChess = Ui_IngameChess
            for i in range(11, 100):
                try:
                    tile = getattr(self, "Tile_{}".format(i))
                    self.tiles.append(tile)
                    tile.installEventFilter(self)
                    if tile.property("Piece") != '':
                        tile.setPixmap(QtGui.QPixmap(Piece_Resource_Corresp[tile.property("Piece")]))
                    else:
                        tile.clear()
                except AttributeError:
                    pass
                
        def showEvent(self, event):
            self.state.wt.start()
            event.accept()

        def whiteCD(self):
            self.timeEdit.setTime(self.timeEdit.time().addSecs(-1))

        def blackCD(self):
            self.timeEdit_2.setTime(self.timeEdit_2.time().addSecs(-1))

        def drawBoard(self):
            # O tile'daki piece'i ekrana çiz
            for i in range(11, 89):
                try:
                    tile = getattr(self, "Tile_{}".format(i))
                    if tile.property("Piece") != '':
                        tile.setPixmap(QtGui.QPixmap(Piece_Resource_Corresp[tile.property("Piece")]))
                    else:
                        tile.clear()
                except AttributeError:
                    pass

        def eventFilter(self, source, event):
            # Saha içinde mouse'a tıklandıysa
            if event.type() == QtCore.QEvent.MouseButtonPress and source in self.tiles:

                # Sol click ile tıklandıysa
                if event.button() == 1:
                    self.clicked_tile = source
                    posx, posy = self.clicked_tile.objectName()[-2], self.clicked_tile.objectName()[-1]
                    print(self.state.turn, self.state.action)
                    print("Coordinates:", posx, posy)

                    # Bir taşa bastıysam hold state'ine geçip ife giriyor
                    # Hold state'ine geçiş sonraki if'te (elif'te)
                    if self.state.action=="Hold":
                        self.state.action = "Wait"
                        if self.latest_click is not None:
                            piece_tile = getattr(self, "Tile_{}{}".format(self.latest_click[0], self.latest_click[1]))
                            destination_tile = getattr(self, "Tile_{}{}".format(posx, posy))
                            # self.cursor().setShape(Qt.CursorShape(piece_tile.property("Piece")) )
                            # self.cursor().setShape( QtGui.QPixmap(Piece_Resource_Corresp[piece_tile.property("Piece")]) )
                            print("attempt to move the piece", piece_tile.property("Piece"), "at", piece_tile, "to ", destination_tile)
                        print("State changed back to Wait")
                        if self.latest_click == (posx, posy):
                            print("Piece unhold")
                            # self.cursor().setShape(ArrowCursor)
                        else:
                            destination_tile.setProperty("Piece", piece_tile.property("Piece")) 
                            piece_tile.setProperty("Piece", '')
                            self.drawBoard()
                            # self.cursor().setShape(ArrowCursor)
                            print("Changing turn")
                            self.change_turn()
                    elif source.pixmap() is not None:
                        print("You are trying to move",source.property("Piece"))
                        if source.property("Piece")[2] != self.state.turn[0]:
                            print("... which is not your piece.")
                        elif self.state.action =="Wait":
                            self.state.action = "Hold"
                            self.latest_click = tuple((posx, posy),)
                            print("State changed to Hold")
            return super(window_ingame, self).eventFilter(source, event)

        def change_turn(self):
            if self.state.turn == "White":
                self.state.turn = "Black"
                self.state.wt.stop()
                self.state.bt.start()
            else:
                self.state.turn = "White"
                self.state.bt.stop()
                self.state.wt.start()

    return window_ingame

class window_optsmenu(QtWidgets.QWidget, Ui_Options_Menu):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.closeEvent = self.closeEvent
		self.buttonReturn.clicked.connect(self.close)
	def closeEvent(self, event):
		back_to_main()
		event.accept()

class window_gamemode(QtWidgets.QWidget, Ui_Gamemode_Menu):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.buttonChess.clicked.connect(self.start_chess_game)
		self.buttonShogi.clicked.connect(self.start_shogi_game)
		self.closeEvent = self.closeEvent
	def start_chess_game(self):
		w_w = ingame_wrapper(Ui_IngameChess, 8)()
		w_w.show()
		self.hide()
	def start_shogi_game(self):
		w_w = ingame_wrapper(Ui_IngameShogi, 9)()
		w_w.show()
		self.hide()
	def closeEvent(self, event):
		back_to_main()
		event.accept()

class window_main(QtWidgets.QMainWindow, Ui_MainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.buttonStart.clicked.connect(self.game_menu)
		self.buttonOpts.clicked.connect(self.opts_menu)
		self.buttonExit.clicked.connect(self.close)
		self.show()
	def game_menu(self):
		w_g.show()
		self.hide()
	def opts_menu(self):
		w_o.show()
		self.hide()

def back_to_main():
	w.show()

import sys

app = QtWidgets.QApplication([])
w = window_main()
w_g = window_gamemode()
# w_c = window_ingame_8x8()
# w_s = window_ingame_9x9()
w_o = window_optsmenu()
sys.exit(app.exec_())