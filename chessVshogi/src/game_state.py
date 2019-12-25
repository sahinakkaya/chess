from PyQt5 import QtCore

from chessVshogi.src.cell import Cell


class GameState:
    def __init__(self, piece_layout, window=None):
        super().__init__()
        self.pieces_on_board = []
        self.board_size = len(piece_layout)
        self.piece_layout = piece_layout
        self.window = window
        self.board = []
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
        self.create_board()

    def create_board(self):
        import chessVshogi.src.ui_mapper as ui_mapper
        mapper = ui_mapper.mapper()
        for i, line in enumerate(self.piece_layout):
            self.board.append([])
            for j, name in enumerate(line):
                game_piece = None
                try:
                    game_piece = mapper[name]["piece"](
                        board=self.window, x=j + 1, y=i + 1, side=name[2])
                    game_piece.resource = mapper[name]["resource"]
                    game_piece.name_ = name
                except KeyError:
                    pass
                cell = Cell(x=j + 1, y=i + 1, piece=game_piece)
                self.board[-1].append(cell)


if __name__ == '__main__':
    from chessVshogi.src.layouts import chess_default, shogi_default
    from chessVshogi.src.windows import in_game_window
    from chessVshogi.UI.ingame_chess import Ui_IngameChess
    import sys
    from PyQt5.QtWidgets import QApplication

    # app = QApplication([])
    # w = in_game_window.in_game_wrapper(Ui_IngameChess, 8)()
    GameState(chess_default)
    # sys.exit(app.exec_())
