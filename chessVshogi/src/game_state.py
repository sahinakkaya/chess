from PyQt5 import QtCore


class GameState:
    def __init__(self, sz):
        super().__init__()
        self.pieces_on_board = []
        self.board_size = sz
        self.turn = "White"
        self.action = "Wait"  # Wait - Hold
        self.latest_click = None
        self.danger = {
            "White": False,
            "Black": False
            }
        self.timer_white = QtCore.QTimer()
        self.timer_white.setInterval(1000)
        self.timer_black = QtCore.QTimer()
        self.timer_black.setInterval(1000)
