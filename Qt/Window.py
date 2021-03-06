

from PyQt5.QtGui import QIcon,QPageLayout,QPainter

from PyQt5.QtPrintSupport import QPrinter, QPrintPreviewDialog
from PyQt5.QtWidgets import QAction, qApp
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import  QtPrintSupport


from Qt import CentralWiget


class MainWindow(QMainWindow):
    """Главное окно приложения"""
    def __init__(self, param):
        super().__init__()
        self.param=param
        self.setAction()
        self.setMenuBar()
        self.setToolBar()
        self.setGeometry(200, 200, 1200, 800)
        self.setWindowTitle('Программа рассчета валка на прочность')
        self.statusBar().showMessage('Готово')
        self.setWindowIcon(QIcon('Images/app_icon.png'))  # App Icon
        self.printer=QtPrintSupport.QPrinter()
        self.printer.setPageOrientation(QPageLayout.Landscape)
        #self.Variables = Variables
        #print (self.Variable.)
        self.CentralWG=CentralWiget.CWG(self.param, self)
        self.setCentralWidget(self.CentralWG)
        #self.resultTE =QTextEdit()
    def setAction(self):
        self.exitAction = QAction(QIcon('Images/Exit.png'), 'Выход', self)
        self.exitAction.setShortcut('Ctrl+Q')
        self.exitAction.setStatusTip('Выход из приложения')
        self.exitAction.triggered.connect(qApp.quit)

        self.aboutAction = QAction(QIcon('Images/About.png'), 'О программе', self)
        #self.aboutexitAction.setShortcut('Ctrl+Q')
        self.aboutAction.setStatusTip('О программе')
        self.aboutAction.triggered.connect(self.about)

        self.helpAction = QAction(QIcon('Images/Help.png'), 'Помощь', self)
        # self.helpAction.setShortcut('Ctrl+Q')
        self.helpAction.setStatusTip('Помощь')
        # self.helpAction.triggered.connect(qApp.quit)

        self.newFileAction = QAction(QIcon('Images/new.png'), 'Новый', self)
        # self.newFileAction.setShortcut('Ctrl+Q')
        self.newFileAction.setStatusTip('Новый файл')
        # self.newFileAction.triggered.connect(qApp.quit)

        self.openFileAction = QAction(QIcon('Images/Open.png'), 'Загрузить условия', self)
        # self.openFileAction.setShortcut('Ctrl+Q')
        self.openFileAction.setStatusTip('Загрузить условия из файла')
        self.openFileAction.triggered.connect(self.Load)


        self.saveFileAction = QAction(QIcon('Images/Save.png'), 'Сохранить условаия', self)
        # self.saveFileAction.setShortcut('Ctrl+Q')
        self.saveFileAction.setStatusTip('Сохранить условия в файл')
        self.saveFileAction.triggered.connect(self.Save)

        self.savePDFFileAction = QAction(QIcon('Images/PDF.jpg'), 'Сохранить расчет в TXT', self)
        # self.savePDFFileAction.setShortcut('Ctrl+Q')
        self.savePDFFileAction.setStatusTip('Сохранить расчет в файл')
        self.savePDFFileAction.triggered.connect(self.filePrintPdf)

        self.saveTXTFileAction = QAction(QIcon('Images/savetotxt.jpg'), 'Сохранить расчет в TXT', self)
        # self.savePDFFileAction.setShortcut('Ctrl+Q')
        self.saveTXTFileAction.setStatusTip('Сохранить расчет в файл')
        self.saveTXTFileAction.triggered.connect(self.SaveTXT)


        self.settingAction = QAction(QIcon('Images/setting.png'), 'Насторойки', self)
        # self.settingAction.setShortcut('Ctrl+Q')
        self.settingAction.setStatusTip('Насторойки программы')
        self.settingAction.triggered.connect(self.Setting)

        self.printAction = QAction(QIcon('Images/print.png'), 'Печать', self)
        # self.printAction.setShortcut('Ctrl+Q')
        self.printAction.setStatusTip('Печать')
        self.printAction.triggered.connect(self.preview)

    def setMenuBar(self):
        """определение Меню бара"""
        self.menubar = self.menuBar()
        fileMenu = self.menubar.addMenu('Файл')
        #viewMenu = self.menubar.addMenu('Вид')
        #settingMenu = self.menubar.addMenu('Настройка')
        helpMenu = self.menubar.addMenu('Помощь')
        """Меню Файл"""
        fileMenu.addAction(self.newFileAction)
        fileMenu.addAction(self.openFileAction)
        fileMenu.addAction(self.saveFileAction)
        fileMenu.addAction(self.saveTXTFileAction)
        fileMenu.addAction(self.savePDFFileAction)
        fileMenu.addSeparator()
        fileMenu.addAction(self.printAction)
        fileMenu.addSeparator()
        #fileMenu.addAction(self.settingAction)
        fileMenu.addSeparator()
        fileMenu.addAction(self.exitAction)
        """Меню Помощь"""
        helpMenu.addAction(self.helpAction)
        fileMenu.addSeparator()
        helpMenu.addAction(self.aboutAction)

    def setToolBar(self):
        """Определение тулбара"""
        self.toolbar = self.addToolBar('Файл')
        #self.toolbar = self.addToolBar('Setting')
        self.toolbar.addAction(self.openFileAction)
        self.toolbar.addAction(self.saveFileAction)
        self.toolbar.addAction(self.saveTXTFileAction)
        self.toolbar.addAction(self.savePDFFileAction)

        #self.toolbar.addAction(self.settingAction)
        self.toolbar.addAction(self.printAction)
        self.toolbar.addAction(self.exitAction)

    def about(self):
        # QMessageBox.about (QWidget parent, QString caption, QString text)
        QMessageBox.about(self, 'О программе',
                          '''О программе.<br />
                              Программа расчета валка на прочность''')

    def Setting (self):
        self.param.Calc()
        print (self.param)

        #self.CentralWG.LogWiget.add(self.Variables.info(),0)

    def Save (self):
        _fname = QFileDialog.getSaveFileName(self, "Сохранить файл", "Расчет.pickle", filter="*.pickle")
        if _fname[0]:
            f = open(_fname[0], 'wb')
            self.param.Save(f)
            #self.Variables.save(f)
            f.close()
            #self.CentralWG.LogWiget.add("Файл {} сохранен.".format(f.name),1)

    def Load(self):


        fname = QFileDialog.getOpenFileName(self, 'Открыть файл', '',"*.pickle")

        if fname[0]:
            f = open(fname[0], 'rb')
            self.param.Load(f)

            self.ParamTableWG.setmodel()
            self.CentralWG.Calc()
            #self.Variables.load(f)
            f.close()
            #print ("load  \n",self.Variables)
            #self.CentralWG.treeview.Variables=self.Variables
            #print ("set ver \n",self.CentralWG.treeview.Variables)
            #self.CentralWG.treeview.reload()
            #self.CentralWG.LogWiget.add("Файл {} загружен.".format(f.name),1)
    def SaveTXT (self):
        fname = QFileDialog.getSaveFileName(self, "Сохранить файл", "Расчет.txt", filter="*.txt")
        f = open(fname[0], 'wb')
        self.param.SaveResult(f.name)
        # self.Variables.save(f)
        f.close()

        #self.param.SaveResult

    def setParamTable (self, paramtablewg, resultte):
        self.ParamTableWG=paramtablewg
        self.resultTE=resultte

    def preview (self):
        printer = QPrinter(QPrinter.HighResolution)
        preview = QPrintPreviewDialog(printer, self)
        preview.paintRequested.connect(self.printPreview)
        preview.exec_()



    def printPreview(self, printer):
        self.resultTE.document().print_(printer)

    def filePrintPdf(self):
        #fn, _ = QFileDialog.getSaveFileName(self, "Экспорт в PDF", None,
