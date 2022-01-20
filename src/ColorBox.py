# -*- coding: utf-8 -*-
"""
Created on Sun May  2 14:58:26 2021

@author: @IamRezaMousavi

برنامه جعبه رنگ - نوشته سیدرضا موسوی
در انجام هر تغییری آزاد هستید تا وقتی که این نوشته ها را تکرار کنید

"""

from datetime import datetime
from notifypy import Notify
import pygame
import math
import sys

def setText(window, text, loc, color=(255, 0, 0),
              font="Comic Sans MS", size=50):
    textFont = pygame.font.SysFont(font, size)
    textRender = textFont.render(text, True, color)
    textLoc = textRender.get_rect()
    textLoc.center = loc
    window.blit(textRender, textLoc)


def location(number, where="First", size=10, center=(400, 300), 
             radius=270, angle=(math.pi/30)):
    x = center[0] + radius*math.sin(number * angle)
    y = (center[1] - radius) + radius*(1 - math.cos(number * angle))
    if where.lower() == "end":
        x = x - size*math.sin(number * angle)
        y = y + size*math.cos(number * angle)
    return (x, y)


def setClockLines(window, mode, color, width, radius=270):
    if mode.lower() == "secounds":
        for number in range(60):
            if number % 5 == 0:
                continue
            firstLoc = location(number, radius=radius)
            endLoc = location(number, where="end", radius=radius, size=2)
            pygame.draw.line(window, color, firstLoc, endLoc, width)
    if mode.lower() == "numbers":
        for number in range(60):
            if number % 5 == 0:
                firstLoc = location(number, radius=radius)
                endLoc = location(number, where="end", radius=radius, size=7)
                pygame.draw.line(window, color, firstLoc, endLoc, width)


colorIndex = 0

def changeColor(step=1):
    colors = [
        [(0, 0, 0), (255, 255, 255)],
        [(252, 246, 245), (153, 0, 17)],
        [(153, 0, 17), (252, 246, 245)],
        [(230, 154, 141), (95, 75, 139)],
        [(95, 75, 139), (230, 154, 141)],
        [(173, 239, 209), (0, 32, 63)],
        [(0, 32, 63), (173, 239, 209)],
        [(214, 237, 23), (96, 96, 96)],
        [(96, 96, 96), (214, 237, 23)],
        [(151, 188, 98), (44, 95, 45)],
        [(44, 95, 45), (151, 188, 98)],
        [(238, 164, 127), (0, 83, 156)],
        [(0, 83, 156), (238, 164, 127)],
        [(156, 195, 213), (0, 99, 178)],
        [(0, 99, 178), (156, 195, 213)],
        [(254, 231, 21), (16, 24, 32)],
        [(16, 24, 32), (254, 231, 21)],
        [(242, 170, 76), (16, 24, 32)],
        [(16, 24, 32), (242, 170, 76)],
        [(162, 162, 161), (25, 81, 144)],
        [(25, 81, 144), (162, 162, 161)],
        [(199, 211, 212), (96, 63, 131)],
        [(96, 63, 131), (199, 211, 212)],
        [(252, 246, 245), (43, 174, 102)],
        [(43, 174, 102), (252, 246, 245)],
        [(110, 110, 109), (250, 208, 201)],
        [(250, 208, 201), (110, 110, 109)],
        [(233, 75, 60), (45, 41, 38)],
        [(45, 41, 38), (233, 75, 60)],
        [(97, 98, 71), (218, 160, 61)],
        [(218, 160, 61), (97, 98, 71)],
        [(118, 82, 139), (203, 206, 145)],
        [(203, 206, 145), (118, 82, 139)],
        [(51, 61, 121), (250, 235, 239)],
        [(250, 235, 239), (51, 61, 121)],
        [(253, 210, 14), (249, 56, 34)],
        [(249, 56, 34), (253, 210, 14)],
        [(117, 81, 57), (242, 237, 215)],
        [(242, 237, 215), (117, 81, 57)],
        [(16, 24, 32), (0, 107, 56)],
        [(0, 107, 56), (16, 24, 32)],
        [(255, 255, 255), (249, 87, 0)],
        [(249, 87, 0), (255, 255, 255)],
        [(0, 83, 156), (255, 214, 98)],
        [(255, 214, 98), (0, 83, 156)],
        [(52, 49, 72), (215, 196, 158)],
        [(215, 196, 158), (52, 49, 72)],
        [(60, 16, 83), (223, 101, 137)],
        [(223, 101, 137), (60, 16, 83)],
        [(44, 95, 45), (255, 231, 122)],
        [(255, 231, 122), (44, 95, 45)],
        [(158, 16, 48), (221, 65, 50)],
        [(221, 65, 50), (158, 16, 48)],
        [(66, 32, 87), (252, 249, 81)],
        [(252, 249, 81), (66, 32, 87)],
        [(206, 74, 126), (28, 28, 27)],
        [(28, 28, 27), (206, 74, 126)],
        [(253, 219, 39), (0, 177, 210)],
        [(0, 177, 210), (253, 219, 39)],
        [(161, 57, 65), (189, 127, 55)],
        [(189, 127, 55), (161, 57, 65)],
        [(255, 6, 0), (0, 35, 156)],
        [(0, 35, 156), (255, 6, 0)],
        [(255, 255, 255), (0, 0, 0)]
        ]
    
    global colorIndex
    next = colorIndex + step
    if next == len(colors):
        colorIndex = 0
    elif next == -len(colors) - 1:
        colorIndex = -1
    else:
        colorIndex = next
    return colors[colorIndex]


