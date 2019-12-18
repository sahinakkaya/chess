from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal
from chessVshogi.UI.mainwindow import Ui_MainWindow
from chessVshogi.UI.gamemode_menu import Ui_Gamemode_Menu
from chessVshogi.UI.options_menu import Ui_Options_Menu
from chessVshogi.UI.ingame_shogi import Ui_IngameShogi
from chessVshogi.UI.ingame_chess import Ui_IngameChess
from chessVshogi.UI.ingame_ui import Piece_Resource_Corresp
import chessVshogi.layouts
import chessVshogi.pieces as pieces


class GameState:
    def __init__(self, sz):
        super().__init__()
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
        piece_moved = pyqtSignal(tuple, tuple)

        def __init__(self):
            super().__init__()
            self.setupUi(self)
            self.tiles = []
            self.state = GameState(board_size)
            self.timeWhite.setTime(QtCore.QTime(0, 10))
            self.timeBlack.setTime(QtCore.QTime(0, 10))
            self.state.wt.timeout.connect(self.whiteCD)
            self.state.bt.timeout.connect(self.blackCD)
            self.showEvent = self.showEvent
            # self.Ui_IngameChess = Ui_IngameChess
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

        def whiteCD(self):
            self.timeWhite.setTime(self.timeWhite.time().addSecs(-1))

        def blackCD(self):
            self.timeBlack.setTime(self.timeBlack.time().addSecs(-1))

        def draw_board(self):
            # O tile'daki piece'i ekrana çiz
            for i in range(11, 100):
                try:
                    tile = getattr(self, "Tile_{}".format(i))
                    if tile.property("Piece") != '':
                        tile.setPixmap(QtGui.QPixmap(
                            Piece_Resource_Corresp[tile.property("Piece")]))
                    else:
                        tile.clear()
                except AttributeError:
                    pass

        def eventFilter(self, source, event):
            # Saha içinde mouse'a tıklandıysa
            if event.type() == QtCore.QEvent.MouseButtonPress and source in self.tiles:

                # Sol click ile tıklandıysa
                if event.button() == 1:
                    self.clicked_tile = source
                    posx, posy = int(self.clicked_tile.objectName()[-2]), \
                                 int(self.clicked_tile.objectName()[-1])
                    print(self.state.turn, self.state.action)
                    print("Coordinates:", posx, posy)

                    # Bir taşa bastıysam hold state'ine geçip ife giriyor
                    # Hold state'ine geçiş sonraki if'te (elif'te)
                    if self.state.action == "Hold":
                        self.state.action = "Wait"
                        piece_tile = self.get_last_clicked_tile()
                        destination_tile = getattr(self,
                                                   "Tile_{}{}".format(posx,
                                                                      posy))
                        print("attempt to move the piece",
                              piece_tile.property("Piece"), "at",
                              self.latest_click[0], self.latest_click[1],
                              "to ", posx, posy)
                        if self.latest_click == (posx, posy):
                            print("Piece unhold")
                        elif (posx, posy) in self.possible_moves:
                            self.piece_moved.emit(self.latest_click,
                                                  (posx, posy))
                            destination_tile.setProperty("Piece",
                                                         piece_tile.property(
                                                             "Piece"))
                            piece_tile.setProperty("Piece", '')
                            self.draw_board()
                            print("Changing turn")
                            self.change_turn()
                        else:
                            self.state.action = "Hold"
                        if self.state.action != "Hold":
                            for i in self.possible_moves:
                                tile = getattr(self,
                                               "Tile_{}{}".format(i.x, i.y))
                                self.toggle_highlight_tile(tile)
                    elif source.pixmap() is not None:
                        print("You are trying to move",
                              source.property("Piece"))
                        if source.property("Piece")[2] != self.state.turn[0]:
                            print("... which is not your piece.")
                        elif self.state.action == "Wait":
                            self.state.action = "Hold"
                            self.latest_click = (posx, posy)
                            self.mouse_clicked.emit(posx, posy)
                            for i in self.possible_moves:
                                tile = getattr(self,
                                               "Tile_{}{}".format(i.x, i.y))
                                self.toggle_highlight_tile(tile)
                            print("State changed to Hold")
            return super(WindowInGame, self).eventFilter(source, event)

        def get_last_clicked_tile(self):
            piece_tile = getattr(self, "Tile_{}{}".format(
                self.latest_click[0], self.latest_click[1]))
            return piece_tile

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

        def toggle_highlight_tile(self, tile):
            stylesheet_remapper = {
                "border-image: url(:/BG/resources/Wooden_noborder.jpg);": "border-image: url("
                                                                          ":/BG/resources/Wooden_selected.jpg);",
                "border-image: url(:/BG/resources/Wooden_selected.jpg);": "border-image: url("
                                                                          ":/BG/resources/Wooden_noborder.jpg);",
                "background-color: rgb(255, 255, 255);": "background-color: rgb(42, 192, 92);",
                "background-color: rgb(42, 192, 92);": "background-color: rgb(255, 255, 255);",
                "background-color: rgb(127, 127, 127);": "background-color: rgb(42, 191, 92);",
                "background-color: rgb(42, 191, 92);": "background-color: rgb(127, 127, 127);"
                }
            tile.setStyleSheet(stylesheet_remapper[tile.styleSheet()])
            pass

        def load_layout(self, layout):
            for i, line in enumerate(layout):
                for j, piece in enumerate(line):
                    print("Tile_{}{}".format(i + 1, j + 1), "set to", piece)
                    getattr(self,
                            "Tile_{}{}".format(i + 1, j + 1)).setProperty(
                        "Piece", piece)

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
        self.closeEvent = self.closeEvent

    def start_chess_game(self):
        self.w_w = in_game_wrapper(Ui_IngameChess, 8)()
        pawns = []
        for i in range(1, 9):
            w_pawn = pieces.WhitePawn(board=self.w_w, x=i, y=2,
                                      promotable=True)
            b_pawn = pieces.BlackPawn(board=self.w_w, x=i, y=7,
                                      promotable=True)
            pawns.append(w_pawn)
            pawns.append(b_pawn)

        bishops = [pieces.Bishop(board=self.w_w, x=3, y=1),
                   pieces.Bishop(board=self.w_w, x=6, y=1),
                   pieces.Bishop(board=self.w_w, x=3, y=8),
                   pieces.Bishop(board=self.w_w, x=6, y=8)]

        rooks = [pieces.Rook(board=self.w_w, x=1, y=1),
                 pieces.Rook(board=self.w_w, x=8, y=1),
                 pieces.Rook(board=self.w_w, x=1, y=8),
                 pieces.Rook(board=self.w_w, x=8, y=8)]
        self.w_w.show()
        self.hide()

        kings = [pieces.King(board=self.w_w, x=5, y=1),
                 pieces.King(board=self.w_w, x=5, y=8)]

        queens = [pieces.Queen(board=self.w_w, x=4, y=1),
                  pieces.Queen(self.w_w, 4, 8)]

        knights = [pieces.Knight(self.w_w, x=2, y=1),
                   pieces.Knight(self.w_w, x=7, y=1),
                   pieces.Knight(self.w_w, x=2, y=8),
                   pieces.Knight(self.w_w, x=7, y=8)]

    def start_shogi_game(self):
        w_w = in_game_wrapper(Ui_IngameShogi, 9)()
        w_w.show()
        self.hide()

    def start_hybrid_game(self):
        w_w = in_game_wrapper(Ui_IngameShogi, 9)()
        w_w.load_layout(chessVshogi.layouts.hybrid_default)
        w_w.draw_board()
        w_w.show()
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
    w_o = WindowOptsMenu()
    sys.exit(app.exec_())
