from tkinter import *
from tkinter import messagebox
import random
import json

color = "#C0C0C0"
font = "Arial"
colors="#5F9EA0"


# --------------------------------Search---------------------------------------- #
def search():
    website = web_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="Data not found!")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email:- {email}\nPassword:- {password}")
        else:
            messagebox.showinfo(title=website, message=f"No details found {website} doesn't exists")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols = ['@', '#', '$', '&', '*', '£', '¥']

password_list = [random.choice(letters) for _ in range(3)]
password_list += [random.choice(numbers) for _ in range(8)]
password_list += [random.choice(symbols) for _ in range(2)]

random.shuffle(password_list)
gen_password = ""
for char in password_list:
    gen_password += char


def generate_pass():
    pass_entry.insert(0, gen_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = web_entry.get()
    email = user_entry.get()
    password = pass_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="OOPS", message="Dont leave any box")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        else:
            with open("data.json","w") as data_file:
                data.update(new_data)
                json.dump(data,data_file,indent=4)
        finally:
            web_entry.delete(0, END)
            pass_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("password generator")
window.config(padx=30, pady=30,bg=colors)

canva = Canvas(width=200, height=200)
logo_image = PhotoImage(file="lockn1.png")
canva.create_image(100,100 ,image=logo_image)
canva.config(bg=colors,highlightthickness=0)
canva.grid(column=1, row=0)

# labels
web_label = Label(text="Website :-", font=(font, 13,"bold"),bg=colors)
web_label.grid(column=0, row=1)
user_label = Label(text="Email/username :-", font=(font, 13,"bold"),bg=colors)
user_label.grid(column=0, row=2)
pass_label = Label(text="Password :-", font=(font, 13,"bold"),bg=colors)
pass_label.grid(column=0, row=3)

# entries
web_entry = Entry(width=35)
web_entry.grid(column=1, row=1)
web_entry.focus()
user_entry = Entry(width=50)
user_entry.grid(column=1, row=2, columnspan=2)
user_entry.insert(0, "neha.dhole2004@gmail.com")
pass_entry = Entry(width=30)
pass_entry.grid(column=1, row=3)

# buttons
gen_pass_button = Button(text="Gene_pass", width=10, command=generate_pass)
gen_pass_button.grid(column=2, row=3, columnspan=2)
add_button = Button(text="Add",width=20,bg="green", command=save)
add_button.grid(column=1, row=4)

search_button = Button(text="search", width=10, command=search)
search_button.grid(column=2, row=1)

window.mainloop()
