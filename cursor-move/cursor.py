from tkinter import *

def myfunc(event):
    draw(event.x,event.y)
def draw(x,y):
    paint.coords(circle,x-20,y-20,x+20,y+20)



win=Tk()
paint=Canvas()
paint.bind("<Motion>",myfunc)
paint.pack()

circle=paint.create_oval(0,0,0,0)

win.mainloop()
