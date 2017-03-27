from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction, qApp
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtWidgets import QMessageBox
#from App import App_Variable
from Qt import CentralWiget
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

class MainWindow(QMainWindow):
    """Главное окно приложения"""
    def __init__(self):
        super().__init__()
        self.setAction()
        self.setMenuBar()
        self.setToolBar()
        self.setGeometry(300, 300, 1200, 600)
        self.setWindowTitle('Программа рассчета валка на прочность')
        self.statusBar().showMessage('Готово')
        self.setWindowIcon(QIcon('Images/app_icon.png'))  # App Icon

        #self.Variables = Variables
        #print (self.Variable.)
        self.CentralWG=CentralWiget.CWG()
        self.setCentralWidget(self.CentralWG)

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

        self.savePDFFileAction = QAction(QIcon('Images/PDF.jpg'), 'Сохранить расчет в PDF', self)
        # self.savePDFFileAction.setShortcut('Ctrl+Q')
        self.savePDFFileAction.setStatusTip('Сохранить условия в файл')
        self.savePDFFileAction.triggered.connect(self.SavePDF)


        self.settingAction = QAction(QIcon('Images/setting.png'), 'Насторойки', self)
        # self.settingAction.setShortcut('Ctrl+Q')
        self.settingAction.setStatusTip('Насторойки программы')
        self.settingAction.triggered.connect(self.Setting)

        self.printAction = QAction(QIcon('Images/print.png'), 'Печать', self)
        # self.printAction.setShortcut('Ctrl+Q')
        self.printAction.setStatusTip('Печать')
        # self.printAction.triggered.connect(qApp.quit)

    def setMenuBar(self):
        """определение Меню бара"""
        self.menubar = self.menuBar()
        fileMenu = self.menubar.addMenu('Файл')
        viewMenu = self.menubar.addMenu('Вид')
        settingMenu = self.menubar.addMenu('Настройка')
        helpMenu = self.menubar.addMenu('Помощь')
        """Меню Файл"""
        fileMenu.addAction(self.newFileAction)
        fileMenu.addAction(self.openFileAction)
        fileMenu.addAction(self.saveFileAction)
        fileMenu.addAction(self.savePDFFileAction)
        fileMenu.addSeparator()
        fileMenu.addAction(self.printAction)
        fileMenu.addSeparator()
        fileMenu.addAction(self.settingAction)
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
        self.toolbar.addAction(self.savePDFFileAction)
        self.toolbar.addAction(self.settingAction)
        self.toolbar.addAction(self.printAction)
        self.toolbar.addAction(self.exitAction)

    def about(self):
        # QMessageBox.about (QWidget parent, QString caption, QString text)
        QMessageBox.about(self, 'О программе',
                          '''О программе.<br />
                              Программа расчета валка на прочность''')

    def Setting (self):
        pass
        #self.CentralWG.LogWiget.add(self.Variables.info(),0)

    def Save (self):
        _fname = QFileDialog.getSaveFileName(self, "Сохранить файл", "Расчет.pickle", filter="*.pickle")
        if _fname[0]:
            f = open(_fname[0], 'wb')
            #self.Variables.save(f)
            f.close()
            self.CentralWG.LogWiget.add("Файл {} сохранен.".format(f.name),1)

    def Load(self):


        fname = QFileDialog.getOpenFileName(self, 'Открыть файл', '',"*.pickle")

        if fname[0]:
            f = open(fname[0], 'rb')
            #self.Variables.load(f)
            f.close()
            #print ("load  \n",self.Variables)
            #self.CentralWG.treeview.Variables=self.Variables
            #print ("set ver \n",self.CentralWG.treeview.Variables)
            #self.CentralWG.treeview.reload()
            #self.CentralWG.LogWiget.add("Файл {} загружен.".format(f.name),1)
    def SavePDF (self):
        #f = QFileDialog.getSaveFileName(self, "Сохранить файл", "Расчет.pdf", filter="*.pdf")
        #print (f)
        from reportlab.pdfgen import canvas
        canvas = canvas.Canvas("form.pdf", pagesize=letter)
        canvas.setLineWidth(.3)
        canvas.setFont('Helvetica', 12)

        canvas.drawString(30, 750, 'Расчеты')
        canvas.drawString(30, 735, 'OF ACME INDUSTRIES')
        canvas.drawString(500, 750, "12/12/2010")
        canvas.line(480, 747, 580, 747)

        canvas.drawString(275, 725, 'AMOUNT OWED:')
        canvas.drawString(500, 725, "$1,000.00")
        canvas.line(378, 723, 580, 723)

        canvas.drawString(30, 703, 'RECEIVED BY:')
        canvas.line(120, 700, 580, 700)
        canvas.drawString(120, 703, "JOHN DOE")

        canvas.save()
        #self.CentralWG.LogWiget.add("Файл {} сохранен.".format(f[0]), 1)



