from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget

import chessVshogi
import chessVshogi.layouts as layouts
from chessVshogi.UI.gamemode_menu import Ui_Gamemode_Menu
from chessVshogi.UI.ingame_chess import Ui_IngameChess
from chessVshogi.UI.ingame_shogi import Ui_IngameShogi
from chessVshogi.src.windows.in_game_window import in_game_wrapper


class GameModeWindow(QWidget, Ui_Gamemode_Menu):
    def __init__(self, par):
        super().__init__(par)
        self.setupUi(self)
        self.buttonChess.clicked.connect(self.load_game)
        self.buttonShogi.clicked.connect(self.load_game)
        self.buttonHybrid.clicked.connect(self.load_game)

    def load_game(self):
        button_name = self.sender().objectName()[6:]
        try:
            board_layout = globals()[f"Ui_Ingame{button_name}"]
        except KeyError:
            board_layout = globals()["Ui_IngameShogi"]
        piece_layout = getattr(chessVshogi.layouts,
                               f"{button_name.lower()}_default")
        if button_name == "Chess":
            board_size = 8
        else:
            board_size = 9

        window_in_game = in_game_wrapper(board_layout, board_size)()
        window_in_game.load_layout(piece_layout)
        window_in_game.load_pieces(piece_layout)
        window_in_game.draw_board()
        stacked_widget = self.parentWidget()
        stacked_widget.addWidget(window_in_game)
        stacked_widget.setCurrentIndex(3)


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication([])
    w_g = GameModeWindow()

    sys.exit(app.exec_())
