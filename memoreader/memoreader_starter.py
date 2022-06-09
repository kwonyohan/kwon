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
                self.fdata = str(data)
                print(data.hex())
                self.hexview.setPlainText(data.hex(' ', 1)) 
                self.textviewer_euckr.setPlainText(data.decode('euc_kr', 'ignore'))
                self.textviewer_utf8.setPlainText(data.decode('utf-8', 'ignore'))
                self.textviewer_cp949.setPlainText(data.decode('cp949', 'ignore'))
                self.textviewer_ansi.setPlainText(data.decode('ansi', 'ignore'))
                self.textviewer_unicode.setPlainText(data.decode('utf-16le', 'ignore'))
                self.textviewer_unicode_2.setPlainText(data.decode('utf-16be', 'ignore'))
                self.opened_file_path = fname
                self.opened = True
                if "efbfbdefbfbd" in data.hex():
                    self.console.append("Found '占쏙옙(ï¿½)' in the file (efbfbdefbfbd)")
                    msgBox = QMessageBox()
                    if self.lan == 0:
                        msgBox.setText("해당 파일은 '占쏙옙'이 일어난 훼손된 파일일 수 있으며 \n어떤 인코딩으로도 원본을 볼 수 없음을 경고합니다.")
                        msgBox.setWindowTitle("손상된 파일 경고")
                        msgBox.setDetailedText("해당 파일의 HEX값에 EF BF BD EF BF BD(占쏙옙) 값이 반복되어 나타나 있다면 UTF-8로 저장하는 과정 중 오류가 발생한 손상된 문서로 어떤 방식을 통해서도 원본 복구가 불가능함을 알림니다.")
                    else:
                        msgBox.setText("It warns you that the file may be corrupted with an 'ï¿½' \nand that the original cannot be viewed in any encoding.")
                        msgBox.setWindowTitle("Critical Message")
                        msgBox.setDetailedText("If the EF BF BD EF BF BD(ï¿½) value is repeatedly displayed in the HEX value of the file, it is a damaged document that has an error during the process of saving in UTF-8 and it is not possible to recover the original through any method.")
                    msgBox.setIcon(QMessageBox.Critical)
                    msgBox.exec_()                    
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
            msgBox.setWindowTitle("Memoreader 정보")
        else :
            msgBox.setWindowTitle("Memoreader Info")
        msgBox.setText("Memoreader v0.5\n\n 2022.06.08.")
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
            self.menu_file.setTitle("파일")
            self.menu_help.setTitle("도움말")
            self.action_open.setText("열기")
            self.action_exit.setText("끝내기")
            self.action_help.setText("도움말 보기")
            self.actionmemoreader.setText("Memoreader 정보")
            self.lan = 0
            
        
    def engFunction(self):
        if self.lan == 0:
            self.console_label.setText("Console")
            self.console_label_2.setText("HEX value of the opened file")
            self.savebutton.setText("Save As with that encoding")
            self.menu_file.setTitle("File")
            self.menu_help.setTitle("Help")
            self.action_open.setText("Open")
            self.action_exit.setText("Exit")
            self.action_help.setText("Get Help")
            self.actionmemoreader.setText("Memoreader information")
            self.lan = 1
        
app = QApplication(sys.argv)
w = mainWindow()
w.show()
QApplication.processEvents()
sys.exit(app.exec_())       