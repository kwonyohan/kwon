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
        self.action_korean.triggered.connect(self.korFunction)
        self.actionEnglish.triggered.connect(self.engFunction)
        self.actionmemoreader.triggered.connect(self.verFunction)
        self.savebutton.clicked.connect(self.saveFunction)
        self.tabWidget.tabBarClicked.connect(self.tabbarClicked)        
        self.opened = False
        self.opened_file_path = '제목 없음'
        self.enc = 'utf-8'
        self.viewenc = 'UTF-8'
        self.fdata = ''
        self.yesorno = 1
        self.lan = 0
        
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
        if self.lan == 0:
            msgBox.setText(" '메뉴바>열기'를 선택하여 파일을 불러온 후\n \
우측 창의 탭에 여러 인코딩 방식을 선택하며\n 알맞은 인코딩을 찾으시면 됩니다.\n \
우측 하단의 버튼을 통해 선택하신 인코딩 방식으로\n 파일을 다시 저장하실 수 있습니다.")
            msgBox.setWindowTitle("도움말 보기")
        else:
            msgBox.setText("Select 'Menu Bar>Open' to load the file,\n then select various encoding methods in the tab on the right window and find the appropriate encoding.\nYou can re-save the file using the selected encoding method by clicking the button in the lower right corner.")
            msgBox.setWindowTitle("Help Window")            
        msgBox.setIcon(QMessageBox.Question)        
        msgBox.exec_()
        
    def saveFunction(self):
        if self.opened == True:
            msgBox = QMessageBox()
            if self.lan == 0:
                msgBox.setText(self.viewenc + " 인코딩으로 다른이름으로 저장하시겠습니까?")
                msgBox.setWindowTitle("해당 인코딩으로 다른이름으로 저장")
            else:
                msgBox.setText("Save As with " + self.viewenc +" Encoding?")
                msgBox.setWindowTitle("Save As with that encoding")  
            msgBox.setStandardButtons(QMessageBox.No|QMessageBox.Yes)
            msgBox.buttonClicked.connect(self.popup_button)
            msgBox.exec_()
            if self.yesorno == 1:
                fname = QFileDialog.getSaveFileName(self)
                if fname[0]:
                    data = self.fdata.decode(self.enc, 'ignore')
                    with open(fname[0], 'w', encoding = self.enc) as f:
                        f.write(data)
                    self.console.append("Save file : " + fname[0] + " as " + self.viewenc +" encoding")
        if self.opened == False:
            msgBox = QMessageBox()
            if self.lan == 0:
                msgBox.setText("파일을 불러와주세요.(Ctrl+O)")
                msgBox.setWindowTitle("경고")
            else :
                msgBox.setText("Please load the file.(Ctrl+O)")
                msgBox.setWindowTitle("Warning")
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.exec_()
    
    def popup_button(self, dialog_button):
        print(dialog_button.text())
        if dialog_button.text() == "&Yes":
            self.yesorno = 1
        else:
            self.yesorno = 0       
        print(self.yesorno)     
            
    def verFunction(self):
        msgBox = QMessageBox()
        if self.lan == 0:
            msgBox.setWindowTitle("memoreader 정보")
        else :
            msgBox.setWindowTitle("memoreader Info")
        msgBox.setText("memoreader v0.5\n\n 2022.06.08.")
        msgBox.setIcon(QMessageBox.Information)
        msgBox.exec_()
            
    def tabbarClicked(self, index):
        print(index)
        if index == 0 :
            self.enc = 'utf-8'
            self.viewenc = 'UTF-8'
        elif index == 1 :
            self.enc = 'euc-kr'
            self.viewenc = 'EUC-KR'
        elif index == 2 :
            self.enc = 'cp949'
            self.viewenc = 'CP949'
        elif index == 3 :
            self.enc = 'ansi'
            self.viewenc = 'ANSI'
        elif index == 4 :
            self.enc = 'utf-16le'
            self.viewenc = 'UNICODE'
        else :
            self.enc = 'utf-16be'
            self.viewenc = 'UNICODE(big endian)'
            
    def korFunction(self):
        if self.lan == 1:
            self.console_label.setText("상태창")
            self.console_label_2.setText("불러온 파일 HEX 값")
            self.savebutton.setText("해당 인코딩으로 다른이름으로 저장")
            self.action_open.setText("열기")
            self.action_exit.setText("끝내기")
            self.action_help.setText("도움말 보기")
            self.actionmemoreader.setText("memoreader 정보")
            self.lan = 0
            
        
    def engFunction(self):
        if self.lan == 0:
            self.console_label.setText("console")
            self.console_label_2.setText("HEX value of the opened file")
            self.savebutton.setText("Save As with that encoding")
            self.action_open.setText("open")
            self.action_exit.setText("exit")
            self.action_help.setText("Help")
            self.actionmemoreader.setText("memoreader information")
            self.lan = 1
        
app = QApplication(sys.argv)
w = mainWindow()
w.show()
QApplication.processEvents()
sys.exit(app.exec_())       