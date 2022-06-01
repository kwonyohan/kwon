import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import uic


class memoreaderui(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("memoreaderui.ui")
        
       
if __name__ == '__main__':
    app = QApplication(sys.argv)
    memoreaderui = memoreaderui()
    memoreaderui.show()
    sys.exit(app.exec_())