from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget



from Qt.ParametrsWiget import ParamTableWiget


class CWG(QWidget):
    """Центральный вигет"""

    def __init__(self, param,parent=None):
        super().__init__(parent)
        self.param = param
        self.ParamTableWiget= ParamTableWiget(param)
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
    def Calc (self):
        self.param.Calc()
        self.Report.clear()
        self.Report.append (self.param.strWin())
