# -*- coding: utf-8 -*-
# @Author: @IamRezaMousavi
# @Date:   2022-08-10 05:39:09
# @Last Modified by:   @IamRezaMousavi
# @Last Modified time: 2022-08-10 20:27:30

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon
import sys

from clock import AnalogClock
from config import SETTING, BASEDIR

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.readVarible()
        
        self.setWindowTitle("ColorBox")
        self.setWindowIcon(QIcon(str(BASEDIR / "files/logo.png")))
        
        self.widget = AnalogClock()
        self.setCentralWidget(self.widget)
        
        self.setVarible()
    
    def readVarible(self):
        self.backgroundColor = SETTING["window"]["background"]
        self.windowSize = int(SETTING["window"]["size"])
    
    def setVarible(self):    
        self.resize(self.windowSize, self.windowSize)
        
        style = """QWidget {
            background-color: ++;
            }"""
        style = style.replace("++", SETTING['window']['background'])
        self.widget.setStyleSheet(style)
        self.setStyleSheet(style)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec())
