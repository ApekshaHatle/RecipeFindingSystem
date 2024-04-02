from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector


class Recipe:
    def __init__(self,root):
        self.root=root
        self.root.title("Recipe Finding System")
        self.root.geometry("1510x810+0+0")

        self.NameOfDish=StringVar()
        self.DishID=StringVar()
        self.PrepTime=StringVar()
        self.Serves=StringVar()
        self.Difficulty=StringVar()
        self.Cuisine=StringVar()
        self.Tags=StringVar()
        self.AddedBy=StringVar()
        self.Ingredients=StringVar()
        self.Recipe=StringVar()
        
        lbltitle=Label(self.root,bd=20,relief=RIDGE,text="RECIPE FINDING SYSTEM",fg="#D09683",bg="#330000",font=("times new roman",50,"bold"))
        lbltitle.pack(side=TOP,fill=X)

        #========================DataFrame===========================
        DataFrame=Frame(self.root,bd=20,relief=RIDGE)
        DataFrame.place(x=0,y=130,width=1500,height=400)

        DataFrameLeft=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=10,font=("arial",12,"bold"),text="Dish Details")
        DataFrameLeft.place(x=0,y=5,width=980,height=350)

        DataFrameRight=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=10,font=("arial",12,"bold"),text="Search Recipe")
        DataFrameRight.place(x=990,y=5,width=460,height=350)

        #========================ButtonsFrame==========================

        ButtonFrame=Frame(self.root,bd=20,relief=RIDGE)
        ButtonFrame.place(x=0,y=530,width=1500,height=70)

        #========================DetailsFrame==========================

        DetailsFrame=Frame(self.root,bd=20,relief=RIDGE)
        DetailsFrame.place(x=0,y=600,width=1500,height=190)
    
        #=====================DataFrameLeft===========================

        lblDishName=Label(DataFrameLeft,text="Dish Name",font=("arial",12,"bold"),padx=2,pady=6)
        lblDishName.grid(row=0,column=0)
        txtName=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.NameOfDish,width=35)
        txtName.grid(row=0,column=1)

        lblDishID=Label(DataFrameLeft,text="Dish ID",font=("arial",12,"bold"),padx=2,pady=6)
        lblDishID.grid(row=1,column=0)
        txtID=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.DishID,width=35)
        txtID.grid(row=1,column=1)

        lblPrepTime=Label(DataFrameLeft,text="Preparation Time",font=("arial",12,"bold"),padx=2,pady=6)
        lblPrepTime.grid(row=2,column=0)
        txtPrepTime=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.PrepTime,width=35)
        txtPrepTime.grid(row=2,column=1)

        lblServings=Label(DataFrameLeft,text="Serves",font=("arial",12,"bold"),padx=2,pady=6)
        lblServings.grid(row=3,column=0)
        txtServings=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.Serves,width=35)
        txtServings.grid(row=3,column=1)

        lblDiff=Label(DataFrameLeft,text="Difficulty",font=("arial",12,"bold"),padx=2,pady=6)
        lblDiff.grid(row=4,column=0)
        txtDiff=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.Difficulty,width=35)
        txtDiff.grid(row=4,column=1)

        lblCuisine=Label(DataFrameLeft,text="Cuisine",font=("arial",12,"bold"),padx=2,pady=6)
        lblCuisine.grid(row=5,column=0)
        txtCuisine=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.Cuisine,width=35)
        txtCuisine.grid(row=5,column=1)

        lblTags=Label(DataFrameLeft,text="Tags",font=("arial",12,"bold"),padx=2,pady=6)
        lblTags.grid(row=6,column=0)
        txtTags=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.Tags,width=35)
        txtTags.grid(row=6,column=1)

        lblAddedBy=Label(DataFrameLeft,text="Added By",font=("arial",12,"bold"),padx=2,pady=6)
        lblAddedBy.grid(row=7,column=0)
        txtAddedBy=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.AddedBy,width=35)
        txtAddedBy.grid(row=7,column=1)

        lblIngredients=Label(DataFrameLeft,text=" Ingredients",font=("arial",12,"bold"),padx=2,pady=6)
        lblIngredients.grid(row=0,column=2)
        txtIngredients=Entry(DataFrameLeft,font=("arial",12,"bold"),width=40)
        txtIngredients.grid(row=0,column=3)

        lblRecipe=Label(DataFrameLeft,text="Recipe",font=("arial",12,"bold"),padx=2,pady=6)
        lblRecipe.grid(row=1,column=2)
        txtRecipe = Text(DataFrameLeft, font=("arial", 12, "bold"), height=13.5, width=40)
        txtRecipe.grid(row=1, column=3, columnspan=2, padx=5, pady=5, sticky='w',rowspan=7)

        #=====================DataFrameRight===========================

        lblSearchWithName=Label(DataFrameRight,text="Recipe Name",font=("arial",12,"bold"),padx=2,pady=6)
        lblSearchWithName.grid(row=0,column=0)
        txtSearchWithName=Entry(DataFrameRight,font=("arial",12),width=35)
        txtSearchWithName.grid(row=0,column=1,pady=10)

        btnSearchWName=Button(DataFrameRight,text="Search With Dish Name",font=("arial",12,"bold"),fg="#330000",bg="#D09683",width=23)
        btnSearchWName.grid(row=2,column=1,pady=20)

        lblOR=Label(DataFrameRight,text="OR",font=("arial",15,"bold"),padx=2,pady=6)
        lblOR.grid(row=3,column=1,pady=10)

        lblSearchWithIngre=Label(DataFrameRight,text="Ingredients",font=("arial",12,"bold"),padx=2,pady=6)
        lblSearchWithIngre.grid(row=5,column=0)
        txtSearchWithIngre=Entry(DataFrameRight,font=("arial",12),width=35)
        txtSearchWithIngre.grid(row=5,column=1,pady=10)

        btnSearchWIngre=Button(DataFrameRight,text="Search With Ingredients",font=("arial",12,"bold"),fg="#330000",bg="#D09683",width=23)
        btnSearchWIngre.grid(row=6,column=1,pady=20)

        #=========================Buttons==============================
        btnInsert=Button(ButtonFrame,text="Insert",font=("arial",12,"bold"),fg="#330000",bg="#D09683",width=23)
        btnInsert.grid(row=0,column=0)

        btnUpdate=Button(ButtonFrame,text="Update",font=("arial",12,"bold"),fg="#330000",bg="#D09683",width=23)
        btnUpdate.grid(row=0,column=1)

        btnDelete=Button(ButtonFrame,text="Delete",font=("arial",12,"bold"),fg="#330000",bg="#D09683",width=23)
        btnDelete.grid(row=0,column=2)

        btnClear=Button(ButtonFrame,text="Clear",font=("arial",12,"bold"),fg="#330000",bg="#D09683",width=23)
        btnClear.grid(row=0,column=3)

        btnExit=Button(ButtonFrame,text="Exit",font=("arial",12,"bold"),fg="#330000",bg="#D09683",width=23)
        btnExit.grid(row=0,column=4)

        #=========================Display==============================
        #=========Scrollbar==========
        scroll_x=ttk.Scrollbar(DetailsFrame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(DetailsFrame,orient=VERTICAL)
        self.recipe_details=ttk.Treeview(DetailsFrame,column=("dishname","dishid","preptime","serves","difficulty","cuisine","addedby"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x=ttk.Scrollbar(command=self.recipe_details.xview)
        scroll_y=ttk.Scrollbar(command=self.recipe_details.yview)

        self.recipe_details.heading("dishname",text="Dish Name")
        self.recipe_details.heading("dishid",text="Dish ID")
        self.recipe_details.heading("preptime",text="Preparation Time")
        self.recipe_details.heading("serves",text="Serves")
        self.recipe_details.heading("difficulty",text="Difficulty")
        self.recipe_details.heading("cuisine",text="Cuisine")
        self.recipe_details.heading("addedby",text="Added By")

        self.recipe_details["show"]="headings"

        self.recipe_details.column("dishname",width=100)
        self.recipe_details.column("dishid",width=100)
        self.recipe_details.column("preptime",width=100)
        self.recipe_details.column("serves",width=100)
        self.recipe_details.column("difficulty",width=100)
        self.recipe_details.column("cuisine",width=100)
        self.recipe_details.column("addedby",width=100)

        self.recipe_details.pack(fill=BOTH,expand=1)

        
        
root=Tk()
ob=Recipe(root)
root.mainloop()




#fg="#FBEAEB",bg="#2F3C7E"  bg="#F1D3B2"