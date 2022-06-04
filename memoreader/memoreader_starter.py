import sys
from memoreader import Ui_MainWindow
from PyQt5 import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class mainWindow(QMainWindow, Ui_MainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.setupUi(self)
        
        self.show()
    
app = QApplication([])
w = mainWindow()
QApplication.processEvents()
sys.exit(app.exec_())       
    
"""        
def openFunction(self):
    fname = QFileDialog.getOpenFileName(self)
    print(fname[0])
    print("open!!")
"""    