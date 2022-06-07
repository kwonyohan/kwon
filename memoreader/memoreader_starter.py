import sys
from memoreader import Ui_MainWindow
from PyQt5 import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic

class mainWindow(QMainWindow, Ui_MainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.setupUi(self)
        
        self.action_open.triggered.connect(self.openFunction)
        self.action_exit.triggered.connect(self.exitFunction)
        
        
    def openFunction(self):
        fname = QFileDialog.getOpenFileName(self)
        binAllString =""
        with open(fname[0], "rb") as f:
            data = f.read()
            self.hexview.setPlainText(str(data)) 
            self.textviewer_euckr.setPlainText(data.decode('euc_kr', 'ignore'))
            self.textviewer_utf8.setPlainText(data.decode('utf-8', 'ignore'))
            self.textviewer_cp949.setPlainText(data.decode('cp949', 'ignore'))
            self.textviewer_ansi.setPlainText(data.decode('ansi', 'ignore'))
            self.textviewer_unicode.setPlainText(data.decode('utf-16le', 'ignore'))
            self.textviewer_unicode_2.setPlainText(data.decode('utf-16be', 'ignore'))
        print(fname[0])
        print("open!!")
        self.console.setPlainText(fname[0] +"  file open")
    
    def exitFunction(selt):
        print(exit)
        
    
app = QApplication([])
w = mainWindow()
w.show()
QApplication.processEvents()
sys.exit(app.exec_())       