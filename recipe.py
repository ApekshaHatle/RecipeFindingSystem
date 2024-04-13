from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector
from PIL import Image, ImageTk


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
        self.Image=StringVar()
        self.SearchWithName=StringVar()
        
        lbltitle=Label(self.root,bd=20,relief=RIDGE,text="RECIPE FINDING SYSTEM",fg="#D09683",bg="#330000",font=("times new roman",50,"bold"))
        lbltitle.pack(side=TOP,fill=X)

        #========================DataFrame===========================
        DataFrame=Frame(self.root,bd=20,relief=RIDGE)
        DataFrame.place(x=0,y=130,width=1500,height=470)

        DataFrameLeft=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=10,font=("arial",12,"bold"),text="Dish Details")
        DataFrameLeft.place(x=0,y=5,width=460,height=380)

        DataFrameMiddle=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=10,font=("arial",12,"bold"),text="Display")
        DataFrameMiddle.place(x=470,y=5,width=510,height=380)

        DataFrameRight=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=10,font=("arial",12,"bold"),text="Search Recipe")
        DataFrameRight.place(x=990,y=5,width=460,height=380)

        #========================ButtonsFrame==========================

        ButtonFrame=Frame(self.root,bd=20,relief=RIDGE)
        ButtonFrame.place(x=0,y=540,width=1500,height=70)

        #========================DetailsFrame==========================

        DetailsFrame=Frame(self.root,bd=20,relief=RIDGE)
        DetailsFrame.place(x=0,y=610,width=1500,height=190)
    
        #=====================DataFrameLeft===========================

        lblDishName=Label(DataFrameLeft,text="Dish Name",font=("arial",12,"bold"),padx=2,pady=6)
        lblDishName.grid(row=0,column=0)
        txtName=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.NameOfDish,width=30)
        txtName.grid(row=0,column=1)

        lblDishID=Label(DataFrameLeft,text="Dish ID",font=("arial",12,"bold"),padx=2,pady=6)
        lblDishID.grid(row=1,column=0)
        txtID=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.DishID,width=30)
        txtID.grid(row=1,column=1)

        lblPrepTime=Label(DataFrameLeft,text="Preparation Time",font=("arial",12,"bold"),padx=2,pady=6)
        lblPrepTime.grid(row=2,column=0)
        txtPrepTime=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.PrepTime,width=30)
        txtPrepTime.grid(row=2,column=1)

        lblServings=Label(DataFrameLeft,text="Serves",font=("arial",12,"bold"),padx=2,pady=6)
        lblServings.grid(row=3,column=0)
        txtServings=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.Serves,width=30)
        txtServings.grid(row=3,column=1)

        lblDiff=Label(DataFrameLeft,text="Difficulty",font=("arial",12,"bold"),padx=2,pady=6)
        lblDiff.grid(row=4,column=0)
        txtDiff=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.Difficulty,width=30)
        txtDiff.grid(row=4,column=1)

        lblCuisine=Label(DataFrameLeft,text="Cuisine",font=("arial",12,"bold"),padx=2,pady=6)
        lblCuisine.grid(row=5,column=0)
        txtCuisine=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.Cuisine,width=30)
        txtCuisine.grid(row=5,column=1)

        lblTags=Label(DataFrameLeft,text="Tags",font=("arial",12,"bold"),padx=2,pady=6)
        lblTags.grid(row=6,column=0)
        txtTags=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.Tags,width=30)
        txtTags.grid(row=6,column=1)

        lblAddedBy=Label(DataFrameLeft,text="Added By",font=("arial",12,"bold"),padx=2,pady=6)
        lblAddedBy.grid(row=7,column=0)
        txtAddedBy=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.AddedBy,width=30)
        txtAddedBy.grid(row=7,column=1)

        lblIngredients=Label(DataFrameLeft,text="Ingredients",font=("arial",12,"bold"),padx=2,pady=6)
        lblIngredients.grid(row=8,column=0)
        txtIngredients=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.Ingredients,width=30) 
        txtIngredients.grid(row=8,column=1)

        lblImage=Label(DataFrameLeft,text="Image",font=("arial",12,"bold"),padx=2,pady=6)
        lblImage.grid(row=9,column=0)
        txtImage=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.Image,width=30)
        txtImage.grid(row=9, column=1)

        #=====================DataFrameMiddle==========================
        
        self.txtDisplay=Text(DataFrameMiddle,font=("arial",12,"bold"),width=51,height=7,padx=2,pady=6)
        self.txtDisplay.grid(row=0,column=0)

        self.img_label = Label(DataFrameMiddle)
        self.img_label.grid(row=1, column=0)

        #=====================DataFrameRight===========================

        lblSearchWithName=Label(DataFrameRight,text="Recipe Name",font=("arial",12,"bold"),padx=2,pady=6)
        lblSearchWithName.grid(row=0,column=0)
        txtSearchWithName=Entry(DataFrameRight,font=("arial",12),textvariable=self.SearchWithName,width=35)
        txtSearchWithName.grid(row=0,column=1,pady=10)

        btnSearchWName=Button(DataFrameRight,text="Search With Dish Name",font=("arial",12,"bold"),fg="#330000",bg="#D09683",width=23,command=self.search_with_dish_name)
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
        btnInsert=Button(ButtonFrame,text="Insert",font=("arial",12,"bold"),fg="#330000",bg="#D09683",width=28,command=self.iInsertData)
        btnInsert.grid(row=0,column=0)

        btnUpdate=Button(ButtonFrame,text="Update",font=("arial",12,"bold"),fg="#330000",bg="#D09683",width=28,command=self.update)
        btnUpdate.grid(row=0,column=1)

        btnDelete=Button(ButtonFrame,text="Delete",font=("arial",12,"bold"),fg="#330000",bg="#D09683",width=28,command=self.delete_data)
        btnDelete.grid(row=0,column=2)

        btnClear=Button(ButtonFrame,text="Clear",font=("arial",12,"bold"),fg="#330000",bg="#D09683",width=28,command=self.clear_fields)
        btnClear.grid(row=0,column=3)

        btnExit=Button(ButtonFrame,text="Exit",font=("arial",12,"bold"),fg="#330000",bg="#D09683",width=28,command=self.exit_app)
        btnExit.grid(row=0,column=4)

        #=========================Display==============================
        #=========Scrollbar==========
        scroll_x=ttk.Scrollbar(DetailsFrame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(DetailsFrame,orient=VERTICAL)
        self.recipe_details=ttk.Treeview(DetailsFrame,column=("dishname","dishid","preptime","serves","difficulty","cuisine","tags","addedby","ingredients","image"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
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
        self.recipe_details.heading("tags",text="Tags")
        self.recipe_details.heading("addedby",text="Added By")
        self.recipe_details.heading("ingredients",text="Ingredients")
        self.recipe_details.heading("image",text="Image")

        self.recipe_details["show"]="headings"

        self.recipe_details.column("dishname",width=100)
        self.recipe_details.column("dishid",width=100)
        self.recipe_details.column("preptime",width=100)
        self.recipe_details.column("serves",width=100)
        self.recipe_details.column("difficulty",width=100)
        self.recipe_details.column("cuisine",width=100)
        self.recipe_details.column("tags",width=100)
        self.recipe_details.column("addedby",width=100)
        self.recipe_details.column("ingredients",width=100)
        self.recipe_details.column("image",width=100)

        self.recipe_details.pack(fill=BOTH,expand=1)
        self.recipe_details.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    
    #=================Functionality Declaration==================

    def iInsertData(self):
        if self.NameOfDish.get()=="" or self.DishID.get()=="":
            messagebox.showerror("Error","All Fields are Required")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="root",database="DishDetails")
            my_cursor=conn.cursor()
            my_cursor.execute("INSERT INTO dish values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                                                                                   
                                                                                            self.NameOfDish.get(),
                                                                                            self.DishID.get(),
                                                                                            self.PrepTime.get(),
                                                                                            self.Serves.get(),
                                                                                            self.Difficulty.get(),
                                                                                            self.Cuisine.get(),
                                                                                            self.Tags.get(),
                                                                                            self.AddedBy.get(),
                                                                                            self.Ingredients.get(),
                                                                                            self.Image.get()      
                                                                                                                   ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success","Record has been inserted")

    def update(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="root",database="DishDetails")
        my_cursor=conn.cursor()
        my_cursor.execute("UPDATE dish SET DishName=%s,PrepTime=%s,Serves=%s,Difficulty=%s,Cuisine=%s,Tags=%s,AddedBy=%s,Ingredients=%s,Image=%s where DishID=%s",(
                                                                                                                                                                                   
                                                                                            self.NameOfDish.get(),
                                                                                            self.PrepTime.get(),
                                                                                            self.Serves.get(),
                                                                                            self.Difficulty.get(),
                                                                                            self.Cuisine.get(),
                                                                                            self.Tags.get(),
                                                                                            self.AddedBy.get(),
                                                                                            self.Ingredients.get(),
                                                                                            self.Image.get(),
                                                                                            self.DishID.get(),      
                                                                                                                   ))
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Success", "Record has been updated")


    def search_with_dish_name(self):
        search_name = self.SearchWithName.get()
        if search_name:
            conn = mysql.connector.connect(host="localhost", username="root", password="root", database="DishDetails")
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT * FROM dish WHERE DishName LIKE %s", (f"%{search_name}%",))
            row = my_cursor.fetchone()  # Assuming you only want to display the first search result
            if row:
                self.txtDisplay.delete(1.0, END)
                self.txtDisplay.insert(END, f"Dish Name: {row[0]}\n")
                self.txtDisplay.insert(END, f"Dish ID: {row[1]}\n")
                self.txtDisplay.insert(END, f"Preparation Time: {row[2]}\n")
                self.txtDisplay.insert(END, f"Serves: {row[3]}\n")
                self.txtDisplay.insert(END, f"Difficulty: {row[4]}\n")
                self.txtDisplay.insert(END, f"Cuisine: {row[5]}\n")
                self.txtDisplay.insert(END, f"Tags: {row[6]}\n")
                self.txtDisplay.insert(END, f"Added By: {row[7]}\n")
                self.txtDisplay.insert(END, f"Ingredients: {row[8]}\n\n")
                
                # Display image if available
                if row[9]:
                    img = Image.open(row[9])  # Assuming row[9] contains the path to the image
                    img = img.resize((450 ,190), Image.LANCZOS)
                    img = ImageTk.PhotoImage(img)
                    self.img_label.configure(image=img)
                    self.img_label.image = img  # Keep reference to avoid garbage collection
            else:
                self.txtDisplay.delete(1.0, END)
                self.txtDisplay.insert(END, "No records found for the given dish name.")
                # Clear the image label
                self.img_label.configure(image='')
                self.img_label.image = None

            conn.close()
        else:
            messagebox.showwarning("Search Error", "Please enter a dish name to search.")

    def delete_data(self):
        if not self.DishID.get():
            messagebox.showerror("Error", "Please select a record to delete.")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="root", database="DishDetails")
            my_cursor = conn.cursor()
            my_cursor.execute("DELETE FROM dish WHERE DishID=%s", (self.DishID.get(),))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Record has been deleted.")
            self.fetch_data()  # Refresh the displayed data after deletion

    def clear_fields(self):
        self.NameOfDish.set("")
        self.DishID.set("")
        self.PrepTime.set("")
        self.Serves.set("")
        self.Difficulty.set("")
        self.Cuisine.set("")
        self.Tags.set("")
        self.AddedBy.set("")
        self.Ingredients.set("")
        self.Image.set("")

    def exit_app(self):
        self.root.destroy()

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="root",database="DishDetails")
        my_cursor=conn.cursor()
        my_cursor.execute("SELECT * FROM dish")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.recipe_details.delete(*self.recipe_details.get_children())
            for i in rows:
                self.recipe_details.insert("",END,values=i)
            conn.commit()
        conn.close()
        
    def get_cursor(self,event):
        cursor_row=self.recipe_details.focus()
        content=self.recipe_details.item(cursor_row)
        row=content["values"]
        self.NameOfDish.set(row[0])
        self.DishID.set(row[1])
        self.PrepTime.set(row[2])
        self.Serves.set(row[3])
        self.Difficulty.set(row[4])
        self.Cuisine.set(row[5])
        self.Tags.set(row[6])
        self.AddedBy.set(row[7])
        self.Ingredients.set(row[8])
        self.Image.set(row[9])

root=Tk()
ob=Recipe(root)
root.mainloop()




