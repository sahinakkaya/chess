from PyQt5.QtWidgets import QWidget
from chessVshogi.UI.options_menu import Ui_Options_Menu
import chessVshogi.src.ui_mapper as ui_mapper


class OptionsMenuWindow(QWidget, Ui_Options_Menu):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.buttonReturn.clicked.connect(self.parent().close)
        self.PG_ChessStyle.clicked.connect(lambda: self.set_piece_style(ui_mapper.hidetchi_prefix))
        self.PG_ShogiStyle.clicked.connect(lambda: self.set_piece_style(ui_mapper.ichiji_prefix))

    def set_piece_style(self, selection):
        ui_mapper.prefix = selection
        pass
