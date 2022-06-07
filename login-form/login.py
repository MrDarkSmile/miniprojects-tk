from tkinter import *
from tkinter import messagebox as ms 
import sqlite3


with sqlite3.connect("log.db") as db:
    c=db.cursor()

c.execute("CREATE TABLE IF NOT EXISTS user (username TEXT NOT NULL,password TEXT NOT NULL)")
db.commit()
db.close()


class main:
    def __init__(self,master):
        self.master=master

        self.username=StringVar()
        self.password=StringVar()
        self.n_username=StringVar()
        self.n_password=StringVar()
       
        self.widgets()

    def login(self):
        with sqlite3.connect("log.db") as db:
            c=db.cursor()
        find_user="SELECT * FROM user WHERE username=? and password=?"
        c.execute(find_user,[(self.username.get()),(self.password.get())])
        result=c.fetchall()
        if result:
            self.logf.pack_forget()
            self.head["text"]=self.username.get()+"\nlogged in"
            self.head["pady"]=150
        else:
            ms.showerror("oop!","username not found.")
        
        
    def new_user(self):
        with sqlite3.connect("log.db") as db:
            c=db.cursor()
        find_user=("SELECT * FROM user WHERE username=?")
        c.execute(find_user,[(self.username.get())])
        if c.fetchall():
            ms.showerror("error","username was used")
        else:
            ms.showinfo("success","acount created")
            self.log()
        insert="INSERT INTO user(username,password) VALUES(?,?)"
        c.execute(insert,[(self.n_username.get()),(self.n_password.get())])
        db.commit()
    def log(self):
        self.username.set("")
        self.password.set("")
        self.crf.pack_forget()
        self.head["text"]="loggin"
        self.logf.pack()


    def cr(self):
        self.n_username.set("")
        self.n_password.set("")
        self.logf.pack_forget()
        self.head["text"]="create account"
        self.crf.pack()


    def widgets(self):
        self.head=Label(self.master,text="Login",font=("",35),pady=10)
        self.head.pack()
        self.logf=Frame(self.master,padx=10,pady=10)
        Label(self.logf,text="username: ",font=('',20),padx=5,pady=5).grid(sticky=W)
        Entry(self.logf,textvariable=self.username,bd=5,font=('',15)).grid(row=0,column=1)
        Label(self.logf,text="password: ",font=('',20),padx=5,pady=5).grid(sticky=W)
        Entry(self.logf,textvariable=self.password,bd=5,font=('',15),show="*").grid(row=1,column=1)
        Button(self.logf,text="login",bd=3,padx=5,pady=5,font=('',15),command=self.login).grid()
        Button(self.logf,text="create account",bd=3,padx=5,pady=5,font=('',15),command=self.cr).grid(row=2,column=2)
        self.logf.pack()

        self.crf=Frame(self.master,padx=10,pady=10)
        Label(self.crf,text="username: ",font=('',20),padx=5,pady=5).grid(sticky=W)
        Entry(self.crf,textvariable=self.n_username,bd=5,font=('',15)).grid(row=0,column=1)
        Label(self.crf,text="password: ",font=('',20),padx=5,pady=5).grid(sticky=W)
        Entry(self.crf,textvariable=self.n_password,bd=5,font=('',15),show="*").grid(row=1,column=1)
        Button(self.crf,text="create account",bd=3,padx=5,pady=5,font=('',15),command=self.new_user).grid()
        Button(self.crf,text="go to login",bd=3,padx=5,pady=5,font=('',15),command=self.log).grid(row=2,column=2)

root = Tk()
main(root)
root.mainloop()
 
