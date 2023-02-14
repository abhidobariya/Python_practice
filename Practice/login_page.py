import tkinter as tk
import hashlib

def hash_password(password):
    """Hashes the password using SHA-256 algorithm"""
    hash_object = hashlib.sha256(password.encode())
    return hash_object.hexdigest()

def validate(username, password):
    """Validates the entered credentials"""

    valid_username = "abhi"
    valid_password = hash_password("123")
    if username == valid_username and hash_password(password) == valid_password:
        return True
    else:
        return False

def login():
    """Logs in the user"""
    username = entry_username.get()
    password = entry_password.get()
    if validate(username, password):
        label_message.config(text="Login successful!")
    else:
        label_message.config(text="Invalid username or password.")

# Create the GUI
root = tk.Tk()
root.title("Login")

label_username = tk.Label(root, text="Username:")
label_username.grid(row=0, column=0)

entry_username = tk.Entry(root)
entry_username.grid(row=0, column=1)

label_password = tk.Label(root, text="Password:")
label_password.grid(row=1, column=0)

entry_password = tk.Entry(root, show="*")
entry_password.grid(row=1, column=1)

button_login = tk.Button(root, text="Login", command=login)
button_login.grid(row=2, column=1)

label_message = tk.Label(root, text="")
label_message.grid(row=3, column=1)

root.mainloop()
