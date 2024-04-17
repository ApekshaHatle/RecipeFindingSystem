from tkinter import *
import os

def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("REGISTER")
    register_screen.geometry("400x300")
    register_screen.configure(bg="#E8F6EF")  # Light green background

    global username_entry
    global password_entry

    Label(register_screen, text="Please Enter Your Details Below", bg="#E8F6EF", fg="#333333", font=("Anton", 12)).pack()
    Label(register_screen, text="").pack()
    username_label = Label(register_screen, text="Username *", bg="#E8F6EF", fg="#333333", font=("Anton", 10))
    username_label.pack()
    username_entry = Entry(register_screen, font=("Anton", 10))
    username_entry.pack()
    password_label = Label(register_screen, text="Password *", bg="#E8F6EF", fg="#333333", font=("Anton", 10))
    password_label.pack()
    password_entry = Entry(register_screen, show='*', font=("Anton", 10))
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=15, height=2, bg="#4CAF50", fg="white", font=("Anton", 10, "bold"), command=register_user).pack()

def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("400x300")
    login_screen.configure(bg="#E8F6EF")  # Light green background

    global username_verify
    global password_verify
    global username_login_entry
    global password_login_entry

    username_verify = StringVar()
    password_verify = StringVar()

    Label(login_screen, text="Please Enter Your Details Below", bg="#E8F6EF", fg="#333333", font=("Anton", 12)).pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Username *", bg="#E8F6EF", fg="#333333", font=("Anton", 10)).pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify, font=("Anton", 10))
    username_login_entry.pack()
    Label(login_screen, text="Password *", bg="#E8F6EF", fg="#333333", font=("Anton", 10)).pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show='*', font=("Anton", 10))
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=15, height=2, bg="#4CAF50", fg="white", font=("Anton", 10, "bold"), command=login_verify).pack()

def register_user():
    username_info = username_entry.get()
    password_info = password_entry.get()

    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(register_screen, text="Registration Success", fg="green", font=("Anton", 11)).pack()

def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_success()
        else:
            password_not_recognised()
    else:
        user_not_found()

def login_success():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("200x150")
    Label(login_success_screen, text="Login Success", font=("Anton", 12)).pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()

def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Invalid Password")
    password_not_recog_screen.geometry("200x150")
    Label(password_not_recog_screen, text="Invalid Password", font=("Anton", 12)).pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()

def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("User Not Found")
    user_not_found_screen.geometry("200x150")
    Label(user_not_found_screen, text="User Not Found", font=("Anton", 12)).pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()

def delete_login_success():
    login_success_screen.destroy()
 
def delete_password_not_recognised():
    password_not_recog_screen.destroy()

def delete_user_not_found_screen():
    user_not_found_screen.destroy()

def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("400x300")
    main_screen.title("Account Login")
    Label(main_screen, text="Recipe Finding System", bg="#E8F6EF", font=("Anton", 16, "bold")).pack(pady=10)
    main_screen.configure(bg="#E8F6EF")  # Light green background


    Label(text="").pack()
    Button(text="Login", height="2", width="30", bg="#4CAF50", fg="white", font=("Anton", 10, "bold"), command=login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", bg="#4CAF50", fg="white", font=("Anton", 10, "bold"), command=register).pack()

    main_screen.mainloop()

main_account_screen()