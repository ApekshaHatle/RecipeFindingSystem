from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector
from PIL import Image, ImageTk
from tkinter import Toplevel
import sys

username = ""
email = ""

if __name__ == "__main__":
    if len(sys.argv) >= 3:
        username = sys.argv[1]
        email = sys.argv[2]

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

        lblImage=Label(DataFrameLeft,text="Image",font=("arial",12,"bold"),padx=2,pady=6)
        lblImage.grid(row=7,column=0)
        txtImage=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.Image,width=30)
        txtImage.grid(row=7, column=1)

        lblRecipe=Label(DataFrameLeft,text="Recipe",font=("arial",12,"bold"),padx=2,pady=6)
        lblRecipe.grid(row=8,column=0)
        txtRecipe=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.Recipe,width=30)
        txtRecipe.grid(row=8, column=1)


        img = Image.open("D:\\Workspace\\Python Workspace\\RecipeFinder\\images\\user.jpg")
        img = img.resize((80,80), Image.LANCZOS)
        img = ImageTk.PhotoImage(img)
        lblImage = Label(DataFrameLeft, image=img)
        lblImage.image = img
        lblImage.grid(row=0, column=2, rowspan=2)

        lblUserNow=Label(DataFrameLeft,text=username,font=("arial",12,"bold"),padx=2,pady=6)
        lblUserNow.grid(row=0,column=3)
        
        lblEmailNow=Label(DataFrameLeft,text=email,font=("arial",12,"bold"),padx=2,pady=6)
        lblEmailNow.grid(row=1,column=3)

        lblIngrInfo=Label(DataFrameLeft,text="Input Ingredients Individually",font=("arial",12,"bold"),padx=2,pady=6)
        lblIngrInfo.grid(row=2,column=3,pady=5, columnspan=2)

        lblIngredient=Label(DataFrameLeft,text="Ingredient",font=("arial",12,"bold"),padx=2,pady=6)
        lblIngredient.grid(row=3,column=2,padx=15)
        txtIngredient=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.Ingredient,width=35) 
        txtIngredient.grid(row=3,column=3, columnspan=2)

        lblIngreID=Label(DataFrameLeft,text="Ingredient ID",font=("arial",12,"bold"),padx=2,pady=6)
        lblIngreID.grid(row=4,column=2,padx=15)
        txtIngreID=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.IngreID,width=35) 
        txtIngreID.grid(row=4,column=3, columnspan=2)

        lblIngreQuantity=Label(DataFrameLeft,text="Quantity",font=("arial",12,"bold"),padx=2,pady=6)
        lblIngreQuantity.grid(row=5,column=2,padx=15)
        txtIngreQuantity=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.IngreQuantity,width=35) 
        txtIngreQuantity.grid(row=5,column=3, columnspan=2)


        btnInsertIngredient = Button(DataFrameLeft, text="Insert", font=("arial", 12, "bold"), fg="#330000", bg="#D09683", width=15, command=self.insertIngredient)
        btnInsertIngredient.grid(row=7, column=2, padx=11)

        btnUpdateIngredient = Button(DataFrameLeft, text="Update", font=("arial", 12, "bold"), fg="#330000", bg="#D09683", width=15, command=self.updateIngredient)
        btnUpdateIngredient.grid(row=7, column=3, padx=9)

        btnDeleteIngredient = Button(DataFrameLeft, text="Delete", font=("arial", 12, "bold"), fg="#330000", bg="#D09683", width=15, command=self.deleteIngredient)
        btnDeleteIngredient.grid(row=7, column=4, padx=9)
        #=====================DataFrameRight===========================

        self.cmbSearchWithName = None
        self.cmbSearchWithIngre = None

        lblSearchWithName=Label(DataFrameRight,text="Recipe Name",font=("arial",12,"bold"),padx=2,pady=6)
        lblSearchWithName.grid(row=0,column=0)
        self.cmbSearchWithName=ttk.Combobox(DataFrameRight,font=("arial",12),textvariable=self.SearchWithName,width=30,state="NORMAL")
        self.cmbSearchWithName.grid(row=0,column=1,pady=10)

        btnSearchWName=Button(DataFrameRight,text="Search With Dish Name",font=("arial",12,"bold"),fg="#330000",bg="#D09683",width=23,command=self.search_with_dish_name)
        btnSearchWName.grid(row=2,column=1,pady=20)

        lblOR=Label(DataFrameRight,text="OR",font=("arial",15,"bold"),padx=2,pady=6)
        lblOR.grid(row=3,column=1,pady=10)
        
        lblSearchWithIngre=Label(DataFrameRight,text="Ingredients",font=("arial",12,"bold"),padx=2,pady=6)
        lblSearchWithIngre.grid(row=5,column=0)
        self.cmbSearchWithIngre=ttk.Combobox(DataFrameRight,font=("arial",12),textvariable=self.SearchWithIngredient,width=30,state="NORMAL")
        self.cmbSearchWithIngre.grid(row=5,column=1,pady=10)

        btnSearchWIngre=Button(DataFrameRight,text="Search With Ingredients",font=("arial",12,"bold"),fg="#330000",bg="#D09683",width=23,command=self.search_with_ingre_name)
        btnSearchWIngre.grid(row=6,column=1,pady=20)

        

        self.update_combobox()
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
        self.recipe_details=ttk.Treeview(DetailsFrame,column=("dishname","dishid","preptime","serves","difficulty","cuisine","tags","image","recipe","email"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
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
        self.recipe_details.heading("email",text="Email")
        
        self.recipe_details["show"]="headings"

        self.recipe_details.column("dishname",width=100)
        self.recipe_details.column("dishid",width=100)
        self.recipe_details.column("preptime",width=100)
        self.recipe_details.column("serves",width=100)
        self.recipe_details.column("difficulty",width=100)
        self.recipe_details.column("cuisine",width=100)
        self.recipe_details.column("tags",width=100)
        self.recipe_details.column("image",width=100)
        self.recipe_details.column("recipe",width=100)
        self.recipe_details.column("email",width=100)

        self.recipe_details.pack(fill=BOTH,expand=1)
        self.recipe_details.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    
    #=================Functionality Declaration==================

    def update_combobox(self):
            con = mysql.connector.connect(host="localhost", username="root", password="root", database="DishDetails")
            cur = con.cursor()
            cur.execute("SELECT DishName FROM recipe")
            recipe_options=[row[0] for row in cur.fetchall()]
            self.cmbSearchWithName['values']=recipe_options

            cur.execute("SELECT DISTINCT Ingredient FROM ingredients")
            ingre_options=[row[0] for row in cur.fetchall()]
            self.cmbSearchWithIngre['values']=ingre_options
            cur.close()
            con.close()

    def insertIngredient(self):
        if not all([
            self.Ingredient.get(), self.IngreID.get(), self.IngreQuantity.get()
        ]):
            messagebox.showerror("Error", "All Ingredient Details are Required")
        elif not self.can_edit():
            messagebox.showerror("Error", "This Recipe doesn't belong to you")
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
            self.update_combobox()

    def updateIngredient(self):
        if not all([self.IngreID.get(), self.Ingredient.get(), self.IngreQuantity.get()]):
            messagebox.showerror("Error", "All Ingredient Details are Required")
        elif not self.can_edit():
            messagebox.showerror("Error", "This Recipe doesn't belong to you")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="root",database="DishDetails")
            my_cursor=conn.cursor()
            
            my_cursor.execute("UPDATE ingredients SET Ingredient=%s, Quantity=%s WHERE IngreID=%s AND DishID=%s",(                                                                                                         
                                                                                self.Ingredient.get(),
                                                                                self.IngreID.get(),
                                                                                self.IngreQuantity.get(),
                                                                                self.DishID.get()     
                                                                                                ))
            
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success","Ingredient has been updated")
            self.update_combobox()

    def deleteIngredient(self):
        if not self.DishID.get() and self.IngreID.get():
            messagebox.showerror("Error", "Please select an ingredient to delete.")
        elif not self.can_edit():
            messagebox.showerror("Error", "This Recipe doesn't belong to you")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="root", database="DishDetails")
            my_cursor = conn.cursor()
            my_cursor.execute("DELETE FROM ingredients WHERE DishID=%s and IngreID=%s", (self.DishID.get(),self.IngreID.get()))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Ingredient has been deleted.")
            self.fetch_data()  # Refresh the displayed data after deletion
            self.update_combobox()

            
    def insert(self):
        if not all([
            self.NameOfDish.get(), self.DishID.get(), self.PrepTime.get(),
            self.Serves.get(), self.Difficulty.get(), self.Cuisine.get(),
            self.Tags.get(), self.Image.get(), self.Recipe.get()
        ]):
            messagebox.showerror("Error", "All Recipe Details are Required")
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
                                                                                            email  
                                                                                                                   ))
            
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success","Record has been inserted")
            self.update_combobox()

    def can_edit(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="root", database="DishDetails")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT Email from recipe WHERE DishID=%s",(self.DishID.get(),))
        result = my_cursor.fetchone()
        conn.close()  # Close the connection after fetching the data
        if result and result[0] == email:
            return True
        else:
            return False

    def update_recipe(self):
        if not all([
            self.NameOfDish.get(), self.DishID.get(), self.PrepTime.get(),
            self.Serves.get(), self.Difficulty.get(), self.Cuisine.get(),
            self.Tags.get(), self.Image.get(), self.Recipe.get()
        ]):
            messagebox.showerror("Error", "All Recipe Details are Required")
        elif not self.can_edit():
            messagebox.showerror("Error", "This Recipe doesn't belong to you")
        else:
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
            self.update_combobox()

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
                            "email": row[9],
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
                    txtSearchResult.insert(END, f"Added By : {dish_data['email']}\n")
                    txtSearchResult.insert(END, f"Recipe : {dish_data['recipe']}\n")

                    # Display ingredients for this dish
                    txtSearchResult.insert(END, "Ingredients   :\n")
                    for ingredient in dish_data["ingredients"]:
                        txtSearchResult.insert(END, f"- {ingredient['quantity']} {ingredient['ingredient']} ({ingredient['ingredient_id']})\n")

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
            my_cursor.execute("SELECT recipe.DishName FROM recipe INNER JOIN ingredients ON recipe.DishID = ingredients.DishID WHERE ingredients.Ingredient LIKE %s", (f"%{search_name}%",))

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
        elif not self.can_edit():
            messagebox.showerror("Error", "This Recipe doesn't belong to you")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="root", database="DishDetails")
            my_cursor = conn.cursor()
            my_cursor.execute("DELETE FROM ingredients WHERE DishID=%s", (self.DishID.get(),))
            my_cursor.execute("DELETE FROM recipe WHERE DishID=%s", (self.DishID.get(),))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Record has been deleted.")
            self.fetch_data()  # Refresh the displayed data after deletion
            self.update_combobox()

    def clear_fields(self):
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
        self.Email.set(row[9])

root=Tk()
ob=Recipe(root)
root.mainloop()