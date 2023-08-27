from PyQt6.QtWidgets import QWidget
from chessVshogi.UI.custom_game_1 import Ui_Custom_Game_1
from chessVshogi.src.windows.in_game_window import in_game_wrapper
import chessVshogi.src.layouts as layouts
from chessVshogi.UI.ingame_chess import Ui_IngameChess
from chessVshogi.UI.ingame_shogi import Ui_IngameShogi

class VersusGameOptsWindow(QWidget, Ui_Custom_Game_1):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.buttonStart.clicked.connect(self.load_game)

    def load_game(self):
        if self.Board_8x8.isChecked():
            _layout = globals()["Ui_IngameChess"]
        else:
            _layout = globals()["Ui_IngameShogi"]

        if self.SL_Default.isChecked():
            piece_layout = getattr(layouts, "shogi_8x8_default_white")
        else:
            piece_layout = getattr(layouts, "shogi_8x8_mirror_white")
            pass

        window_in_game = in_game_wrapper(_layout, piece_layout)()
        stacked_widget = self.parentWidget()
        stacked_widget.addWidget(window_in_game)
        stacked_widget.setCurrentIndex(4)
