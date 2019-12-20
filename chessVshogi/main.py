from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, QEvent
from chessVshogi.UI.mainwindow import Ui_MainWindow
from chessVshogi.UI.gamemode_menu import Ui_Gamemode_Menu
from chessVshogi.UI.options_menu import Ui_Options_Menu
from chessVshogi.UI.ingame_shogi import Ui_IngameShogi
from chessVshogi.UI.ingame_chess import Ui_IngameChess
from chessVshogi.UI.ingame_ui import Piece_Resource_Corresp
from chessVshogi.UI.ingame_ui import Piece_Class_Corresp as pcc
import chessVshogi.layouts
import chessVshogi.directions as directions


class GameState:
    def __init__(self, sz):
        super().__init__()
        self.pieces_on_board = []
        self.board_size = sz
        self.turn = "White"
        self.action = "Wait"  # Wait - Hold
        self.latest_click = None
        self.wt = QtCore.QTimer()
        self.wt.setInterval(1000)
        self.bt = QtCore.QTimer()
        self.bt.setInterval(1000)


def in_game_wrapper(ui_class, board_size):
    class WindowInGame(QtWidgets.QWidget, ui_class):
        mouse_clicked = pyqtSignal(int, int)
        piece_moved = pyqtSignal(tuple, tuple, str)

        def __init__(self):
            super().__init__()
            self.setupUi(self)
            self.tiles = []
            self.possible_moves = None
            self.latest_click = None
            self.latest_shadow = None
            self.possible_dead_pawn = None
            self.state = GameState(board_size)
            self.timeWhite.setTime(QtCore.QTime(0, 10))
            self.timeBlack.setTime(QtCore.QTime(0, 10))
            self.state.wt.timeout.connect(lambda: self.cool_down("White"))
            self.state.bt.timeout.connect(lambda: self.cool_down("Black"))
            for i in range(11, 100):
                try:
                    tile = getattr(self, "Tile_{}".format(i))
                    self.tiles.append(tile)
                    tile.installEventFilter(self)
                    if tile.property("Piece") != '':
                        tile.setPixmap(QtGui.QPixmap(
                            Piece_Resource_Corresp[tile.property("Piece")]))
                    else:
                        tile.clear()
                except AttributeError:
                    pass

        def showEvent(self, event):
            self.state.wt.start()
            event.accept()

        def cool_down(self, color):
            time_edit = getattr(self, f"time{color}")
            time_edit.setTime(time_edit.time().addSecs(-1))

        def draw_board(self):
            for i in range(11, 100):
                try:
                    tile = getattr(self, "Tile_{}".format(i))
                    if tile.property("Piece") not in ("", "shadow"):
                        pixmap = Piece_Resource_Corresp[tile.property("Piece")]
                        tile.setPixmap(QtGui.QPixmap(pixmap))
                    else:
                        tile.clear()
                except AttributeError:
                    pass

        def eventFilter(self, source, event):
            if event.type() == QEvent.MouseButtonPress and source in self.tiles:
                if event.button() == 1:
                    posx, posy = map(int, iter(source.objectName()[-2:]))
                    print(self.state.turn, self.state.action)
                    if self.state.action == "Hold":
                        self.relocate_piece(posx, posy)
                    elif source.pixmap() is not None:
                        self.hold_piece(posx, posy)

            return super(WindowInGame, self).eventFilter(source, event)

        def change_turn(self):
            if self.state.turn == "White":
                self.state.turn = "Black"
                self.state.wt.stop()
                self.state.bt.start()
            else:
                self.state.turn = "White"
                self.state.bt.stop()
                self.state.wt.start()
            self.labelTurn.setText("Turn: {}".format(self.state.turn))

        def hold_piece(self, posx, posy):
            if self.get_piece(posx, posy)[2] != self.state.turn[0]:
                pass
            elif self.state.action == "Wait":
                self.state.action = "Hold"
                self.latest_click = (posx, posy)
                self.mouse_clicked.emit(posx, posy)
                self.toggle_highlight_for_possible_moves()

        def relocate_piece(self, posx, posy):
            self.state.action = "Wait"
            piece_tile = self.get_last_clicked_tile()
            destination_tile = self.get_tile_at(posx, posy)
            clicked_piece = self.get_piece(posx, posy)
            if self.latest_click == (posx, posy):
                pass
            elif (posx, posy) in self.possible_moves:
                destination_tile.setProperty("Piece",
                                             piece_tile.property("Piece"))
                piece_tile.setProperty("Piece", '')
                moved_piece = destination_tile.property("Piece")[3]
                if clicked_piece == "shadow":
                    if moved_piece == "P":
                        self.remove_dead_pawn()
                else:
                    self.clear_shadows()
                self.latest_shadow = None
                self.piece_moved.emit(self.latest_click, (posx, posy),
                                      moved_piece)
                self.draw_board()
                self.change_turn()
            elif clicked_piece and clicked_piece[2] == self.state.turn[0]:
                self.toggle_highlight_for_possible_moves()
                self.hold_piece(posx, posy)
            else:
                self.state.action = "Hold"
            if self.state.action != "Hold":
                self.toggle_highlight_for_possible_moves()

        def clear_shadows(self):
            if self.latest_shadow:
                tile = self.get_tile_at(*self.latest_shadow)
                tile.setProperty("Piece", "")

        def remove_dead_pawn(self):
            self.get_tile_at(*self.possible_dead_pawn).setProperty("Piece", "")

        def toggle_highlight_for_possible_moves(self):
            for i in self.possible_moves:
                tile = self.get_tile_at(i.x, i.y)
                self.toggle_highlight_tile(tile)

        def handle_double_square_move(self, shadow_x, shadow_y,
                                      actual_x, actual_y):
            self.latest_shadow = shadow_x, shadow_y
            self.possible_dead_pawn = actual_x, actual_y
            tile = self.get_tile_at(*self.latest_shadow)
            tile.setProperty("Piece", "shadow")

        @staticmethod
        def toggle_highlight_tile(tile):
            stylesheet_remapper = {
                "border-image: url(:/BG/resources/Wooden_noborder.jpg);": "border-image: url("
                                                                          ":/BG/resources/Wooden_selected.jpg);",
                "border-image: url(:/BG/resources/Wooden_selected.jpg);": "border-image: url("
                                                                          ":/BG/resources/Wooden_noborder.jpg);",
                "background-color: rgb(255, 255, 255);": "background-color: rgb(42, 192, 92);",
                "background-color: rgb(42, 192, 92);": "background-color: rgb(255, 255, 255);",
                "background-color: rgb(127, 127, 127);": "background-color: rgb(21, 96, 46);",
                "background-color: rgb(21, 96, 46);": "background-color: rgb(127, 127, 127);"
                }
            tile.setStyleSheet(stylesheet_remapper[tile.styleSheet()])

        def load_layout(self, layout):
            for i, line in enumerate(layout):
                for j, piece in enumerate(line):
                    self.get_tile_at(i + 1, j + 1).setProperty("Piece", piece)

        def set_possible_moves(self, possible_moves):
            filtered_moves = directions.SetOfVectors()
            for x, y in possible_moves:
                piece = self.get_piece(x, y)
                if piece == "" or piece[2] != self.state.turn[0]:
                    filtered_moves.add(directions.Vector2D(x, y))
            filtered_moves.add(directions.Vector2D(*self.latest_click))
            self.possible_moves = filtered_moves

        def is_empty(self, x, y):
            return self.get_piece(x, y) == ""

        def get_piece(self, x, y):
            return self.get_tile_at(x, y).property("Piece")

        def get_tile_at(self, x, y):
            return getattr(self, "Tile_{}{}".format(x, y))

        def get_last_clicked_tile(self):
            return self.get_tile_at(*self.latest_click)

        def load_pieces(self, layout):
            for i in range(self.state.board_size):
                for j in range(self.state.board_size):
                    try:
                        piece = pcc[layout[j][i]](board=self, x=j + 1, y=i + 1)
                        piece.side = layout[j][i][2]
                        self.state.pieces_on_board.append(piece)
                    except KeyError:
                        pass

        def get_king_position(self):
            for piece in self.state.pieces_on_board:
                if piece.name() in ["King", "S_King"] and \
                        piece.side == self.state.turn[0]:
                    return piece.x, piece.y

    return WindowInGame


