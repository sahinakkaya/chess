from PyQt5.QtWidgets import QWidget
from chessVshogi.UI.custom_game_1 import Ui_Custom_Game_1


class VersusGameOptsWindow(QWidget, Ui_Custom_Game_1):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)