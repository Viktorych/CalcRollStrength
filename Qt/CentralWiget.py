from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget
import time
import locale
locale.setlocale(locale.LC_ALL, "Russian_Russia.1251")

from Qt.ParametrsWiget import ParamTableWiget


class CWG(QWidget):
    """Центральный вигет"""

    def __init__(self, param,win,parent=None):
        super().__init__(parent)
        self.param = param
        self.ParamTableWiget= ParamTableWiget(param,self)
        win.setParamTable(self.ParamTableWiget)
        hbox = QHBoxLayout()
        vbox = QVBoxLayout()
        bCalc = QPushButton('Расчет', self)
        self.Report= QTextEdit(self)
        bCalc.clicked[bool].connect(self.Calc)
        vbox.addWidget(self.ParamTableWiget)
        vbox.addWidget(bCalc)
        hbox.addLayout(vbox)
        hbox.addWidget(self.Report)
        self.setLayout(hbox)
        self.Calc()
    def Calc (self):
        self.param.Calc()
        self.Report.clear()
        self.Report.append ("<b style='color:#ff0000'>Время расчета: {}</span></b>".format(time.strftime("%c")))
        self.Report.append (self.param.strWin())
