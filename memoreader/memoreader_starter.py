import sys
import binascii #바이너리 아스키출력
#import os
from memoreader import Ui_MainWindow
from PyQt5 import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
#os.system('chcp 949')

class mainWindow(QMainWindow, Ui_MainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.setupUi(self)
        
        self.action_open.triggered.connect(self.openFunction)
        
    def openFunction(self):
        fname = QFileDialog.getOpenFileName(self)
        binAllString =""
        with open(fname[0], "r") as f:
            data = f.read()
        #tohex = binascii.b2a_hex(data)
        self.hexview.setPlainText(data)
        self.console.setPlainText(fname[0])
        self.console.setPlainText("open!")
        
        
    
app = QApplication([])
w = mainWindow()
w.show()
QApplication.processEvents()
sys.exit(app.exec_())       

"""    def openFunction(self):
        fname = QFileDialog.getOpenFileName(self)
        print(fname[0])
        self.console.append("file open!")
        print("open!!")
        pass
        """