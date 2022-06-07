from cgitb import text
from tkinter import *
import random

score=0
timeleft=30

colors=["White","Black","Green","Blue","Brown","Pink","Purple","Gray"]

def startgame(event):
    if timeleft==30:
        countdown()
    nextcolor()

def nextcolor():
    global score
    global timeleft
    if timeleft>0:
        e.focus_set()
        if e.get().lower()==colors[1].lower():
            score += 1
        e.delete(0,END)
        random.shuffle(colors)
        lbl.config(fg=str(colors[1]),text=str(colors[0]))
        scorelbl.config(text="score: "+str(score))

def countdown():
    global timeleft
    if timeleft>0:
        timeleft-=1
        timelabel.config(text="time left: "+str(timeleft))
        timelabel.after(1000,countdown)

root=Tk()
root.title("Color game")
root.geometry("375x200")
root.resizable(False,False)


scorelbl=Label(root,text="press enter to start",font=("Tahoma",10))
scorelbl.pack()

timelabel=Label(root,text="time left: "+str(timeleft),font=("Tahoma",8))
timelabel.pack()

lbl=Label(root,font=("Tahoma",10))
lbl.pack()

e=Entry(root)
root.bind("<Return>",startgame)
e.focus_set()
e.pack()
root.mainloop()
