from graphics import *
from math import *
import random
win=GraphWin("MyWin",1300,700)

def dima_mokeev_petuh(n):
# Do not use this function
# I've done it just for fun
# Now I don't want to clear it, because it's fun
# Do not use it!
    win.getMouse()
    for i in range(n):
        x1=random.random()
        x1=int(1300*x1)
        y1=random.random()
        y1=int(700*y1)
        t=Text(Point(x1,y1),'Дима Мокеев - петух')
        t.setOutline('black')
        t.draw(win)
        win.getMouse()
        
def man(x,y,high,gender):
# Drawes man, women or Dima Mokeev with coordinates x,y
# and high = high. Color of man - gray, color of woman - red
# color of Dima Mokeev - blue
    leg1=Line(Point(x-int(high/10),y-int(3/7*high)),Point(x-int(high/10),y))
    leg1.setWidth(1+int(high/20))
    leg1.draw(win)
    
    leg2=Line(Point(x+int(high/10),y-int(3/7*high)),Point(x+int(high/10),y))
    leg2.setWidth(1+int(high/20))
    leg2.draw(win)

    hand1=Line(Point(x,y-int(high/2)),Point(x+int(high*3/5),y-int(high*7/8)))
    hand1.setWidth(1+int(high/20))
    hand1.draw(win)
    
    hand2=Line(Point(x,y-int(high/2)),Point(x-int(high*3/5),y-int(high*7/8)))
    hand2.setWidth(1+int(high/20))
    hand2.draw(win)
    
    head=Circle(Point(x,y-int(6/7*high)),int(high/7))
    head.draw(win)
    if gender=='man':
        body=Polygon(Point(x,y-int(2/9*high)), Point(x-int(high/3),y-int(5/7*high)), Point(x+int(high/3),y-int(high*5/7)))
        body.setFill('gray')
        head.setFill('gray')
    elif gender=='woman':
        body=Polygon(Point(x,y-int(5/7*high)), Point(x-int(high/3),y-int(2/7*high)), Point(x+int(high/3),y-int(high*2/7)))
        body.setFill('red')
        head.setFill('red')    
    elif gender=='null':
        body=Rectangle(Point(x-int(high/3),y-int(5/7*high)), Point(x+int(high/3),y-int(high*2/7)))
        body.setFill('blue')
        head.setFill('blue')
    body.setWidth(0)
    body.draw(win)

   

    if gender=='null':
        t=Text(Point(x,y-int(high/2)),'Дима Мокеев')
        t.setOutline('white')
        t.draw(win)
        
def tree(x,y,high):
# Drawes tree with coordinates of down central part of tree x,y
# and high = high.
    c=Circle(Point(x,y-int(high/3*2)),int(high/3))
    a=Rectangle(Point(x-int(high/10),y),Point(x+int(high/10),y-int(high/2)))
    c.setWidth(2)
    a.setWidth(0)
    a.setFill('brown')
    c.setFill('green')
    a.draw(win)
    c.draw(win)
    
def sun(n,x0,y0,r):

    sun = Circle(Point(x0,y0), r)
    sun1 = Circle(Point(x0,y0), int(r/10*8))
    sun.setFill('yellow')
    sun1.setFill('orange')
    sun1.setOutline('orange')
    sun.draw(win)
    for i in range(n):
        x = x0 + int(2*r*(sin(2*i*pi/n)))
        y = y0 + int(2*r*(cos(2*i*pi/n)))
        l=Line(Point(x0, y0), Point(x,y))
        l.setWidth(10)
        l.setFill('yellow')
        l.draw(win)
    sun1.draw(win)
    
