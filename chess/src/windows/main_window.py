from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QStackedWidget
from chess.UI.ingame_chess import Ui_IngameChess

from chess.UI.mainwindow import Ui_MainWindow
from chess.src import layouts
from chess.src.windows.in_game_window import in_game_wrapper


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.stacked_widget = QStackedWidget()
        board_layout = Ui_IngameChess
        piece_layout = getattr(layouts,
                               "chess_default")
        window_in_game = in_game_wrapper(board_layout, piece_layout)()
        self.stacked_widget.addWidget(self.centralwidget)
        self.stacked_widget.addWidget(window_in_game)
        self.stacked_widget.setCurrentIndex(0)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.stacked_widget)
        central_widget = QtWidgets.QWidget(self)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        self.buttonStart.clicked.connect(
            lambda: self.stacked_widget.setCurrentIndex(1))
        self.buttonExit.clicked.connect(self.close)
        self.setWindowTitle("Chess")
        self.show()

    def closeEvent(self, event):
        current_index = self.stacked_widget.currentIndex()
        if current_index != 0:
            if current_index == 1:
                self.stacked_widget.currentWidget().restart_game()
            self.stacked_widget.setCurrentIndex(0)
            self.setWindowTitle("Chess")
            event.ignore()
        else:
            event.accept()


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication([])
    w = MainWindow()

    sys.exit(app.exec_())
