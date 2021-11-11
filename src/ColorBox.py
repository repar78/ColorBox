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

def setText(win, text, loc, color=(255, 0, 0),
              font="Comic Sans MS", size=50):
    textfont = pygame.font.SysFont(font, size)
    text_ = textfont.render(text, True, color)
    text_loc = text_.get_rect()
    text_loc.center = loc
    win.blit(text_, text_loc)


def location(num, loc="Start", size=10, center=(400, 300), 
             r=270, teta=(math.pi/30)):
    x = center[0] + r*math.sin(num*teta)
    y = (center[1]-r) + r*(1-math.cos(num*teta))
    if loc.lower() == "stop":
        x = x - size*math.sin(num*teta)
        y = y + size*math.cos(num*teta)
    return (x, y)


def setClockLines(win, mode, color, k, r=270):
    if mode.lower() == "secounds":
        for i in range(60):
            if i%5 == 0:
                continue
            pygame.draw.line(win, color, location(i, r=r), location(i, loc="stop", r=r, size=2), k)
    if mode.lower() == "numbers":
        for i in range(60):
            if i%5 == 0:
                pygame.draw.line(win, color, location(i, r=r), location(i, loc="stop", r=r, size=7), k)


def changeColor(backcolor, numcolor, step= 1):
    color = [
        [(255, 255, 255), (0, 0, 0)],
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
        ]
    for i in range(len(color)):
        if backcolor == color[i][0]:
            if numcolor == color[i][1]:
                count = i
    if count+step == len(color):
        return color[0]
    else:
        return color[count+step]


def checkAlarm(hour, minute):
    time = datetime.now()
    if hour == time.hour and minute == time.minute:
        return True
    return False

def sendNotif(check, text, alarmkey):
    notifi = Notify()
    notifi.message = text
    notifi.title = "Alarm"
    notifi.application_name = "Color Box"
    notifi.icon = "./files/logo.png"
    #notifi.audio = "Timer.wav"
    if check and alarmkey:
        notifi.send()
        return True
    return False


# Size
width = 800
hight = 600
r = 270

# Alarm
alarmkey = False
ralarm = r/3
alarmminute = 0
alarmhour = 0
x_minute_alarm = 0
y_minute_alarm = 0
x_hour_alarm = 0
y_hour_alarm = 0

# Show     
showalarm = 0
showalarmcount = 0

showclockcount = 1
showclocktext = 1
timetextsize = 20

showdatecount = 0
showdatetext = 1
showweekcount = 0
showweektext = 1

# Windows
pygame.init()
win = pygame.display.set_mode((width, hight))
pygame.display.set_caption("Color Box")
gameicon = pygame.image.load("./files/logo.png")
pygame.display.set_icon(gameicon)

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
x_center = width/2
y_center = hight/2

x_secund_line = x_center
y_secund_line = y_center - r
x_minute_line = x_center
y_minute_line = y_center - r
x_hour_line = x_center
y_hour_line = y_center - r

# 1/12
(x1, y1) = location(5)
(x2, y2) = location(10)
(x3, y3) = location(15)
(x4, y4) = location(20)
(x5, y5) = location(25)
(x6, y6) = location(30)
(x7, y7) = location(35)
(x8, y8) = location(40)
(x9, y9) = location(45)
(x10, y10) = location(50)
(x11, y11) = location(55)
(x12, y12) = location(0)

