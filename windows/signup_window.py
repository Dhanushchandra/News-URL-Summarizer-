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

def show_signup_window():
    # Create the main window
    global root
    root = tk.Tk()
    root.title("Signup")
    root.geometry("300x200")

    global username_entry, email_entry, password_entry

    # Username entry
    username_label = tk.Label(root, text="Username:")
    username_label.pack()
    username_entry = tk.Entry(root)
    username_entry.pack()

    # Email entry
    email_label = tk.Label(root, text="Email:")
    email_label.pack()
    email_entry = tk.Entry(root)
    email_entry.pack()

    # Password entry
    password_label = tk.Label(root, text="Password:")
    password_label.pack()
    password_entry = tk.Entry(root, show="*")
    password_entry.pack()

    # Signup button
    signup_button = tk.Button(root, text="Signup", command=signup)
    signup_button.pack()

    signup_button = tk.Button(root, text="Have an account? Sign in", command=root.destroy)
    signup_button.pack(pady=5)

    root.mainloop()

# Show signup window
# show_signup_window()
