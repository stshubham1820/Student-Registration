from tkinter import *
import os
from PIL import ImageTk , Image
import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",passwd="St1820@",database="Stud")
pointer = mydb.cursor()
screen = Tk()
screen.title("My School App")
img = Image.open('undraw.png')
img = img.resize((250,250))
img = ImageTk.PhotoImage(img)
def regis():
    try:
        global name
        global age
        name = StringVar()
        age = IntVar()
        screen = Toplevel(master=None)
        screen.title("Add Students :")
        Label(master = screen,text= "Register Here : Enter Student Details ",font=("Calibri",12)).grid(row=0,sticky=N,pady=10,padx=100)
        Label(master = screen,text= "Full Name",font=("Calibri",12)).grid(row=1,sticky=W,pady=10)
        Label(master = screen,text= "Age",font=("Calibri",12)).grid(row=2,sticky=W,pady=10)
        #Register Entry
        Entry(master=screen,textvariable=name).grid(row=1,column=0)
        Entry(master=screen,textvariable=age).grid(row=2,column=0)
        Button(master=screen,text="Submit",command=insert).grid(row=7,column=0,pady=10)
    except Exception as Error :
        print("User Details hasn't been Stored : !Error With The Code")
        print(Error)
def insert():
    try:
        Name = name.get()
        Age = age.get()
        sqlformula = "INSERT INTO Students (name,age) VALUES (%s,%s)"
        stud = (Name,Age)
        pointer.execute(sqlformula,stud)
        mydb.commit()

    except Exception as Error :
        print("User Details hasn't been Stored : !Error With The Code")
        print(Error)
def dal():
    pointer.execute("DELETE FROM Students")
    screen.destroy()
    mydb.commit()
def output():
    try:
        screen = Toplevel(master=None)
        screen.title("Add Students :")
        Label(master = screen,text= "Register Here : Enter Student Details ",font=("Calibri",12)).grid(row=0,sticky=N,pady=10,padx=100)
        pointer.execute("SELECT * FROM Students")
        j = 1
        for i in pointer:
            Label(master = screen,text= "Full Name",font=("Calibri",12)).grid(row=1,column=0,sticky=W,pady=10)
            Label(master = screen,text= "Age",font=("Calibri",12)).grid(row=1,column=1,sticky=W,pady=10)
            Label(master = screen,text= i[0] ,font=("Calibri",12)).grid(row=j+1,column=0,sticky=W,pady=10)
            Label(master = screen,text= i[1] ,font=("Calibri",12)).grid(row=j+1,column=1,sticky=W,pady=10)
            j=j+1
            k=j
        Button(master=screen,text="Clear Data",command=dal).grid(row=k+1,column=0,pady=10)
        
    except Exception as Error:
        print(Error)

Label(master = None,text= "My School App",font=("Helvetica",12)).grid(row=0,sticky=N,pady=10,padx=100)
Label(master = None , text= "Student Dashboard",font=("Calibri",14)).grid(row=1,sticky=N)
Label(master = None , image=img).grid(row=2,sticky=N)

Button(master = None , text = "Enter Student",font=("Helvetica",12),command=regis).grid(row=4,sticky=N)
Button(master = None , text = "Student Data",font=("Helvetica",12),command=output).grid(row=5,sticky=N,pady=10)

