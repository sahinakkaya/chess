from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QStackedWidget

from chessVshogi.UI.mainwindow import Ui_MainWindow
from chessVshogi.src.windows.game_mode_window import GameModeWindow
from chessVshogi.src.windows.options_menu_window import OptionsMenuWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.stacked_widget = QStackedWidget()
        game_mode_window = GameModeWindow(self)
        options_menu_window = OptionsMenuWindow(self)
        self.stacked_widget.addWidget(self.centralwidget)
        self.stacked_widget.addWidget(game_mode_window)
        self.stacked_widget.addWidget(options_menu_window)
        self.stacked_widget.setCurrentIndex(0)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.stacked_widget)
        central_widget = QtWidgets.QWidget(self)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        self.buttonStart.clicked.connect(
            lambda: self.stacked_widget.setCurrentIndex(1))
        self.buttonOpts.clicked.connect(
            lambda: self.stacked_widget.setCurrentIndex(2))
        self.buttonExit.clicked.connect(self.close)
        self.show()

    def closeEvent(self, event):
        current_index = self.stacked_widget.currentIndex()
        if current_index != 0:
            if current_index == 3:
                self.stacked_widget.removeWidget(self.stacked_widget.currentWidget())
            self.stacked_widget.setCurrentIndex(0)
            event.ignore()
        else:
            event.accept()


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication([])
    w = MainWindow()

    sys.exit(app.exec_())
