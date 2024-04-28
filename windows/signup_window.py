import tkinter as tk
# from windows.login_window import run_login_window

def signup():
    username = username_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    print("Signup Details:")
    print("Username:", username)
    print("Email:", email)
    print("Password:", password)




def show_signup_window():
    def goto_signin():
        # pass
        root.destroy()
        from windows import login_window
        login_window.run_login_window()

    # Create the main window
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

    signup_button = tk.Button(root, text="Have an account? Sign in", command=goto_signin)
    signup_button.pack(pady=5)

    root.mainloop()

# Show signup window
# show_signup_window()