def tube(x,y,size,color):
    t1=Rectangle(Point(x+size//30, y),Point(x+2*size//7,y-size//3))
    t1.setFill(color)
    t1.setOutline(color)
    t1.draw(win)
    
    t2=Rectangle(Point(x,y-size//3),Point(x+2*size//7+size//30,y-size//3-size//20))
    t2.setFill(color)
    t2.setWidth(4)
    t2.draw(win)

    
def roof(x,y,high,color):
    size =int(high*772/510)
    
    roof_high=int(size*263/772)

    tube(x,y,size,color)
    
    roof1=Polygon(Point(x,y),Point(x + size//2, y - roof_high),Point(x+size,y))
    roof1.setFill("black")
    roof1.draw(win)

    roof2=Polygon(Point(x+ int(size*23/772),y - int(size*6/772)),Point(x+size-int(size*23/772),y - int(size*6/772)),Point(x+size//2,y - roof_high + int(size*6/772)))
    roof2.setFill("#c3c3c3")
    roof2.setOutline("#c3c3c3")
    roof2.draw(win)
    
    roof3=Polygon(Point(x+ int(2*size*23/772),y - int(2*size*6/772)),Point(x+size-int(2*size*23/772),y - int(2*size*6/772)),Point(x+size//2,y - roof_high + int(2*size*6/772)))
    roof3.setFill(color)
    roof3.setOutline(color)
    roof3.draw(win)
    
    
    line4=Line(Point(x+int(80*size/772),y-int(50*size/772)),Point(x+size-int(80*size/772),y-int(50*size/772)))
    line3=Line(Point(x+int(2*80*size/772),y-int(2*50*size/772)),Point(x+size-int(2*80*size/772),y-int(2*50*size/772)))
    line2=Line(Point(x+int(3*80*size/772),y-int(3*50*size/772)),Point(x+size-int(3*80*size/772),y-int(3*50*size/772)))
    line1=Line(Point(x+int(4*80*size/772),y-int(4*50*size/772)),Point(x+size-int(4*80*size/772),y-int(4*50*size/772)))

    line1.setWidth(5)
    line2.setWidth(5)
    line3.setWidth(5)
    line4.setWidth(5)

    line1.draw(win)
    line2.draw(win)
    line3.draw(win)
    line4.draw(win)

def windows(x,y,high,window_color,window1_color):
    size=high/510*318
    win1=Rectangle(Point(x+int(size/7*6),y-int(high*4/5)),Point(x+int(size/7*2),y-int(high/5*2)))
    win1.setWidth(5)
    win1.setFill(window_color)
    win1.draw(win)
    win2=Rectangle(Point(x-int(size/7*6),y-int(high*4/5)),Point(x-int(size/7*2),y-int(high/5*2)))
    win2.setWidth(5)
    win2.setFill(window_color)
    win2.draw(win)
    vertical_line_win1=Line(Point(x+int(size/7*4),y-int(high*4/5)),Point(x+int(size/7*4),y-int(high/5*2)))
    vertical_line_win1.setWidth(5)
    vertical_line_win1.draw(win)
    horizontal_line_win1=Line(Point(x+int(size/7*6),y-int(high*3/5)),Point(x+int(size/7*2),y-int(high/5*3)))
    horizontal_line_win1.setWidth(5)
    horizontal_line_win1.draw(win)
    vertical_line_win2=Line(Point(x-int(size/7*4),y-int(high*4/5)),Point(x-int(size/7*4),y-int(high/5*2)))
    vertical_line_win2.setWidth(5)
    vertical_line_win2.draw(win)
    horizontal_line_win2=Line(Point(x-int(size/7*6),y-int(high*3/5)),Point(x-int(size/7*2),y-int(high/5*3)))
    horizontal_line_win2.setWidth(5)
    horizontal_line_win2.draw(win)
    down_win1=Rectangle(Point(x-int(size/7*6 + size/40),y-int(high*2/5)),Point(x-int(size/7*2 - size/40),y-int(high*2/5-high/10)))
    down_win1.setWidth(5)
    down_win1.setFill(window1_color)
    down_win1.draw(win)
    down_win2=Rectangle(Point(x+int(size/7*6 + size/40),y-int(high*2/5)),Point(x+int(size/7*2 - size/40),y-int(high*2/5-high/10)))
    down_win2.setWidth(5)
    down_win2.setFill(window1_color)
    down_win2.draw(win)

def door(x,y,high,door_color,door1_color):
    size=high/510*318
    door=Rectangle(Point(x- int(size/5),y),Point(x + int(size/5),y-int(high/5*3)))
    door.setFill(door_color)
    door.setWidth(5)
    door.setOutline("#c3c3c3")
    door.draw(win)
    
    hand=Circle(Point(x + int(size/7),y - int(high/10*3)),int(size/23))
    hand.setFill(door1_color)
    hand.setOutline(door1_color)
    hand.draw(win)
    
def house(x, y, high, door_color, house_color, ruf_color, window_color, door1_color, window1_color):
    whall=Rectangle(Point(x-int(high/510*318),y),Point(x+int(high/510*318),y-high))
    whall.setFill(house_color)
    whall.setWidth(5)
    whall.draw(win)
    roof(x-int(387*high/510),y-high,high,ruf_color)
    windows(x,y,high,window_color,window1_color)
    door(x,y,high,door_color,door1_color)
    
heaven=Rectangle(Point(0,0),Point(3000,500))
heaven.setFill("blue")
heaven.draw(win)


field=Rectangle(Point(0,500),Point(3000,1000))
field.setFill("green")
field.draw(win)

sun(10,100,150,60)
for i in range(10):
    dh=random.random()
    dh=int(70*dh)
    tree(160*i,500,200+dh)

house(500, 600, 350, "#3a0201", "#126287", "#e449d3", "#d9ff73", "#465da3", "#ed1b24")
house(130, 500, 160, "#b5e51d", "#c3c3c3", "#ef1c25", "#3f48cb", "#434bb8", "#e82b31")
man(800,600,200,'man')
man(550,600,160,'woman')
win.getMouse()

win.close()
