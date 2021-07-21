import time
from tkinter import *
animation = Tk()
canvas = Canvas(animation, width = 800, height = 600)
canvas.pack()
from tkinter import colorchooser
c = colorchooser.askcolor()
c1 = colorchooser.askcolor()
print(c)
print(c1)
canvas.create_polygon(100,30,10,70,180,50,fill = c[1],width = 20, outline = c1[1])

def ch_cl():
    c = colorchooser.askcolor()
    c1 = colorchooser.askcolor()
    print(c)
    print(c1)
    canvas.create_polygon(100,30,10,70,180,50,fill = c[1],width = 20, outline = c1[1])

for x in range(0,100):
    canvas.move(1,5,0)
    animation.update()
    time.sleep(0.02)
headlights = Button(animation,text = "choose headlights color", command = ch_cl)
headlights.pack()