# Main
while True:
    # Backgrund
    win.fill(backgrundcolor)
    #pygame.draw.circle(win, clockcolor, (width/2, hight/2), r, 1)
    #pygame.draw.circle(win, yellow, (width/2, hight/2), (2*r)/3, 1)
    
    # Clock
    time = datetime.now()
    t_clock = math.pi/30
    tsecund = time.second*t_clock + (time.microsecond/1000000)*(2*math.pi)/60
    tminute = time.minute*t_clock + ((time.second*1000000+time.microsecond)/60000000)*(2*math.pi)/60
    thour = time.hour*5*t_clock + ((time.minute*60+time.second)/720)*t_clock
    
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
                setText(win, "It's Ok", (x_center, y_center),
                        color=(255, 0, 0), font=font4, size = 50)
            if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                alarmkey = True
                setText(win, "It's Ready", (x_center, y_center),
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
                showdatecount += 1
                if showdatecount%2 == 1:
                    showdatetext = 0
                else:
                    showdatetext = 1
            if event.key == pygame.K_v:
                showweekcount += 1
                if showweekcount%2 == 1:
                    showweektext = 0
                else:
                    showweektext = 1
            if event.key == pygame.K_b:
                showclockcount += 1
                if showclockcount%2 == 1:
                    showclocktext = 0
                    showdatetext = 0
                    showweektext = 0
                    timetextsize = 10
                else:
                    showclocktext = 1
                    showdatetext = 1
                    showweektext = 1
                    timetextsize = 20
            if event.key == pygame.K_SPACE:
                showalarmcount += 1
                if showalarmcount%2 == 1:
                    showclocktext = 0
                    showdatetext = 0
                    showweektext = 0
                    showalarm = 1
                    timetextsize = 10
                    numbercolorold = numbercolor
                    numbercolor = blue
                    clockcolor = green
                else:
                    showalarm = 0
                    showclocktext = 1
                    showdatetext = 1
                    showweektext = 1
                    timetextsize = 20
                    numbercolor = numbercolorold
                    clockcolor = numbercolorold
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                backgrundcolor, clockcolor = changeColor(backgrundcolor,
                                                        clockcolor)
                numbercolor = clockcolor
            if event.button == 3:
                backgrundcolor, clockcolor = changeColor(backgrundcolor,
                                                        clockcolor, step=-1)
                numbercolor = clockcolor
    if showalarm:
        # Alarm
        setClockLines(win, "numbers", yellow, 4, r=ralarm) # Line Number
        setClockLines(win, "secounds", yellow, 2, r=ralarm) # Secund Lines
        setText(win, "Alarm Clock", (width/2, hight/2-20),
                color=yellow, size=15, font=font5)
        
        x_minute_alarm = x12 + ralarm*math.sin(alarmminute*t_clock)
        y_minute_alarm = y_center - ralarm*math.cos(alarmminute*t_clock)
        pygame.draw.aaline(win, pink, (x_center, y_center),
                               (x_minute_alarm, y_minute_alarm), 1)
        x_hour_alarm = x12 + (2*ralarm/3)*math.sin(alarmhour*5*t_clock)
        y_hour_alarm = y_center - (2*ralarm/3)*math.cos(alarmhour*5*t_clock)
        pygame.draw.aaline(win, cyan, (x_center, y_center),
                               (x_hour_alarm, y_hour_alarm), 1)
        if alarmhour > 23:
            alarmhour = 0
        if alarmminute > 59:
            alarmminute = 0
        if alarmminute < 0:
            alarmminute = 59
        if alarmhour < 0:
            alarmhour = 23
        setText(win, str(alarmhour)+":"+str(alarmminute), (x_center,y_center+20),
                size=20, color=yellow, font=font4)
    
    # Me Text 
    setText(win, "Mousavi", (width/2, hight/2-r/2), 
              color=numbercolor, size=10)
    # اجازه تغییر این بخش را ندارید
    setText(win, "@IamRezaMousavi", (width-50, hight-6), 
              color=numbercolor, size=10)
    # Time Text
    setText(win, time.strftime("%H:%M:%S"), (width/2, hight/2+r/2),
            color=numbercolor, size=timetextsize)
    if showdatetext:
        # Date Text
        setText(win, time.strftime("%B %d"),
                (width/2+r/2, hight/2),
                color=numbercolor, font=font9, size=30)
    if showweektext:
        # Week Text
        setText(win, time.strftime("%A"),
                (width/2-r/2, hight/2),
                color=numbercolor, font=font9, size=30)
    if showclocktext:
        # Numbers Texts 
        setText(win, "", (x1-25, y1+25),
                color=numbercolor, font=font3, size=30)
        setText(win, "", (x2-25, y2+15),
                color=numbercolor, font=font3, size=30)
        setText(win, "3", (x3-25, y3), color=numbercolor, font=font13, size=60)
        setText(win, "IV", (x4-25, y4-15),
                color=numbercolor, font=font10, size=30)
        setText(win, "V", (x5-15, y5-25),
                color=numbercolor, font=font10, size=30)
        setText(win, "VI", (x6, y6-25),
                color=numbercolor, font=font10, size=60)
        setText(win, "", (x7+15, y7-25), color=numbercolor)
        setText(win, "", (x8+25, y8-15),
                color=numbercolor, font=font3, size=30)
        setText(win, "NINE", (x9+25, y9),
                color=numbercolor, font=font3, size=50)
        setText(win, "TEN", (x10+25, y10+15),
                color=numbercolor, font=font3, size=30)
        setText(win, "ELEVEN", (x11+25, y11+25),
                color=numbercolor, font=font3, size=30)
        setText(win, "12", (x12, y12+25),
                color=numbercolor, font=font3, size=60)
        
    setClockLines(win, "numbers", numbercolor, 4) # Line Number
    setClockLines(win, "secounds", numbercolor, 2) # Secund Lines
    
    # Lines
    pygame.draw.aaline(win, red, (x_center, y_center),
                           (x_secund_line, y_secund_line), 4)
    pygame.draw.aaline(win, clockcolor, (x_center, y_center),
                           (x_minute_line, y_minute_line), 4)
    pygame.draw.aaline(win, clockcolor, (x_center, y_center),
                           (x_hour_line, y_hour_line), 4)
    
    x_secund_line = x12 + r*math.sin(tsecund)
    y_secund_line = y_center - r*math.cos(tsecund)
    
    x_minute_line = x12 + r*math.sin(tminute)
    y_minute_line = y_center - r*math.cos(tminute)
    
    x_hour_line = x12 + (2*r/3)*math.sin(thour)
    y_hour_line = y_center - (2*r/3)*math.cos(thour)

    if alarmkey:
        alarm = sendNotif(checkAlarm(alarmhour, alarmminute), "Ding Ding", alarmkey)
        if alarm:
            setText(win, "Alarm", (x_center, y_center),
                    color = (255, 0, 0), font=font4, size=150)
    
    pygame.display.update()

# Edited on San May 29 22:29:00 2021
# Edited on Mon Aug  2 01:10:13 2021
