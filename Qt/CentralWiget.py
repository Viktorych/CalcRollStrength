from PyQt5 import QtCore

from PyQt5 import QtWidgets

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *



from Qt import LogWiget


class CWG(QWidget):
    """Центральный вигет"""

    def __init__(self, param,parent=None):
        super().__init__(parent)
        self.param = param
        self.LogWiget= LogWiget.LogWiget(param)
        vbox = QVBoxLayout()


        vbox.addWidget(self.LogWiget)
        self.setLayout(vbox)
