# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'memoreaderui.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(847, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.console = QtWidgets.QTextBrowser(self.centralwidget)
        self.console.setGeometry(QtCore.QRect(10, 490, 401, 61))
        self.console.setObjectName("console")
        self.console_label = QtWidgets.QLabel(self.centralwidget)
        self.console_label.setGeometry(QtCore.QRect(10, 470, 77, 18))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.console_label.setFont(font)
        self.console_label.setObjectName("console_label")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(430, 10, 411, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.utp8 = QtWidgets.QWidget()
        self.utp8.setEnabled(True)
        font = QtGui.QFont()
        font.setKerning(True)
        self.utp8.setFont(font)
        self.utp8.setAccessibleName("")
        self.utp8.setStyleSheet("")
        self.utp8.setObjectName("utp8")
        self.tabWidget.addTab(self.utp8, "")
        self.euckr = QtWidgets.QWidget()
        self.euckr.setObjectName("euckr")
        self.tabWidget.addTab(self.euckr, "")
        self.cp949 = QtWidgets.QWidget()
        self.cp949.setObjectName("cp949")
        self.tabWidget.addTab(self.cp949, "")
        self.ansi = QtWidgets.QWidget()
        self.ansi.setObjectName("ansi")
        self.tabWidget.addTab(self.ansi, "")
        self.unicode = QtWidgets.QWidget()
        self.unicode.setObjectName("unicode")
        self.tabWidget.addTab(self.unicode, "")
        self.hex = QtWidgets.QWidget()
        self.hex.setObjectName("hex")
        self.tabWidget.addTab(self.hex, "")
        self.hexview = QtWidgets.QTextEdit(self.centralwidget)
        self.hexview.setGeometry(QtCore.QRect(10, 30, 411, 421))
        self.hexview.setObjectName("hexview")
        self.textviewer = QtWidgets.QTextBrowser(self.centralwidget)
        self.textviewer.setGeometry(QtCore.QRect(430, 30, 411, 521))
        self.textviewer.setObjectName("textviewer")
        self.tabWidget.raise_()
        self.console.raise_()
        self.console_label.raise_()
        self.hexview.raise_()
        self.textviewer.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 847, 21))
        self.menubar.setObjectName("menubar")
        self.menu_file = QtWidgets.QMenu(self.menubar)
        self.menu_file.setObjectName("menu_file")
        self.menu_help = QtWidgets.QMenu(self.menubar)
        self.menu_help.setObjectName("menu_help")
        self.menu_Language = QtWidgets.QMenu(self.menubar)
        self.menu_Language.setObjectName("menu_Language")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_open = QtWidgets.QAction(MainWindow)
        self.action_open.setObjectName("action_open")
        self.action_save = QtWidgets.QAction(MainWindow)
        self.action_save.setObjectName("action_save")
        self.action_korean = QtWidgets.QAction(MainWindow)
        self.action_korean.setObjectName("action_korean")
        self.actionEnglish = QtWidgets.QAction(MainWindow)
        self.actionEnglish.setObjectName("actionEnglish")
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.actionmemoreader = QtWidgets.QAction(MainWindow)
        self.actionmemoreader.setObjectName("actionmemoreader")
        self.menu_file.addAction(self.action_open)
        self.menu_file.addAction(self.action_save)
        self.menu_help.addAction(self.action)
        self.menu_help.addAction(self.actionmemoreader)
        self.menu_Language.addAction(self.action_korean)
        self.menu_Language.addAction(self.actionEnglish)
        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_help.menuAction())
        self.menubar.addAction(self.menu_Language.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "memoreader"))
        self.console_label.setText(_translate("MainWindow", "상태창"))
        self.utp8.setToolTip(_translate("MainWindow", "<html><head/><body><p>야<br/></p></body></html>"))
        self.utp8.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.utp8), _translate("MainWindow", "UTF-8"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.euckr), _translate("MainWindow", "EUC-KR"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.cp949), _translate("MainWindow", "CP949"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ansi), _translate("MainWindow", "ANSI"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.unicode), _translate("MainWindow", "UNICODE"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.hex), _translate("MainWindow", "HEX"))
        self.menu_file.setTitle(_translate("MainWindow", "파일"))
        self.menu_help.setTitle(_translate("MainWindow", "도움말"))
        self.menu_Language.setTitle(_translate("MainWindow", "언어(Language)"))
        self.action_open.setText(_translate("MainWindow", "열기"))
        self.action_open.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.action_save.setText(_translate("MainWindow", "저장"))
        self.action_save.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.action_korean.setText(_translate("MainWindow", "한국어"))
        self.actionEnglish.setText(_translate("MainWindow", "English"))
        self.action.setText(_translate("MainWindow", "\n"
"도움말 보기"))
        self.actionmemoreader.setText(_translate("MainWindow", "memoreader 정보"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())



"""
삽질하던거
import os
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType(os.getcwd()+"\memoreader\\memoreaderui.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi(self)
        
       

app = QApplication(sys.argv)
mainWindow = WindowClass()
mainWindow.show()
sys.exit(app.exec_())
"""