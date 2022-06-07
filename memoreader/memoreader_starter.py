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
        self.action_exit.triggered.connect(self.close)
        self.action_help.triggered.connect(self.helpFunction)
        self.savebutton.clicked.connect(self.saveFunction)
        self.tabWidget.tabBarClicked.connect(self.tabbarClicked)        
        self.opened = False
        self.opened_file_path = '제목 없음'
        self.enc = 'utf-8'
        self.fdata = ''
        
    def openFunction(self):
        fname = QFileDialog.getOpenFileName(self)
        if fname[0]:
            with open(fname[0], "rb") as f:
                data = f.read()
                self.fdata = data
                self.hexview.setPlainText(str(data)) 
                self.textviewer_euckr.setPlainText(data.decode('euc_kr', 'ignore'))
                self.textviewer_utf8.setPlainText(data.decode('utf-8', 'ignore'))
                self.textviewer_cp949.setPlainText(data.decode('cp949', 'ignore'))
                self.textviewer_ansi.setPlainText(data.decode('ansi', 'ignore'))
                self.textviewer_unicode.setPlainText(data.decode('utf-16le', 'ignore'))
                self.textviewer_unicode_2.setPlainText(data.decode('utf-16be', 'ignore'))
                self.opened_file_path = fname
                self.opened = True
            print(fname[0])
            print("open!!")
            self.console.append("open file : " + fname[0])
        
    def closeEvent(selt, event):
        print("exit")
    
    def helpFunction(self):
        msgBox = QMessageBox()
        msgBox.setText(" '메뉴바>열기'를 선택하여 파일을 불러온 후/n \
            우측 창의 탭에 여러 인코딩 방식을 선택하며 알맞은 인코딩을 찾으시면 됩니다./n \
            우측 하단의 버튼을 통해 선택하신 인코딩 방식으로 파일을 다시 저장하실 수 있습니다.")
        msgBox.addButton()
        
    def saveFunction(self):
        if self.opened == True:
            fname = QFileDialog.getSaveFileName(self)
            if fname[0]:
                data = self.fdata.decode(self.enc, 'ignore')
                with open(fname[0], 'w', encoding = self.enc) as f:
                    f.write(data)
                self.console.append("Save file : " + fname[0] + " as " + self.enc +" encoding")
        #if self.opened == False:
        #    msgBox = self.QMessageBox()
        #    msgBox.setText("파일을 불러와주세요.(Ctrl+O)")
        #    msgBox.set()
        #    msgBox.exec_()
            
            
    def tabbarClicked(self, index):
        print(index)
        if index == 0 :
            self.enc = 'utf-8'
        elif index == 1 :
            self.enc = 'euc-kr'
        elif index == 2 :
            self.enc = 'cp949'
        elif index == 3 :
            self.enc = 'ansi'
        elif index == 4 :
            self.enc = 'utf-16le'
        else :
            self.enc = 'utf-16be'
        
app = QApplication(sys.argv)
w = mainWindow()
w.show()
QApplication.processEvents()
sys.exit(app.exec_())       