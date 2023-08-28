from PyQt6 import QtWidgets
from PyQt6.QtCore import pyqtSignal, QTime, QEvent, Qt
from PyQt6.QtGui import QPixmap

from chessVshogi.src import directions
from chessVshogi.src.game_state import GameState


def in_game_wrapper(board_layout, piece_layout):
    class InGameWindow(QtWidgets.QWidget, board_layout):
        piece_moved = pyqtSignal(tuple, tuple, str)

        def __init__(self):
            super().__init__()
            self.setupUi(self)
            self.game_started = False
            self.buttonResignRestart.clicked.connect(
                self.resignOrRestart)

        def restart_game(self):
            self.game_started = False
            self.buttonResignRestart.setText("Start")
            self.tiles = []
            self.create_tiles()
            self.possible_moves = None
            self.latest_click = None
            self.latest_shadow_b = None
            self.latest_shadow_w = None
            self.possible_dead_pawn = None
            self.piece_layout = piece_layout
            self.board_size = len(piece_layout)
            self.state = GameState(piece_layout, self)
            self.timeWhite.setTime(QTime(0, 10))
            self.timeBlack.setTime(QTime(0, 10))
            self.state.timer_white.timeout.connect(
                lambda: self.cool_down("White"))
            self.state.timer_black.timeout.connect(
                lambda: self.cool_down("Black"))
            self.draw_board()

        def resignOrRestart(self):
            if self.game_started:
                self.buttonResignRestart.setText("Restart")
                self.terminate_game("lost", self.state.turn,
                                            "Resigned")
            else:
                self.restart_game()
                self.buttonResignRestart.setText("Resign")
                self.start_game()


        def create_tiles(self):
            for i in range(11, 100):
                try:
                    tile = getattr(self, "Tile_{}".format(i))
                except AttributeError:
                    continue
                tile.installEventFilter(self)
                self.tiles.append(tile)

        def showEvent(self, event):
            event.accept()

        def cool_down(self, color):
            if self.isEnabled():
                time_edit = getattr(self, f"time{color}")
                time_edit.setTime(time_edit.time().addSecs(-1))
                main_window = self.parentWidget().parentWidget().parentWidget()
                main_window.setWindowTitle(self.labelTurn.text() +
                                           " Remaining Time:" +
                                           time_edit.text() +
                                           "- Chess")

        def eventFilter(self, source, event):
            if event.type() == QEvent.Type.MouseButtonPress and source in self.tiles:
                if not self.game_started:
                    pass
                elif event.button() == Qt.MouseButton.LeftButton:
                    posx, posy = map(int, iter(source.objectName()[-2:]))
                    if self.state.action == "Hold":
                        self.relocate_piece(posx, posy)
                    elif self.get_piece(posx, posy) is not None:
                        self.hold_piece(posx, posy)

            return super(InGameWindow, self).eventFilter(source, event)

        def change_turn(self):
            if self.state.turn == "White":
                self.state.turn = "Black"
                self.state.timer_white.stop()
                self.state.timer_black.start()
            else:
                self.state.turn = "White"
                self.state.timer_black.stop()
                self.state.timer_white.start()
            self.labelTurn.setText("Turn: {}".format(self.state.turn))

        def hold_piece(self, posx, posy):
            piece = self.get_piece(posx, posy)
            if piece.side != self.state.turn[0]:
                pass
            elif self.state.action == "Wait":
                self.state.action = "Hold"
                self.latest_click = (posx, posy)
                possible_moves = piece.get_possible_moves()
                self.set_possible_moves(possible_moves)
                self.toggle_highlight_for_possible_moves()

        def draw_board(self):
            for row in self.state.board:
                # print(row)
                for cell in row:
                    tile = self.get_tile_at(cell.x, cell.y)
                    if cell.piece:
                        pixmap = cell.piece.resource
                        tile.setPixmap(QPixmap(pixmap))
                    else:
                        tile.clear()
            # print()

        def relocate_piece(self, posx, posy):
            self.state.action = "Wait"
            piece_tile = self.get_last_clicked_tile()
            source_cell = self.get_cell(*self.latest_click)
            destination_cell = self.get_cell(posx, posy)
            clicked_piece = destination_cell.piece
            if self.latest_click == (posx, posy):
                pass
            elif (posx, posy) in self.possible_moves:

                destination_cell.set_piece(source_cell.piece)
                source_cell.clear()
                self.clear_shadows()
                self.draw_board()
                moved_piece = destination_cell.piece.name_[3]
                if moved_piece == "K" and self.state.danger[self.state.turn]:
                    self.toggle_highlight_tile(piece_tile, "threat")
                    self.toggle_highlight_tile(piece_tile)
                if self.check_king_threat():
                    print("Illegal move.")
                    self.terminate_game(result="lost", player=self.state.turn,
                                        case="Illegal move.")
                    return
                self.change_turn()
                if self.check_king_threat():
                    print("Threat!")
            elif clicked_piece and clicked_piece.side == self.state.turn[0]:
                self.toggle_highlight_for_possible_moves()
                self.hold_piece(posx, posy)
            else:
                self.state.action = "Hold"
            if self.state.action != "Hold":
                self.toggle_highlight_for_possible_moves()

        def clear_shadows(self):
            if self.state.turn == "White":
                if self.latest_shadow_b:
                    cell = self.get_cell(*self.latest_shadow_b)
                    cell.shadow = None
            else:
                if self.latest_shadow_w:
                    cell = self.get_cell(*self.latest_shadow_w)
                    cell.shadow = None

        def toggle_highlight_for_possible_moves(self):
            for i in self.possible_moves:
                tile = self.get_tile_at(i.x, i.y)
                self.toggle_highlight_tile(tile)

        def handle_double_square_move(self, shadow_x, shadow_y,
                                      actual_x, actual_y):
            self.get_cell(shadow_x, shadow_y).shadow = self.get_cell(actual_x,
                                                                     actual_y)
            if self.state.turn == "White":
                self.latest_shadow_w = shadow_x, shadow_y
            else:
                self.latest_shadow_b = shadow_x, shadow_y

        def handle_pawn_promotion(self, piece):
            from chessVshogi.UI.PawnPromoOpts import Ui_Frame

            class PromoWindow(QtWidgets.QWidget, Ui_Frame):
                def __init__(self, parent=None):
                    super().__init__(parent)
                    self.setupUi(self)
                    self.windowptr = None

                def show_black(self):
                    import PyQt6.QtGui as QtGui
                    knighticon = QtGui.QIcon()
                    knighticon.addPixmap(QtGui.QPixmap(":/Chess/resources/chess_48/Chess_ndt48.png"),
                                         QtGui.QIcon.Normal,
                                         QtGui.QIcon.Off)
                    bishopicon = QtGui.QIcon()
                    bishopicon.addPixmap(QtGui.QPixmap(":/Chess/resources/chess_48/Chess_bdt48.png"),
                                         QtGui.QIcon.Normal,
                                         QtGui.QIcon.Off)
                    queenicon = QtGui.QIcon()
                    queenicon.addPixmap(QtGui.QPixmap(":/Chess/resources/chess_48/Chess_qdt48.png"), QtGui.QIcon.Normal,
                                        QtGui.QIcon.Off)
                    rookicon = QtGui.QIcon()
                    rookicon.addPixmap(QtGui.QPixmap(":/Chess/resources/chess_48/Chess_rdt48.png"), QtGui.QIcon.Normal,
                                       QtGui.QIcon.Off)
                    self.Knight.setIcon(knighticon)
                    self.Bishop.setIcon(bishopicon)
                    self.Queen.setIcon(queenicon)
                    self.Rook.setIcon(rookicon)

                def closeEvent(self, event):
                    self.windowptr.setEnabled(True)
                    self.windowptr.check_king_threat()
                    event.accept()

            self.popup = PromoWindow()
            self.popup.windowptr = self
            if piece.side == "B":
                self.popup.show_black()
            self.popup.show()
            self.setDisabled(True)
            self.popup.Knight.clicked.connect(piece.transform)
            self.popup.Bishop.clicked.connect(piece.transform)
            self.popup.Queen.clicked.connect(piece.transform)
            self.popup.Rook.clicked.connect(piece.transform)

        @staticmethod
        def toggle_highlight_tile(tile, style="move"):
            stylesheet_remapper = {
                "border-image: url(:/BG/resources/Wooden_noborder.jpg);": "border-image: url("
                                                                          ":/BG/resources/Wooden_selected.jpg);",
                "border-image: url(:/BG/resources/Wooden_selected.jpg);": "border-image: url("
                                                                          ":/BG/resources/Wooden_noborder.jpg);",
                "border-image: url(:/BG/resources/Wooden_threat.jpg);": "border-image: url("
                                                                        ":/BG/resources/Wooden_threat.jpg);",
                "background-color: rgb(255, 255, 255);": "background-color: rgb(42, 192, 92);",
                "background-color: rgb(42, 192, 92);": "background-color: rgb(255, 255, 255);",
                "background-color: rgb(127, 127, 127);": "background-color: rgb(21, 96, 46);",
                "background-color: rgb(21, 96, 46);": "background-color: rgb(127, 127, 127);",
                "background-color: rgb(96, 24, 12);": "background-color: rgb(96, 24, 12);",
                "background-color: rgb(192, 48, 24);": "background-color: rgb(192, 48, 24);"
                }
            threat_remapper = {
                "border-image: url(:/BG/resources/Wooden_noborder.jpg);": "border-image: url("
                                                                          ":/BG/resources/Wooden_threat.jpg);",
                "border-image: url(:/BG/resources/Wooden_threat.jpg);": "border-image: url("
                                                                        ":/BG/resources/Wooden_noborder.jpg);",
                "border-image: url(:/BG/resources/Wooden_selected.jpg);": "border-image: url("
                                                                          ":/BG/resources/Wooden_selected.jpg);",
                "background-color: rgb(255, 255, 255);": "background-color: rgb(192, 48, 24);",
                "background-color: rgb(192, 48, 24);": "background-color: rgb(255, 255, 255);",
                "background-color: rgb(127, 127, 127);": "background-color: rgb(96, 24, 12);",
                "background-color: rgb(96, 24, 12);": "background-color: rgb(127, 127, 127);",
                "background-color: rgb(42, 192, 92);": "background-color: rgb(42, 192, 92);",
                "background-color: rgb(21, 96, 46);": "background-color: rgb(21, 96, 46);"
                }
            if style == "move":
                tile.setStyleSheet(stylesheet_remapper[tile.styleSheet()])
            elif style == "threat":
                tile.setStyleSheet(threat_remapper[tile.styleSheet()])

        def set_possible_moves(self, possible_moves):
            filtered_moves = directions.SetOfVectors()
            for x, y in possible_moves:
                piece = self.get_piece(x, y)
                if not piece or piece.side != self.state.turn[0]:
                    filtered_moves.add(directions.Vector2D(x, y))
            filtered_moves.add(directions.Vector2D(*self.latest_click))
            self.possible_moves = filtered_moves

        def is_empty(self, x, y, include_shadows=False):
            piece_check = self.get_piece(x, y) is None
            shadow_check = self.get_cell(x, y).shadow is None
            if include_shadows:
                return piece_check and shadow_check

            return piece_check

        def get_piece(self, x, y):
            return self.get_cell(x, y).piece

        def get_cell(self, x, y):
            return self.state.board[y - 1][x - 1]

        def get_tile_at(self, x, y):
            return getattr(self, "Tile_{}{}".format(x, y))

        def get_last_clicked_tile(self):
            return self.get_tile_at(*self.latest_click)

        def get_king_position(self):
            for row in self.state.board:
                for cell in row:
                    piece = cell.piece
                    if piece and piece.name() == "King" and \
                            piece.side == self.state.turn[0]:
                        return piece.x, piece.y

        def check_king_threat(self):
            king_pos = self.get_king_position()
            for row in self.state.board:
                for cell in row:
                    piece = cell.piece
                    if piece and piece.side != self.state.turn[0]:
                        if king_pos in piece.get_possible_moves():
                            if not self.state.danger[self.state.turn]:
                                self.state.danger[self.state.turn] = True
                                self.toggle_highlight_tile(
                                    self.get_tile_at(*king_pos), style="threat")
                            return True
            if self.state.danger[self.state.turn]:
                self.state.danger[self.state.turn] = False
                self.toggle_highlight_tile(self.get_tile_at(*king_pos),
                                           style="threat")
            return False

        def start_game(self):
            self.state.timer_white.start()
            self.labelTurn.setText("Turn: {}".format(self.state.turn))
            self.game_started = True

        def terminate_game(self, result, player, case):
            self.state.timer_white.stop()
            self.state.timer_black.stop()
            g_over = QtWidgets.QMessageBox()
            g_over.setIcon(QtWidgets.QMessageBox.Icon.Information)
            g_over.setWindowTitle('Game Over')
            g_over.setText(case + "\n{} has {}".format(player, result))
            g_over.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
            g_over.exec()
            self.tiles = []
            main_window = self.parentWidget().parentWidget().parentWidget()
            main_window.setWindowTitle("Chess")
            self.game_started = False

    return InGameWindow


if __name__ == '__main__':
    from chessVshogi.src.layouts import chess_default
    from chessVshogi.src.windows import in_game_window
    from chessVshogi.UI.ingame_chess import Ui_IngameChess
    import sys
    from PyQt6.QtWidgets import QApplication

    app = QApplication([])
    w = in_game_window.in_game_wrapper(Ui_IngameChess, chess_default)()
    w.draw_board()
    w.show()
    sys.exit(app.exec_())
