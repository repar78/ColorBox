# -*- coding: utf-8 -*-
# @Author: @IamRezaMousavi
# @Date:   2022-08-10 02:14:05
# @Last Modified by:   @IamRezaMousavi
# @Last Modified time: 2022-08-10 20:11:27

from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QTimer, QPoint, Qt, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QPolygon, QPainter, QBrush, QColor, QPen
from PyQt5 import QtGui
from datetime import datetime

from config import SETTING

class Clock(QWidget):
    windowStateChange = pyqtSignal(int)
    
    def __init__(self, parent=None):
        super(Clock, self).__init__(parent)
        
        self.readVaribles()
        self.editWidgets()
        self.windowStateChange.connect(self.editWidgets)
    
    def resizeEvent(self, a0: QtGui.QResizeEvent) -> None:
        self.windowStateChange.emit(1)
        return super().resizeEvent(a0)
    
    def setClockPos(self):
        EVERY_SECOND_ANGLE = 6
        # init
        self.secondAngle = EVERY_SECOND_ANGLE * 0
        self.minuteAngle = EVERY_SECOND_ANGLE * 0
        self.hourAngle = EVERY_SECOND_ANGLE * 5 * 0
    
    def readVaribles(self):
        self.secondHandColor = QColor(SETTING["analogClock"]["secondHand"]["color"])
        self.minuteHandColor = QColor(SETTING["analogClock"]["minuteHand"]["color"])
        self.hourHandColor = QColor(SETTING["analogClock"]["hourHand"]["color"])
        self.signColor = QColor(SETTING["analogClock"]["sign"]["color"])
    
        self.secondWidth = int(SETTING["analogClock"]["secondHand"]["width"])
        self.minuteWidth = int(SETTING["analogClock"]["minuteHand"]["width"])
        self.hourWidth = int(SETTING["analogClock"]["hourHand"]["width"])
        self.secondSize = float(SETTING["analogClock"]["secondHand"]["size"])
        self.minuteSize = float(SETTING["analogClock"]["minuteHand"]["size"])
        self.hourSize = float(SETTING["analogClock"]["hourHand"]["size"])
        self.signSize = float(SETTING["analogClock"]["sign"]["size"])
    
    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.translate(self.width() / 2, self.height() / 2)
        
        def drawPointer(color, rotation, pointer):
            painter.setBrush(QBrush(color))
            painter.save()
            painter.rotate(rotation)
            painter.drawConvexPolygon(pointer)
            painter.restore()
        
        self.setClockPos()
        drawPointer(self.secondHandColor, self.secondAngle, self.secondPoints)
        drawPointer(self.minuteHandColor, self.minuteAngle, self.minutePoints)
        drawPointer(self.hourHandColor, self.hourAngle, self.hourPoints)
        
        painter.setPen(QPen(self.signColor, self.signSize, Qt.SolidLine))
        length = QPoint(0, 5)
        for number in range(0, 60):
            if number % 5:
                painter.drawLine(QPoint() - self.radius, QPoint() - self.radius + length)
            else:
                painter.drawLine(QPoint() - self.radius, QPoint() - self.radius + length*4)
            painter.rotate(6)
        painter.end()
        return super().paintEvent(a0)
    
    @pyqtSlot(int)
    def editWidgets(self):
        width, height = self.width(), self.height()
        minimum = min(width, height)
        
        self.radius = QPoint(0, int(minimum/2) - 10)
        self.secondPoints = QPolygon([
            QPoint(self.secondWidth, 0),
            QPoint(0, self.secondWidth),
            QPoint(-self.secondWidth, 0),
            QPoint() - (self.radius * self.secondSize)
        ])
        self.minutePoints = QPolygon([
            QPoint(self.minuteWidth, 0),
            QPoint(0, self.minuteWidth),
            QPoint(-self.minuteWidth, 0),
            QPoint() - (self.radius * self.minuteSize)
        ])
        self.hourPoints = QPolygon([
            QPoint(self.hourWidth, 0),
            QPoint(0, self.hourWidth),
            QPoint(-self.hourWidth, 0),
            QPoint() - (self.radius * self.hourSize)
        ])

class AlarmClock(Clock):
    pass

class AnalogClock(Clock):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        timer = QTimer(self)
        timer.timeout.connect(self.update)
        timer.start(1)
    
    def setClockPos(self):
        now = datetime.now()
        
        everySecondAngle = 6
        second = now.second + now.microsecond*(10**-6)
        minute = now.minute + second/60
        hour = now.hour + minute/60
        self.secondAngle = second * everySecondAngle
        self.minuteAngle = minute * everySecondAngle
        self.hourAngle = hour * 5 * everySecondAngle