def checkAlarm(hour, minute):
    time = datetime.now()
    if hour == time.hour and minute == time.minute:
        return True
    return False

def sendNotif(check, text, alarmkey):
    notification = Notify()
    notification.message = text
    notification.title = "Alarm"
    notification.application_name = "Color Box"
    notification.icon = "./files/logo.png"
    # notification.audio = "Timer.wav"
    if check and alarmkey:
        notification.send()
        return True
    return False


# Size
width = 800
hight = 600
radius = 270

# Alarm
alarmkey = False
alarmRadius = radius / 3
alarmminute = 0
alarmhour = 0

# Show     
showalarm = False

showclocktext = True
timetextsize = 20

showdatetext = True
showweektext = True

# Windows
pygame.init()
window = pygame.display.set_mode((width, hight))
pygame.display.set_caption("Color Box")
iconFile = pygame.image.load("./files/logo.png")
pygame.display.set_icon(iconFile)

# Fonts
font1 = "Freestyle Script"
font2 = "Comic Sans MS"
font3 = "Gigi"
font4 = "Algerian"
font5 = "MV Boli"
font6 = "Segoe Print"
font7 = "Arial Rounded MT Bold"
font8 = "Forte"
font9 = "Freestyle Script"
font10 = "Viner Hand ITC"
font12 = "Lucida Handwriting"
font13 = "Segoe Print"

# Color
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
pink = (255, 0, 255)
cyan = (0, 255, 255)
white = (255, 255, 255)
black = (0, 0, 0)

# Change Mode
backgrundcolor = black
clockcolor = white
numbercolor = clockcolor

# Location
xCenter = width / 2
yCenter = hight / 2

xSecundLine = xCenter
ySecundLine = yCenter - radius
xMinuteLine = xCenter
yMinuteLine = yCenter - radius
xHourLine = xCenter
yHourLine = yCenter - radius

# 1/12

numLoc = []
for number in range(0, 60, 5):
    numLoc.append(location(number))

