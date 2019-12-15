from UI.mainwindow import *
from UI.gamemode_menu import *
from UI.options_menu import *
from UI.ingame_shogi import *
from UI.ingame_chess import *
from UI.ingame_ui import *
from threading import Thread
from time import sleep
# from datetime import datetime, time

class gamestate:
    def __init__(self, sz):
        super().__init__()
        self.boardsize = sz
        self.turn = "White"
        self.action = "Wait" # Wait - Hold
        self.latest_click = None


class window_ingame_8x8(QtWidgets.QWidget, Ui_IngameChess):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # self.show()
        self.tiles = []
        self.state = gamestate(8)
        # self.Ui_IngameChess = Ui_IngameChess
        self.timer_started = False

        for i in range(11, 89):
            try:
                tile = getattr(self, "Tile_{}".format(i))
                self.tiles.append(tile)
                tile.installEventFilter(self)
                if tile.property("Piece") != '':
                    tile.setPixmap(QtGui.QPixmap(Piece_Resource_Corresp[tile.property("Piece")]))
            except AttributeError:
                pass

    # Code taken from https://www.reddit.com/r/learnpython/comments/cx8qje/how_do_you_have_a_countdown_timer_without_it/
    def Timer(self, time_limit):
        sleep_duration = time_limit
        while sleep_duration > 0:
            minutes = int(sleep_duration / 60)
            seconds = int(sleep_duration % 60)
            print(f"you have {minutes}:{seconds} left")
            # Gui'de göstermeyi bulamadım???
            # Ui_IngameChess.setTime(self, minutes, seconds)
            sleep(1)
            sleep_duration -= 1
        print("timer completed")

    def eventFilter(self, source, event):
        if event.type() == QtCore.QEvent.MouseButtonPress and source in self.tiles:
            if not self.timer_started:
                self.timer_thread = Thread(target=self.Timer, args=[300])
                self.timer_thread.start()
                self.timer_started = True

            if not self.timer_thread.is_alive():
                # timer is complete
                print("oh no. you ran out of time!")

            if event.button() == 1:
                self.clicked_tile = source
                posx, posy = self.clicked_tile.objectName()[-2], self.clicked_tile.objectName()[-1]
                print(self.state.turn, self.state.action)
                print("Coordinates:", posx, posy)
                if self.state.action=="Hold":
                    self.state.action = "Wait"
                    if self.latest_click is not None:
                        print("attempt to move the piece at", self.latest_click, "to ", posx, posy)
                    print("State changed back to Wait")

                if source.pixmap() is not None:
                    print("You are trying to move",source.property("Piece"))
                    if self.state.action =="Wait":
                        self.state.action = "Hold"
                        self.latest_click = tuple((posx, posy),)
                        print("State changed to Hold")
        return super(window_ingame_8x8, self).eventFilter(source, event)

class window_ingame_9x9(QtWidgets.QWidget, Ui_IngameShogi):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # self.show()
        self.tiles = []
        for i in range(11, 100):
            try:
                tile = getattr(self, "Tile_{}".format(i))
                self.tiles.append(tile)
                tile.installEventFilter(self)
                if tile.property("Piece") != '':
                    tile.setPixmap(QtGui.QPixmap(Piece_Resource_Corresp[tile.property("Piece")]))
            except AttributeError:
                pass

    def eventFilter(self, source, event):
        if event.type() == QtCore.QEvent.MouseButtonPress and source in self.tiles:
            if event.button() == 1:
                self.clicked_tile = source
                print("Coordinates:", self.clicked_tile.objectName()[-2], self.clicked_tile.objectName()[-1])
                if source.pixmap() is not None:
                    print("You are trying to move a piece!")
                    print("It is coded as:", source.property("Piece"))
        return super(window_ingame_9x9, self).eventFilter(source, event)

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
		self.buttonChess.clicked.connect(start_8x8)
		self.buttonShogi.clicked.connect(start_9x9)
		self.closeEvent = self.closeEvent
	def closeEvent(self, event):
		back_to_main()
		event.accept()

class window_main(QtWidgets.QMainWindow, Ui_MainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.buttonStart.clicked.connect(game_menu)
		self.buttonOpts.clicked.connect(opts_menu)
		self.buttonExit.clicked.connect(self.close)
		self.show()

def start_8x8():
	w_c.show()
	w_g.hide()

def start_9x9():
	w_s.show()
	w_g.hide()

def game_menu():
	w.hide()
	w_g.show()

def opts_menu():
	w.hide()
	w_o.show()

def back_to_main():
	w.show()

import sys

app = QtWidgets.QApplication([])
w = window_main()
w_g = window_gamemode()
w_c = window_ingame_8x8()
w_s = window_ingame_9x9()
w_o = window_optsmenu()
sys.exit(app.exec_())