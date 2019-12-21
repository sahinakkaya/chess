from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal, QTime, QEvent
from PyQt5.QtGui import QPixmap

from chessVshogi.src import directions
from chessVshogi.UI.ui_mapper import mapper
from chessVshogi.src.game_state import GameState


def in_game_wrapper(ui_class, board_size):
    class InGameWindow(QtWidgets.QWidget, ui_class):
        mouse_clicked = pyqtSignal(int, int)
        piece_moved = pyqtSignal(tuple, tuple, str)

        def __init__(self):
            super().__init__()
            self.setupUi(self)
            self.tiles = []
            self.create_tiles()
            self.possible_moves = None
            self.latest_click = None
            self.latest_shadow = None
            self.possible_dead_pawn = None
            self.state = GameState(board_size)
            self.timeWhite.setTime(QTime(0, 10))
            self.timeBlack.setTime(QTime(0, 10))
            self.state.timer_white.timeout.connect(
                lambda: self.cool_down("White"))
            self.state.timer_black.timeout.connect(
                lambda: self.cool_down("Black"))
            self.buttonResign.clicked.connect(
                lambda: self.terminate_game("lost", self.state.turn,
                                            "Resigned"))

        def create_tiles(self):
            for i in range(11, 100):
                try:
                    tile = getattr(self, "Tile_{}".format(i))
                except AttributeError:
                    continue
                tile.installEventFilter(self)
                self.tiles.append(tile)

        def showEvent(self, event):
            self.state.timer_white.start()
            event.accept()

        def cool_down(self, color):
            time_edit = getattr(self, f"time{color}")
            time_edit.setTime(time_edit.time().addSecs(-1))
            self.setWindowTitle(self.labelTurn.text() +
                                " Remaining Time:" +
                                time_edit.text() +
                                "- chessVshogi")

        def draw_board(self):
            for tile in self.tiles:
                if tile.property("Piece") not in ("", "shadow"):
                    pixmap = mapper[tile.property("Piece")]["resource"]
                    tile.setPixmap(QPixmap(pixmap))
                else:
                    tile.clear()

        def eventFilter(self, source, event):
            if event.type() == QEvent.MouseButtonPress and source in self.tiles:
                if event.button() == 1:
                    posx, posy = map(int, iter(source.objectName()[-2:]))
                    if self.state.action == "Hold":
                        self.relocate_piece(posx, posy)
                    elif source.pixmap() is not None:
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
                        piece = mapper[layout[j][i]]["piece"](board=self,
                                                              x=j + 1, y=i + 1)
                        piece.side = layout[j][i][2]
                        self.state.pieces_on_board.append(piece)
                    except KeyError:
                        pass

        def get_king_position(self):
            for piece in self.state.pieces_on_board:
                if piece.name() in ["King", "S_King"] and \
                        piece.side == self.state.turn[0]:
                    return piece.x, piece.y

        def check_king_threat(self):
            king_pos = self.get_king_position()
            for piece in self.state.pieces_on_board:
                if piece.side != self.state.turn[0]:
                    if king_pos in piece.get_possible_moves(piece.x, piece.y,
                                                            False):
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

        def terminate_game(self, result, player, case):
            self.state.timer_white.stop()
            self.state.timer_black.stop()
            g_over = QtWidgets.QMessageBox()
            g_over.setIcon(QtWidgets.QMessageBox.Information)
            g_over.setWindowTitle('Game Over')
            g_over.setText(case + "\n{} has {}".format(player, result))
            g_over.setStandardButtons(QtWidgets.QMessageBox.Ok)
            g_over.exec()
            self.tiles = []
            self.setDisabled(True)

    return InGameWindow
