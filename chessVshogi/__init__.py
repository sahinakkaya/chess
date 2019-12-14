from UI.mainwindow import *
from UI.gamemode_menu import *
from UI.options_menu import *

class window_optsmenu(QtWidgets.QWidget, Ui_Options_Menu):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.closeEvent = self.closeEvent
	def closeEvent(self, event):
		back_to_main()
		event.accept()

class window_gamemode(QtWidgets.QWidget, Ui_Gamemode_Menu):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.closeEvent = self.closeEvent
	def closeEvent(self, event):
		back_to_main()
		event.accept()

class window_main(QtWidgets.QMainWindow, Ui_MainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.pushButton.clicked.connect(game_menu)
		self.pushButton_2.clicked.connect(opts_menu)
		self.pushButton_3.clicked.connect(self.close)
		self.show()

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
w_o = window_optsmenu()
sys.exit(app.exec_())