class WindowOptsMenu(QtWidgets.QWidget, Ui_Options_Menu):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.closeEvent = self.closeEvent
        self.buttonReturn.clicked.connect(self.close)

    def closeEvent(self, event):
        back_to_main()
        event.accept()


class WindowGameMode(QtWidgets.QWidget, Ui_Gamemode_Menu):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.buttonChess.clicked.connect(self.start_chess_game)
        self.buttonShogi.clicked.connect(self.start_shogi_game)
        self.buttonHybrid.clicked.connect(self.start_hybrid_game)
        # FIXME: Is this really needed?
        self.closeEvent = self.closeEvent

    def start_chess_game(self):
        self.w_w = in_game_wrapper(Ui_IngameChess, 8)()
        self.w_w.load_pieces(chessVshogi.layouts.chess_default)
        self.w_w.show()
        self.hide()

    def start_shogi_game(self):
        self.w_w = in_game_wrapper(Ui_IngameShogi, 9)()
        self.w_w.load_pieces(chessVshogi.layouts.shogi_default)
        self.w_w.show()
        self.hide()

    def start_hybrid_game(self):
        self.w_w = in_game_wrapper(Ui_IngameShogi, 9)()
        self.w_w.load_layout(chessVshogi.layouts.hybrid_default)
        self.w_w.load_pieces(chessVshogi.layouts.hybrid_default)
        self.w_w.draw_board()
        self.w_w.show()
        self.hide()

    def closeEvent(self, event):
        back_to_main()
        event.accept()


class WindowMain(QtWidgets.QMainWindow, Ui_MainWindow):
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


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication([])
    w = WindowMain()
    w_g = WindowGameMode()
    # w_g.start_chess_game()
    w_o = WindowOptsMenu()
    sys.exit(app.exec_())
