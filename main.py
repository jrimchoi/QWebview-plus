#!/usr/bin/env python
#-*-coding: utf-8 -*-
import sys
import os.path
import re
from optparse import OptionParser
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QFileDialog, qApp, QAction, QMainWindow, QStatusBar, QVBoxLayout, QSplitter, QMessageBox
from plus.kiwoom import KiwoomWebViewPlus

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.view = KiwoomWebViewPlus()
        self.initUI()

    def initUI(self):
        self.setMinimumSize(1024, 640)
        self.setWindowTitle("QWebview-plus for Kiwoom")
        self.setCentralWidget(self.view)

        self.view.statusbar = QStatusBar()
        self.setStatusBar(self.view.statusbar)
        self.view.statusbar.showMessage("[F4키] 개발자 도구, [F5키] 화면 Refresh")
        # self.view.devTool.setVisible(True)
        
        openfile_action = QAction('&Open File', self)
        openfile_action.setShortcut('Ctrl+O') 
        openfile_action.setStatusTip('Open files')
        openfile_action.triggered.connect(self.onOpenFile)

        openurl_action = QAction('Open &Url', self)
        openurl_action.setShortcut('Ctrl+U') 
        openurl_action.setStatusTip('Open URL')
        openurl_action.triggered.connect(self.onOpenUrl)
        # exit_action = QAction(QIcon('exit.png'), "&Exit", self)
        
        fileMenu = self.menuBar().addMenu('Menu')
        fileMenu.addAction(openfile_action)
        fileMenu.addAction(openurl_action)
        
       
        
        # view split
        # self.splitter = QSplitter(self)
        # self.splitter.setOrientation(Qt.Horizontal)
        # layout = QVBoxLayout(self)
        # layout.setContentsMargins(0,0,0,0)
        # layout.addWidget(self.splitter)
        # self.splitter.addWidget(self.view)
        # self.splitter.addWidget(self.view.webInspector)
        # self.view.webInspector.setVisible(True)
        # self.splitter.setSizes([640,640])

    def onOpenFile(self, event):
        vOpenfilename = QFileDialog.getOpenFileName(self, 'Open File', filter="*.*")
        if vOpenfilename == "":
            return
        if os.path.isfile(vOpenfilename[0]):
            window.view.load(QUrl.fromLocalFile(vOpenfilename[0]))         

    def onOpenUrl(self, event):
        vOpenfilename = QFileDialog.getOpenFileName(self, 'Open Url', filter="*.*")
        if vOpenfilename == "":
            return
        if os.path.isfile(vOpenfilename[0]):
            window.view.load(QUrl.fromLocalFile(vOpenfilename[0]))                      

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', "QWebview를 종료하시겠습니까?",QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == "__main__":
    #parsing command line arguments
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
    # elif os.path.isfile(opt.file):
    # if opt.url:
    #     prefix = "" if bool(re.match('^(?:http|ftp)s?://', opt.url)) else "http://"
    #     window.view.load(QUrl(prefix + opt.url))
    #     window.show()
    #     sys.exit(app.exec_())
    # elif os.path.isfile(opt.file):
    #     window.view.load(QUrl.fromLocalFile(os.path.join(os.path.dirname( os.path.abspath( __file__ ) ), opt.file)))
    #     window.show()
    #     sys.exit(app.exec_())
    # else:
    #     parser.print_help()
    #     sys.exit()
