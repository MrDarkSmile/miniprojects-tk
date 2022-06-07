from cProfile import run
from cgitb import text
import imp
from tkinter import *
win = Tk()

counter= -1
running=False
def counter_label(lbl):
    def count():
        if running:
            global counter

            if counter== -1:
                display="Starting..."
            else:
                display=str(counter)
            lbl["text"]=display
            lbl.after(1000,count)
            counter+=1
            print(counter)
    count()

def Start(lbl):
    global running
    running=True
    counter_label(lbl)
    start["state"]="disabled"
    stop["state"]="normal"
    reset["state"]="normal"

def Stop():
    global running
    start["state"]="normal"
    stop["state"]="disabled"
    reset["state"]="normal"
    running=False

def Reset(lbl):
    global running
    counter= -1
    if running == False:
        start["state"]="normal"
        lbl["text"]="welcome"
    else:
        lbl["text"]="starting..."


win.title("stop watch")
win.geometry("250x130")
win.resizable(False,False)

lbl = Label(win, text="welcome",fg="black",font="Tahoma 15")
lbl.pack()


start=Button(win,text="start",width=15,command=lambda:Start(lbl))
start.pack()

stop=Button(win,text="stop",width=15 ,state="disabled",command=Stop)
stop.pack()

reset=Button(win,text="reset",width=15 ,state="disabled",command=lambda:Reset(lbl))
reset.pack()

win.mainloop()
