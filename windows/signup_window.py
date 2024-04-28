import tkinter as tk
from tkinter import messagebox
import requests

def signup():
    username = username_entry.get().strip()  # Remove leading and trailing whitespaces
    email = email_entry.get().strip()
    password = password_entry.get().strip()

    if not username or not email or not password:
        messagebox.showerror("Error", "Please fill in all fields.")
        return

    # Prepare the data to send to the server
    data = {
        "username": username,
        "email": email,
        "password": password
    }

    # Send a POST request to the Flask server
    response = requests.post("http://localhost:5000/signup", json=data)

    # Check the response status code
    if response.status_code == 201:
        messagebox.showinfo("Signup Successful", "Signup successful!")
        root.destroy()  # Close the signup window
        from windows import login_window
        login_window.run_login_window()  # Open the login window
    elif response.status_code == 400:
        error_message = response.json().get("error", "Unknown error occurred.")
        messagebox.showerror("Signup Error", error_message)
    else:
        messagebox.showerror("Unknown Error", "Unknown error occurred.")

def changetologin():
    root.destroy()
    from windows import login_window
    login_window.run_login_window()

def exit_full_screen(event):
    root.attributes("-fullscreen", False)


def show_signup_window():
    # Create the main window
    global root
    root = tk.Tk()
    root.title("Signup")
    # root.geometry("300x200")

    root.attributes("-fullscreen", True)

    root.bind("<Escape>", exit_full_screen)


    global username_entry, email_entry, password_entry

    # Username entry
    username_label = tk.Label(root, text="Username:")
    username_label.place(relx=0.5, rely=0.3, anchor="center")
    username_entry = tk.Entry(root)
    username_entry.place(relx=0.5, rely=0.35, anchor="center")

    # Email entry
    email_label = tk.Label(root, text="Email:")
    email_label.place(relx=0.5, rely=0.4, anchor="center")
    email_entry = tk.Entry(root)
    email_entry.place(relx=0.5, rely=0.45, anchor="center")

    # Password entry
    password_label = tk.Label(root, text="Password:")
    password_label.place(relx=0.5, rely=0.5, anchor="center")
    password_entry = tk.Entry(root, show="*")
    password_entry.place(relx=0.5, rely=0.55, anchor="center")

    # Signup button
    signup_button = tk.Button(root, text="Signup", command=signup)
    signup_button.place(relx=0.5, rely=0.6, anchor="center")

    # Have an account? Sign in button
    signin_button = tk.Button(root, text="Have an account? Sign in", command=changetologin)
    signin_button.place(relx=0.5, rely=0.65, anchor="center")


    root.mainloop()

# Show signup window
# show_signup_window()
