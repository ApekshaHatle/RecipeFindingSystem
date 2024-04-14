from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector
from PIL import Image, ImageTk
from tkinter import Toplevel

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
        self.Image=StringVar()
        self.Recipe=StringVar()
        self.Ingredient=StringVar()
        self.IngreID=StringVar()
        self.IngreQuantity=StringVar()
        self.AddedBy=StringVar()
        self.Email=StringVar()
        
        self.SearchWithName=StringVar()
        self.SearchWithIngredient=StringVar()
        
        lbltitle=Label(self.root,bd=20,relief=RIDGE,text="RECIPE FINDING SYSTEM",fg="#D09683",bg="#330000",font=("times new roman",50,"bold"))
        lbltitle.pack(side=TOP,fill=X)

        #========================DataFrame===========================
        DataFrame=Frame(self.root,bd=20,relief=RIDGE)
        DataFrame.place(x=0,y=130,width=1500,height=470)

        DataFrameLeft=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=10,font=("arial",12,"bold"),text="Dish Details")
        DataFrameLeft.place(x=0,y=5,width=970,height=380)

        DataFrameRight=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=10,font=("arial",12,"bold"),text="Search Recipe")
        DataFrameRight.place(x=990,y=5,width=460,height=380)

        #========================ButtonsFrame==========================

        ButtonFrame=Frame(self.root,bd=20,relief=RIDGE)
        ButtonFrame.place(x=0,y=540,width=1500,height=70)

        #========================DetailsFrame==========================

        DetailsFrame=Frame(self.root,bd=20,relief=RIDGE)
        DetailsFrame.place(x=0,y=610,width=1500,height=190)
    
        #=====================DataFrameLeft===========================

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

        lblDishName=Label(DataFrameLeft,text="Dish Name",font=("arial",12,"bold"),padx=2,pady=6)
        lblDishName.grid(row=3,column=0)
        txtName=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.NameOfDish,width=30)
        txtName.grid(row=3,column=1)

        lblDishID=Label(DataFrameLeft,text="Dish ID",font=("arial",12,"bold"),padx=2,pady=6)
        lblDishID.grid(row=4,column=0)
        txtID=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.DishID,width=30)
        txtID.grid(row=4,column=1)

        lblPrepTime=Label(DataFrameLeft,text="Preparation Time",font=("arial",12,"bold"),padx=2,pady=6)
        lblPrepTime.grid(row=5,column=0)
        txtPrepTime=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.PrepTime,width=30)
        txtPrepTime.grid(row=5,column=1)

        lblServings=Label(DataFrameLeft,text="Serves",font=("arial",12,"bold"),padx=2,pady=6)
        lblServings.grid(row=6,column=0)
        txtServings=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.Serves,width=30)
        txtServings.grid(row=6,column=1)

        lblDiff=Label(DataFrameLeft,text="Difficulty",font=("arial",12,"bold"),padx=2,pady=6)
        lblDiff.grid(row=7,column=0)
        txtDiff=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.Difficulty,width=30)
        txtDiff.grid(row=7,column=1)

        lblCuisine=Label(DataFrameLeft,text="Cuisine",font=("arial",12,"bold"),padx=2,pady=6)
        lblCuisine.grid(row=8,column=0)
        txtCuisine=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.Cuisine,width=30)
        txtCuisine.grid(row=8,column=1)

        lblTags=Label(DataFrameLeft,text="Tags",font=("arial",12,"bold"),padx=2,pady=6)
        lblTags.grid(row=0,column=2)
        txtTags=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.Tags,width=40)
        txtTags.grid(row=0,column=3)

        lblImage=Label(DataFrameLeft,text="Image",font=("arial",12,"bold"),padx=2,pady=6)
        lblImage.grid(row=1,column=2)
        txtImage=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.Image,width=40)
        txtImage.grid(row=1, column=3)

        lblRecipe=Label(DataFrameLeft,text="Recipe",font=("arial",12,"bold"),padx=2,pady=6)
        lblRecipe.grid(row=2,column=2)
        txtRecipe=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.Recipe,width=40)
        txtRecipe.grid(row=2, column=3)

        lblIngrInfo=Label(DataFrameLeft,text="Input Ingredients Individually",font=("arial",12,"bold"),padx=2,pady=6)
        lblIngrInfo.grid(row=3,column=3,pady=5)

        lblIngredient=Label(DataFrameLeft,text="Ingredient",font=("arial",12,"bold"),padx=2,pady=6)
        lblIngredient.grid(row=4,column=2,padx=15)
        txtIngredient=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.Ingredient,width=40) 
        txtIngredient.grid(row=4,column=3)

        lblIngreID=Label(DataFrameLeft,text="Ingredient ID",font=("arial",12,"bold"),padx=2,pady=6)
        lblIngreID.grid(row=5,column=2,padx=15)
        txtIngreID=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.IngreID,width=40) 
        txtIngreID.grid(row=5,column=3)

        lblIngreQuantity=Label(DataFrameLeft,text="Quantity",font=("arial",12,"bold"),padx=2,pady=6)
        lblIngreQuantity.grid(row=6,column=2,padx=15)
        txtIngreQuantity=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.IngreQuantity,width=40) 
        txtIngreQuantity.grid(row=6,column=3)

        btnSaveIngre=Button(DataFrameLeft,text="Add Ingredient",font=("arial",12,"bold"),fg="#330000",bg="#D09683",width=15,command=self.addIngredients)
        btnSaveIngre.grid(row=7,column=3)

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
        txtSearchWithIngre=Entry(DataFrameRight,font=("arial",12),textvariable=self.SearchWithIngredient,width=35)
        txtSearchWithIngre.grid(row=5,column=1,pady=10)

        btnSearchWIngre=Button(DataFrameRight,text="Search With Ingredients",font=("arial",12,"bold"),fg="#330000",bg="#D09683",width=23,command=self.search_with_ingre_name)
        btnSearchWIngre.grid(row=6,column=1,pady=20)

        #=========================Buttons==============================
        btnInsert=Button(ButtonFrame,text="Insert",font=("arial",12,"bold"),fg="#330000",bg="#D09683",width=28,command=self.insert)
        btnInsert.grid(row=0,column=0)

        btnUpdate=Button(ButtonFrame,text="Update",font=("arial",12,"bold"),fg="#330000",bg="#D09683",width=28,command=self.update_recipe)
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
        self.recipe_details=ttk.Treeview(DetailsFrame,column=("dishname","dishid","preptime","serves","difficulty","cuisine","tags","image","recipe","addedby","email"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
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
        self.recipe_details.heading("image",text="Image")
        self.recipe_details.heading("recipe",text="Recipe")
        self.recipe_details.heading("addedby",text="Added By")
        self.recipe_details.heading("email",text="Email")
        
        self.recipe_details["show"]="headings"

        self.recipe_details.column("dishname",width=65)
        self.recipe_details.column("dishid",width=65)
        self.recipe_details.column("preptime",width=65)
        self.recipe_details.column("serves",width=65)
        self.recipe_details.column("difficulty",width=65)
        self.recipe_details.column("cuisine",width=65)
        self.recipe_details.column("tags",width=65)
        self.recipe_details.column("image",width=65)
        self.recipe_details.column("recipe",width=65)
        self.recipe_details.column("addedby",width=65)
        self.recipe_details.column("email",width=65)

        self.recipe_details.pack(fill=BOTH,expand=1)
        self.recipe_details.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    
    #=================Functionality Declaration==================


    def userExists(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="root", database="DishDetails")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT AddedBy FROM user WHERE AddedBy LIKE %s", (f"%{self.AddedBy.get()}%",))
        result = my_cursor.fetchone()
        conn.close()  # Close the connection after fetching the data
        if result and result[0] == self.AddedBy.get():
            return True
        else:
            return False


    def setUser(self):
        if self.AddedBy.get()=="":
            messagebox.showerror("Error","All User Details are Required")
        elif self.userExists():
            messagebox.showinfo("Success","User has been set")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="root",database="DishDetails")
            my_cursor=conn.cursor()
            
            my_cursor.execute("INSERT INTO user values (%s,%s)",(                                                                                                         
                                                                    self.AddedBy.get(),
                                                                    self.Email.get()
                                                                                        ))
            
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success","User has been set")


    def addIngredients(self):
        if self.Ingredient.get()=="" or self.IngreID.get()=="":
            messagebox.showerror("Error","All Ingredient Details are Required")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="root",database="DishDetails")
            my_cursor=conn.cursor()
            
            my_cursor.execute("INSERT INTO ingredients values (%s,%s,%s,%s)",(                                                                                                         
                                                                                self.Ingredient.get(),
                                                                                self.IngreID.get(),
                                                                                self.IngreQuantity.get(),
                                                                                self.DishID.get()     
                                                                                                ))
            
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success","Ingredient has been inserted")

    def insert(self):
        if self.NameOfDish.get()=="" or self.DishID.get()=="":
            messagebox.showerror("Error","All Recipe Details are Required")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="root",database="DishDetails")
            my_cursor=conn.cursor()

            my_cursor.execute("INSERT INTO recipe values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(                                                                                      
                                                                                            self.NameOfDish.get(),
                                                                                            self.DishID.get(),
                                                                                            self.PrepTime.get(),
                                                                                            self.Serves.get(),
                                                                                            self.Difficulty.get(),
                                                                                            self.Cuisine.get(),
                                                                                            self.Tags.get(),
                                                                                            self.Image.get(), 
                                                                                            self.Recipe.get(),
                                                                                            self.AddedBy.get()    
                                                                                                                   ))
            
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success","Record has been inserted")



    def update_recipe(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="root", database="DishDetails")
        my_cursor = conn.cursor()
        my_cursor.execute("UPDATE recipe SET DishName=%s, PrepTime=%s, Serves=%s, Difficulty=%s, Cuisine=%s, Tags=%s, Image=%s, Recipe=%s WHERE DishID=%s", (
                            self.NameOfDish.get(), self.PrepTime.get(), self.Serves.get(), self.Difficulty.get(), 
                            self.Cuisine.get(), self.Tags.get(), self.Image.get(), self.Recipe.get(), self.DishID.get()
                        ))
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Success", "Recipe record has been updated")

    def search_with_dish_name(self):
        search_name = self.SearchWithName.get()
        if search_name:
            conn = mysql.connector.connect(host="localhost", username="root", password="root", database="DishDetails")
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT * FROM recipe LEFT JOIN ingredients ON recipe.DishID = ingredients.DishID WHERE recipe.DishName LIKE %s", (f"%{search_name}%",))

            rows = my_cursor.fetchall()  # Fetch all rows

            if rows:
                # Create a new window to display the search results
                search_result_window = Toplevel(self.root)
                search_result_window.title("Search Results")
                search_result_window.geometry("600x500")

                screen_width = search_result_window.winfo_screenwidth()
                screen_height = search_result_window.winfo_screenheight()
                x = (screen_width - 600) // 2
                y = (screen_height - 500) // 2
                search_result_window.geometry("+{}+{}".format(x, y))

                # Create a Text widget to display the search results
                txtSearchResult = Text(search_result_window, font=("arial", 12), wrap="word", height=15, width=60)
                txtSearchResult.pack(padx=10, pady=10)

                # Create a dictionary to store dish details and ingredients
                dish_ingredients = {}

                for row in rows:  # Iterate over each row
                    dish_id = row[1]

                    if dish_id not in dish_ingredients:
                        # Initialize the dish details in the dictionary
                        dish_ingredients[dish_id] = {
                            "name": row[0],
                            "prep_time": row[2],
                            "serves": row[3],
                            "difficulty": row[4],
                            "cuisine": row[5],
                            "tags": row[6],
                            "added_by": row[9],
                            "recipe": row[8],
                            "ingredients": []  # List to store ingredients for this dish
                        }

                    # Append ingredients to the ingredients list for this dish
                    dish_ingredients[dish_id]["ingredients"].append({
                        "ingredient": row[10],
                        "ingredient_id": row[11],
                        "quantity": row[12]
                    })

                # Display dish details and ingredients
                for dish_id, dish_data in dish_ingredients.items():
                    txtSearchResult.insert(END, f"Dish Name : {dish_data['name']}\n")
                    txtSearchResult.insert(END, f"Dish ID : {dish_id}\n")
                    txtSearchResult.insert(END, f"Preparation Time : {dish_data['prep_time']}\n")
                    txtSearchResult.insert(END, f"Serves : {dish_data['serves']}\n")
                    txtSearchResult.insert(END, f"Difficulty : {dish_data['difficulty']}\n")
                    txtSearchResult.insert(END, f"Cuisine : {dish_data['cuisine']}\n")
                    txtSearchResult.insert(END, f"Tags : {dish_data['tags']}\n")
                    txtSearchResult.insert(END, f"Added By : {dish_data['added_by']}\n")
                    txtSearchResult.insert(END, f"Recipe : {dish_data['recipe']}\n")

                    # Display ingredients for this dish
                    txtSearchResult.insert(END, "Ingredients   :\n")
                    for ingredient in dish_data["ingredients"]:
                        txtSearchResult.insert(END, f"- {ingredient['quantity']} {ingredient['ingredient']}\n")

                if rows[0][7]:
                    try:
                        img = Image.open(rows[0][7])
                        img = img.resize((450, 190), Image.LANCZOS)
                        img = ImageTk.PhotoImage(img)
                        lblImage = Label(search_result_window, image=img)
                        lblImage.pack(padx=10, pady=10)
                        lblImage.image = img
                    except Exception as e:
                        print("Error loading image:", e)
                        
            else:
                messagebox.showinfo("Search Results", "No records found for the given dish name.")
            conn.close()
        else:
            messagebox.showwarning("Search Error", "Please enter a dish name to search.")

    def search_with_ingre_name(self):
        search_name = self.SearchWithIngredient.get()
        if search_name:
            conn = mysql.connector.connect(host="localhost", username="root", password="root", database="DishDetails")
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT DISTINCT recipe.DishName FROM recipe INNER JOIN ingredients ON recipe.DishID = ingredients.DishID WHERE ingredients.Ingredient LIKE %s", (f"%{search_name}%",))

            rows = my_cursor.fetchall()  # Fetch all rows

            if rows:
                # Create a new window to display the search results
                search_result_window = Toplevel(self.root)
                search_result_window.title("Search Results")

                # Create a Text widget to display the search results
                txtSearchResult = Text(search_result_window, font=("Arial", 12), wrap="word", height=15, width=60)
                txtSearchResult.pack(padx=10, pady=10)

                # Display search results
                for row in rows:
                    txtSearchResult.insert("end", f"{row[0]}\n")

            else:
                messagebox.showinfo("Search Results", "No recipes found containing the given ingredient.")
            conn.close()
        else:
            messagebox.showwarning("Search Error", "Please enter an ingredient name to search.")

    def delete_data(self):
        if not self.DishID.get():
            messagebox.showerror("Error", "Please select a record to delete.")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="root", database="DishDetails")
            my_cursor = conn.cursor()
            my_cursor.execute("DELETE FROM ingredients WHERE DishID=%s", (self.DishID.get(),))
            my_cursor.execute("DELETE FROM recipe WHERE DishID=%s", (self.DishID.get(),))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Record has been deleted.")
            self.fetch_data()  # Refresh the displayed data after deletion

    def clear_fields(self):
        self.AddedBy.set("")
        self.Email.set("")
        self.NameOfDish.set("")
        self.DishID.set("")
        self.PrepTime.set("")
        self.Serves.set("")
        self.Difficulty.set("")
        self.Cuisine.set("")
        self.Tags.set("")
        self.Image.set("")
        self.Recipe.set("")
        self.Ingredient.set("")
        self.IngreID.set("")
        self.IngreQuantity.set("")
        

    def exit_app(self):
        self.root.destroy()

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="root",database="DishDetails")
        my_cursor=conn.cursor()
        my_cursor.execute("SELECT * FROM recipe")
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
        self.Image.set(row[7])
        self.Recipe.set(row[8])
        self.AddedBy.set(row[9])

root=Tk()
ob=Recipe(root)
root.mainloop()




