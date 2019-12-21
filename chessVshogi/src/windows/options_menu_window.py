from PyQt5.QtWidgets import QWidget
from chessVshogi.UI.options_menu import Ui_Options_Menu


class OptionsMenuWindow(QWidget, Ui_Options_Menu):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.buttonReturn.clicked.connect(self.parent().close)
