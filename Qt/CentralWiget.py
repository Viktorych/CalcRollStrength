from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QSplitter
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
        self.Report = QTextEdit(self)
        font = QFont()
        font.setPointSize(12)
        self.Report.setFont(font)
        win.setParamTable(self.ParamTableWiget, self.Report)

        hbox = QHBoxLayout()
        #vbox = QVBoxLayout()

        splitterH = QSplitter(Qt.Horizontal)
        splitterH.addWidget(self.ParamTableWiget)
        splitterH.addWidget(self.Report)
        #splitterH.scroll(200,500)
        splitterH.setSizes([300,500])
        sp = splitterH.sizePolicy()
        sp.setVerticalPolicy(QSizePolicy.Expanding)
        splitterH.setSizePolicy(sp)

        #hbox = QHBoxLayout()
        # vbox.addStretch(1)
        hbox.addWidget(splitterH)


        #bCalc = QPushButton('Расчет', self)

        #bCalc.clicked[bool].connect(self.Calc)
        #vbox.addWidget(self.ParamTableWiget)
        #vbox.addWidget(bCalc)
        #hbox.addLayout(vbox)
        #hbox.addWidget(self.Report)
        self.setLayout(hbox)
        self.Calc()
    def Calc (self):
        self.param.Calc()
        self.Report.clear()
        #self.Report.append ('<b> Отчет по вычислениям</b>')

        self.Report.append ('<b style="color:#ff0000">Отчет по вычислениям: {}</span></b>'.format(time.strftime("%c")))
        self.Report.append (self.param.strWin())
