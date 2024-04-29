import tkinter as tk
import mysql.connector
from tkinter import messagebox
import subprocess

class RegistrationForm:
    def __init__(self, root):
        self.root = root
        self.root.title("User Registration")

        # Create input fields
        self.username_label = tk.Label(root, text="Username:")
        self.username_label.grid(row=1, column=1, padx=10, pady=5, sticky="e")
        self.username_entry = tk.Entry(root)
        self.username_entry.grid(row=1, column=2, padx=10, pady=5)

        self.email_label = tk.Label(root, text="Email:")
        self.email_label.grid(row=2, column=1, padx=10, pady=5, sticky="e")
        self.email_entry = tk.Entry(root)
        self.email_entry.grid(row=2, column=2, padx=10, pady=5)

        self.password_label = tk.Label(root, text="Password:")
        self.password_label.grid(row=3, column=1, padx=10, pady=5, sticky="e")
        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.grid(row=3, column=2, padx=10, pady=5)

        # Create buttons
        self.register_button = tk.Button(root, text="Register", command=self.register)
        self.register_button.grid(row=4, column=1, columnspan=2, padx=10, pady=5, sticky="ew")

        self.login_button = tk.Button(root, text="Login", command=self.login)
        self.login_button.grid(row=5, column=1, columnspan=2, padx=10, pady=5, sticky="ew")

        # Center the window
        self.center_window()

    def center_window(self):
        # Get the screen width and height
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Calculate the x and y coordinates to center the window
        x = (screen_width - 400) // 2
        y = (screen_height - 300) // 2

        # Set the geometry of the window
        self.root.geometry(f"250x200+{x}+{y}")

    def register(self):
        # Get input from text fields
        username = self.username_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()

        # Validate input (e.g., check if fields are not empty)
        if not all([username, email, password]):
            messagebox.showerror("Error", "All fields are required")
            return

        # Store user data securely in the database
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="root", database="DishDetails")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO user (AddedBy, Email, Password) VALUES (%s, %s, %s)", (username, email, password))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Registration successful")
            subprocess.run(["python", "recipe.py", username, email])
        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"Failed to register: {e}")

    def login(self):
        # Get input from text fields
        email = self.email_entry.get()
        password = self.password_entry.get()

        # Validate input
        if not all([email, password]):
            messagebox.showerror("Error", "Email and password are required")
            return

        # Authenticate user
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="root", database="DishDetails")
            cursor = conn.cursor()
            cursor.execute("SELECT AddedBy FROM user WHERE Email = %s AND Password = %s", (email, password))
            user = cursor.fetchone()
            conn.close()
            if user:
                # Pass username and email to recipe.py
                username = user[0]
                messagebox.showinfo("Success", f"Login successful. Username: {username}")
                subprocess.run(["python", "recipe.py", username, email])
            else:
                messagebox.showerror("Error", "Invalid email or password")
        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"Failed to login: {e}")


root = tk.Tk()
app = RegistrationForm(root)
root.mainloop()
