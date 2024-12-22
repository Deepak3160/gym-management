import requests
from tkinter import *
from tkinter import messagebox, ttk
from PIL import Image, ImageTk

# Base URL of the Django REST API
BASE_URL = 'http://127.0.0.1:8000/gym/'

# Function to register a user via the API
def register_user(username, password):
    data = {'username': username, 'password': password}
    response = requests.post(BASE_URL + 'users/', data=data)
    if response.status_code == 201:
        messagebox.showinfo("Success", "User registered successfully!")
    else:
        messagebox.showerror("Error", f"Error: {response.json()}")

# Function to validate login via the API
def validate_login(username, password):
    response = requests.get(BASE_URL + 'users/')
    users = response.json()
    for user in users:
        if user['username'] == username and user['password'] == password:
            return True
    return False

# Function to register a trainer via the API
def register_trainer():
    data = {
        'trainer_id': e1.get(),
        'trainer_name': e2.get(),
        'email': e3.get(),
        'phone_number': e4.get(),
        'trainer_address': e5.get(),
        'trainer_type': e6.get()
    }
    response = requests.post(BASE_URL + 'trainers/', data=data)
    if response.status_code == 201:
        messagebox.showinfo("Success", "Trainer registered successfully!")
    else:
        messagebox.showerror("Error", f"Error: {response.json()}")

# Function to register a client via the API
def client_registration():
    data = {
        'client_id': et1.get(),
        'name': et2.get(),
        'age': et3.get(),
        'gender': et4.get(),
        'email': et5.get(),
        'phone_number': et6.get(),
        'address': et7.get(),
        'weight': et8.get(),
        'height': et9.get(),
        'type': et10.get()
    }
    response = requests.post(BASE_URL + 'clients/', data=data)
    if response.status_code == 201:
        messagebox.showinfo("Success", "Client registered successfully!")
    else:
        messagebox.showerror("Error", f"Error: {response.json()}")

# Other Tkinter code remains the same

# Main Program
def login():
    username = e1.get()
    password = e2.get()
    if validate_login(username, password):
        port()
    else:
        messagebox.showerror("Error", "Invalid username or password")

def registration():
    reg = Toplevel()
    reg.title("Register")
    reg.geometry("400x300")

    Label(reg, text="Username:").pack(pady=10)
    reg_username = Entry(reg)
    reg_username.pack(pady=10)

    Label(reg, text="Password:").pack(pady=10)
    reg_password = Entry(reg, show="*")
    reg_password.pack(pady=10)

    def register():
        username = reg_username.get()
        password = reg_password.get()
        register_user(username, password)

    Button(reg, text="     Register     ", command=register).pack(pady=20)
    Button(reg, text="     Close        ", command=reg.destroy).pack(pady=10)

main = Tk()
main.title("Ronic Fitness Login")
main.geometry("1530x900")

Label(main, text="User Id").pack(pady=10)
e1 = Entry(main)
e1.pack(pady=10)
Label(main, text="Password").pack(pady=10)
e2 = Entry(main, show="*")
e2.pack(pady=10)

Button(main, text="     Login      ", command=login).pack(pady=20)
Button(main, text="     Register   ", command=registration).pack(pady=10)
Button(main, text="     Exit       ", command=main.destroy).pack(pady=10)
main.mainloop()
