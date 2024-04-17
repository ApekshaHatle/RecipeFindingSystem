from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector
from PIL import Image, ImageTk
from tkinter import Toplevel

class Reg:
    def __init__(self,root):
        self.root=root
        self.root.title("Registration")
        self.root.geometry("1510x810+0+0")
        self.AddedBy=StringVar()
        self.Email=StringVar()
        self.Password=StringVar()



        DataFrame=Frame(self.root,bd=20,relief=RIDGE)
        DataFrame.place(x=0,y=130,width=1500,height=470)
        
        lblAddedBy=Label(DataFrameLeft,text="Added By",font=("arial",12,"bold"),padx=2,pady=6)
        lblAddedBy.grid(row=0,column=0)
        txtAddedBy=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.AddedBy,width=30)
        txtAddedBy.grid(row=0,column=1)

        lblEmail=Label(DataFrameLeft,text="Email Addr",font=("arial",12,"bold"),padx=2,pady=6)
        lblEmail.grid(row=1,column=0)
        txtEmail=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.Email,width=30)
        txtEmail.grid(row=1,column=1)

        btnSetUser=Button(DataFrameLeft,text="Set User",font=("arial",12,"bold"),fg="#330000",bg="#D09683",width=15,command=self.setUser)
        btnSetUser.grid(row=2,column=1,pady=12)