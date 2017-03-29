from PyQt5.QtCore import QModelIndex
from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QDoubleValidator
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtWidgets import QTableView,QStyledItemDelegate, QSpinBox
from PyQt5.QtWidgets import QWidget

from CRS import Parametrs
class ParamDelegate (QStyledItemDelegate):
    def __init__(self, param):
        super().__init__()
        self.param=param
    def createEditor(self, parent, QStyleOptionViewItem, QModelIndex):
        editor=QLineEdit(parent)

        validator = QDoubleValidator(0.99, 9999.99, 2)
        validator.setNotation(QDoubleValidator.StandardNotation)
        editor.setValidator(validator)
        editor.setAlignment(Qt.AlignRight)
        editor.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Expanding)
        #editor.t`
        #editor.setFrame(False)
        #editor.setMinimum(0)
        #editor.setMaximum(10000)
        #editor.setSingleStep(1)
        return editor

    def setEditorData(self, editor, index):
        value=index.model().data(index,Qt.EditRole)
        editor.setText(value)

    def setModelData(self, editor, model, index):

        value=editor.text()
        model.setData(index, value, Qt.EditRole)

        #editor.parentWidget().setParam(index.row(),value)
        self.param.ListIndexParam[index.row()].Value=float(value)

        self.param.Calc()





class ParamTableWiget(QTableView):
    #value_changed = pyqtSignal(object)

    def __init__(self, param, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.Param=param
        sti=QStandardItemModel(parent= self)
        #sti.event()
        for row in self.Param.List:
            itemName=QStandardItem(self.Param.List[row].Name)
            itemName.setEditable(False)
            itemName.setSelectable(False)
            #itemName.
            itemValue = QStandardItem(str(self.Param.List[row].Value))
            itemValue.setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter|Qt.AlignRight)

            itemEdIzm = QStandardItem(self.Param.List[row].Ed_izm)
            itemEdIzm.setEditable(False)
            itemEdIzm.setSelectable(False)

            #print (self.Param.List[row].Value)
            sti.appendRow([itemName,itemValue,itemEdIzm])
        sti.setHorizontalHeaderLabels(["Параметр", "Значение", "Ед.изм"])
        sti.setVerticalHeaderLabels(self.Param.List.keys())
        #print (sti.index())

        self.setModel(sti)
        self.setColumnWidth(0, 200)
        self.setColumnWidth(1, 70)
        self.setColumnWidth(2, 50)
        #self.setC`
        self.setItemDelegateForColumn(1,ParamDelegate(self.Param))
        #self.item
        #i=QModelIndex()
    def setParam (self):
        print ("dsdfds")
        #self.Param.ListIndexParam[index].Value=value
        """
    def edit(self, index, trigger, event):
        if self.edit(self, index, trigger, event):
            print ('editing:', index.row(), index.column())
            return True
        return False
        """
