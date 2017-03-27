from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QColor
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtWidgets import QWidget
from CRS import Parametrs

class LogWiget(QWidget):
    value_changed = pyqtSignal(object)

    def __init__(self, param, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.textEdit = QTextEdit(self)
        self.Param=param
        self.Param.Calc()
        self.textEdit.setStyleSheet("background: grey")
        #self.textEdit.setText("<b style='color:#ffFF00'>Cтарт приложения</span></b>")
        #self.textEdit.append("<b style='color:#ff0000'>Другой текст</span></b>")
        self.add("Cтарт приложения",2)
        _vbox = QHBoxLayout()

        _vbox.addWidget(self.textEdit)

        self.setLayout(_vbox)
        self.add (self.Param.strWin(),0)


    def add(self, txt, color):
        colors = {0: "<b style='color:#ff0000'>{}</span></b>", \
                  1: "<b style='color:#00ff00'>{}</span></b>", \
                  2: "<b style='color:#0000ff'>{}</span></b>"}

        #self.LogWiget.add(colors[color].format(txt))
        #print (txt)
        self.textEdit.append(colors[color].format(txt))