# Main
while True:
    # Backgrund
    window.fill(backgrundcolor)
    #pygame.draw.circle(win, clockcolor, (width/2, hight/2), r, 1)
    #pygame.draw.circle(win, yellow, (width/2, hight/2), (2*r)/3, 1)
    
    # Clock
    time = datetime.now()
    everySecondAngle = math.pi / 30
    secondAngle = time.second*everySecondAngle + (time.microsecond/1000000) * (2*math.pi) /60
    minuteAngle = time.minute*everySecondAngle + ((time.second*1000000 + time.microsecond) / 60000000) * (2*math.pi) / 60
    hourAngle = time.hour*5*everySecondAngle + ((time.minute*60 + time.second) / 720) * everySecondAngle
    
    # Keys
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE or event.key == pygame.K_DELETE:
                alarmhour = 0
                alarmminute = 0
                alarmkey = False
                setText(window, "It's Ok", (xCenter, yCenter),
                        color=(255, 0, 0), font=font4, size=50)
            if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                alarmkey = True
                setText(window, "It's Ready", (xCenter, yCenter),
                        color=(255, 0, 0), font=font4, size=50)
            if event.key == pygame.K_UP:
                alarmhour += 1
            if event.key == pygame.K_DOWN:
                alarmhour -= 1
            if event.key == pygame.K_RIGHT:
                alarmminute += 1
            if event.key == pygame.K_LEFT:
                alarmminute -= 1
            if event.key == pygame.K_n:
                if showdatetext:
                    showdatetext = False
                else:
                    showdatetext = True
            if event.key == pygame.K_v:
                if showweektext:
                    showweektext = False
                else:
                    showweektext = True
            if event.key == pygame.K_b:
                if showclocktext:
                    showclocktext = False
                    showdatetext = False
                    showweektext = False
                    timetextsize = 10
                else:
                    showclocktext = True
                    showdatetext = True
                    showweektext = True
                    timetextsize = 20
            if event.key == pygame.K_SPACE:
                if not showalarm:
                    showclocktext = False
                    showdatetext = False
                    showweektext = False
                    showalarm = True
                    timetextsize = 10
                    numbercolorold = numbercolor
                    numbercolor = blue
                    clockcolor = green
                else:
                    showalarm = False
                    showclocktext = True
                    showdatetext = True
                    showweektext = True
                    timetextsize = 20
                    numbercolor = numbercolorold
                    clockcolor = numbercolorold
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                backgrundcolor, clockcolor = changeColor()
                numbercolor = clockcolor
            if event.button == 3:
                backgrundcolor, clockcolor = changeColor(step=-1)
                numbercolor = clockcolor
    if showalarm:
        # Alarm
        setClockLines(window, "numbers", yellow, 4, radius=alarmRadius) # Number Lines
        setClockLines(window, "secounds", yellow, 2, radius=alarmRadius) # Secund Lines
        setText(window, "Alarm Clock", (width / 2, hight/2 - 20), color=yellow, size=15, font=font5)
        
        xMinuteAlarm = numLoc[0][0] + alarmRadius*math.sin(alarmminute * everySecondAngle)
        yMinuteAlarm = yCenter - alarmRadius*math.cos(alarmminute * everySecondAngle)
        pygame.draw.aaline(window, pink, (xCenter, yCenter), (xMinuteAlarm, yMinuteAlarm), 1)
        
        xHourAlarm = numLoc[0][0] + (2 * alarmRadius / 3)*math.sin(alarmhour * 5*everySecondAngle)
        yHourAlarm = yCenter - (2 * alarmRadius / 3)*math.cos(alarmhour * 5*everySecondAngle)
        pygame.draw.aaline(window, cyan, (xCenter, yCenter), (xHourAlarm, yHourAlarm), 1)
        
        if alarmhour > 23:
            alarmhour = 0
        if alarmminute > 59:
            alarmminute = 0
        if alarmminute < 0:
            alarmminute = 59
        if alarmhour < 0:
            alarmhour = 23
        setText(window, str(alarmhour) + ":" + str(alarmminute), (xCenter, yCenter+20),
                size=20, color=yellow, font=font4)
    
    # Me Text 
    setText(window, "Mousavi", (width / 2, hight/2 - radius/2), 
              color=numbercolor, size=10)
    # Time Text
    setText(window, time.strftime("%H:%M:%S"), (width / 2, hight/2 + radius/2),
            color=numbercolor, size=timetextsize)
    if showdatetext:
        # Date Text
        setText(window, time.strftime("%B %d"), (width/2 + radius/2, hight / 2),
                color=numbercolor, font=font9, size=30)
    if showweektext:
        # Week Text
        setText(window, time.strftime("%A"), (width/2 - radius/2, hight / 2),
                color=numbercolor, font=font9, size=30)
    if showclocktext:
        # Numbers Texts 
        setText(window, "", (numLoc[1][0] - 25, numLoc[1][1] + 25),
                color=numbercolor, font=font3, size=30)
        setText(window, "", (numLoc[2][0] - 25, numLoc[2][1] + 15),
                color=numbercolor, font=font3, size=30)
        setText(window, "3", (numLoc[3][0] - 25, numLoc[3][1]), color=numbercolor, font=font13, size=60)
        setText(window, "IV", (numLoc[4][0] - 25, numLoc[4][1] - 15),
                color=numbercolor, font=font10, size=30)
        setText(window, "V", (numLoc[5][0] - 15, numLoc[5][1] - 25),
                color=numbercolor, font=font10, size=30)
        setText(window, "VI", (numLoc[6][0], numLoc[6][1] - 25),
                color=numbercolor, font=font10, size=60)
        setText(window, "", (numLoc[7][0] + 15, numLoc[7][1] - 25), color=numbercolor)
        setText(window, "", (numLoc[8][0] + 25, numLoc[8][1] - 15),
                color=numbercolor, font=font3, size=30)
        setText(window, "NINE", (numLoc[9][0] + 25, numLoc[9][1]),
                color=numbercolor, font=font3, size=50)
        setText(window, "TEN", (numLoc[10][0] + 25, numLoc[10][1] + 15),
                color=numbercolor, font=font3, size=30)
        setText(window, "ELEVEN", (numLoc[11][0] + 25, numLoc[11][1] + 25),
                color=numbercolor, font=font3, size=30)
        setText(window, "12", (numLoc[0][0], numLoc[0][1] + 25),
                color=numbercolor, font=font3, size=60)
        
    setClockLines(window, "numbers", numbercolor, 4) # Line Number
    setClockLines(window, "secounds", numbercolor, 2) # Secund Lines
    
    # Lines
    pygame.draw.aaline(window, red, (xCenter, yCenter), (xSecundLine, ySecundLine), 4)
    pygame.draw.aaline(window, clockcolor, (xCenter, yCenter), (xMinuteLine, yMinuteLine), 4)
    pygame.draw.aaline(window, clockcolor, (xCenter, yCenter), (xHourLine, yHourLine), 4)
    
    xSecundLine = numLoc[0][0] + radius*math.sin(secondAngle)
    ySecundLine = yCenter - radius*math.cos(secondAngle)
    
    xMinuteLine = numLoc[0][0] + radius*math.sin(minuteAngle)
    yMinuteLine = yCenter - radius*math.cos(minuteAngle)
    
    xHourLine = numLoc[0][0] + (2*radius/3)*math.sin(hourAngle)
    yHourLine = yCenter - (2*radius/3)*math.cos(hourAngle)

    if alarmkey:
        alarm = sendNotif(checkAlarm(alarmhour, alarmminute), "Ding Ding", alarmkey)
        if alarm:
            setText(window, "Alarm", (xCenter, yCenter),
                    color=(255, 0, 0), font=font4, size=150)
    
    pygame.display.update()

# Edited on San May 29 22:29:00 2021
# Edited on Mon Aug  2 01:10:13 2021
# Edited on Thu Jan 20 04:07:27 2022
