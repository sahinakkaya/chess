from chessVshogi.src.windows.main_window import MainWindow
from PyQt5 import QtWidgets

if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication([])
    w = MainWindow()
    sys.exit(app.exec_())
