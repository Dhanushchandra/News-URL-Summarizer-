import tkinter as tk
from tkinter import messagebox
from windows import main_window
from windows import signup_window
import requests

login_window = None  # Define login_window globally


def login():
    username = username_entry.get()
    password = password_entry.get()

    # Prepare the data to send to the server
    data = {
        "email": username,
        "password": password
    }

    # Send a POST request to the Flask server
    response = requests.post("http://localhost:5000/login", json=data)

    # Check the response status code
    if response.status_code == 200:
        messagebox.showinfo("Login Successful", "Login successful!")
        login_window.destroy()
        main_window.show_main_window()
    elif response.status_code == 401:
        messagebox.showerror("Login Failed", "Invalid email or password")
    else:
        messagebox.showerror("Login Failed", "Unknown error occurred")


def goto_signup():
    login_window.destroy()
    signup_window.show_signup_window()


def exit_full_screen(event):
    login_window.attributes("-fullscreen", False)


def run_login_window():
    global login_window  # Access the global login_window variable
    login_window = tk.Tk()
    login_window.title("Login")
    # login_window.geometry("300x150")

    login_window.attributes("-fullscreen", True)

    login_window.bind("<Escape>", exit_full_screen)

    # Username entry
    global username_entry
    username_label = tk.Label(login_window, text="Username:", font=("Helvetica", 12))
    username_label.place(relx=0.5, rely=0.4, anchor="center")
    username_entry = tk.Entry(login_window, width=30, font=("Helvetica", 10))
    username_entry.place(relx=0.5, rely=0.45, anchor="center")

    # Password entry
    global password_entry
    password_label = tk.Label(login_window, text="Password:", font=("Helvetica", 12))
    password_label.place(relx=0.5, rely=0.5, anchor="center")
    password_entry = tk.Entry(login_window, width=30, show="*", font=("Helvetica", 10))
    password_entry.place(relx=0.5, rely=0.55, anchor="center")

    # Login button
    login_button = tk.Button(login_window, text="Login", command=login, bg="lightblue", font=("Helvetica", 12, "bold"))
    login_button.place(relx=0.5, rely=0.6, anchor="center")

    # Sign up button
    signup_button = tk.Button(login_window, text="Don't have an account? Sign up", command=goto_signup)
    signup_button.place(relx=0.5, rely=0.65, anchor="center")

    # Run the login window's main loop
    login_window.mainloop()

# Run the login window
# run_login_window()