#                                            "PDF files (*.pdf);;All Files (*)")

        #if fn:
            #if QFileInfo(fn).suffix().isEmpty():
                #fn += '.pdf'


        """
        writer=QPdfWriter("test.pdf")
        writer.setCreator("программа расчета валка на прочность")
        writer.setTitle("программа расчета валка на прочность")
        painter=QPainter()
        painter.begin(writer)
        pen = QPen(Qt.SolidLine)
        pen.setColor(Qt.black)
        pen.setWidth(2)
        painter.setPen(pen)
        painter.drawLine(20, 0, 20, 100)
        painter.drawText(100, 100, 100, 100, Qt.AlignLeft, "ssssss")
        painter.drawLine(10,10,30,30)
        painter.end()
        
        
        """
            #painter= self.resultTE.
            #printer = QPrinter(QPrinter.HighResolution)
            #printer.setOutputFormat(QPrinter.PdfFormat)
            #printer.setOutputFileName(fn)
            #self.resultTE.document.print_(printer)
        filename = QFileDialog.getSaveFileName(self, "Экспорт в PDF", None,\
                                            "PDF files (*.pdf);;All Files (*)")
        #print (filename)
        w=True
        try:
            filehandle = open(filename[0], 'w')
            filehandle.close()
        except IOError:
            print('Unable to write to file ' + filename[0])
            w=False
        #if os.access(filename[0], os.W_OK):
            #pass
            #print ("Можно писать")
        #else:
            #pass
           #print("Нельзя писать")
        if w:
            printer = QPrinter(QPrinter.HighResolution)
            printer.setPageSize(QPrinter.A4)
            printer.setColorMode(QPrinter.Color)
            printer.setOutputFormat(QPrinter.PdfFormat)
            printer.setOutputFileName(filename[0])
            self.resultTE.document().print_(printer)
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Ошибка записи в файл")
            msg.setInformativeText('Не возможно записать в файл <br>{} '.format(filename[0]))
            msg.setWindowTitle("Не возможно записать в файл")
            msg.setDetailedText("{} Возможно открыт в другой программе".format(filename[0]))
            msg.setStandardButtons(QMessageBox.Ok )
            msg.exec()




