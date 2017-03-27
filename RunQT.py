from PyQt5.QtWidgets import QApplication
from Qt import Window
from CRS import Parametrs

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    param=Parametrs.Рarameters()
    #print (QStyleFactory.keys())
    # qApp.setStyle(QStyleFactory.create("Fusion"))
    #
    # dark_palette = App_dark_palette.dark_palette()
    # qApp.setPalette(dark_palette)
    # qApp.setStyleSheet("QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }")

    app.setStyle("Fusion")
    window = Window.MainWindow(param)

    window.show()

    sys.exit(app.exec_())