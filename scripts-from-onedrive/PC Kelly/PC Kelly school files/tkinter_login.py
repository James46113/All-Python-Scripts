from tkinter import *
from tkinter.font import *


username = "HdKjZolFk"
password = "MAcOHzedp"
login_good = False
users = []
passes = []

def get_logins():
    global users, passes
    userpass = open("userpass.txt", "r")
    temp = userpass.read().split("\n")
    users = []
    passes = []
    for x in temp:
        tempuser, temppass = x.split(",")
        users.append(tempuser)
        passes.append(temppass)
    userpass.close()


def add_user(username: str, password: str):
    if username != "" and password != "":
        good = True
        taken = False
        
        for x in username:
            if x == ",":
                good = False
        for x in password:
            if x == ",":
                good = False

        for x in users:
            if username == x:
                good = False
                taken = True
        
        if good:
            file = open("userpass.txt", "a")
            both = "\n" + username + "," + password
            file.write(both)
            file.close()
            get_logins()
            print(users)
            print(passes)
            show_sign_up(1)
            
        if taken:
            taken_label.place(relx=0.5, y=155, anchor=CENTER)



def show_sign_up(num: int):
    if num == 0:
        login.place_forget()
        sign_up.place_forget()
        username_input.place_forget()
        password_input.place_forget()
        error_label.place_forget()

        username_input.delete(0, "end")
        password_input.delete(0, "end")

    else:
        username_input.place(relx=0.5, y=67, anchor=CENTER)
        password_input.place(relx=0.5, y=90, anchor=CENTER)
        login.place(relx=0.5, y=135, anchor=CENTER)
        sign_up.place(relx=0.5, y=155, anchor=CENTER)
        img_label.place(relx=0.5, y=30, anchor=CENTER)

        prompt1.place_forget()
        prompt2.place_forget()
        create_username.place_forget()
        create_password.place_forget()
        sign_up_button.place_forget()
        taken_label.place_forget()
        create_username.delete(0, "end")
        create_password.delete(0, "end")
        
        window.title("Login")         
        window.bind("<Return>", lambda e: get_input())



def sign():
    show_sign_up(0)
    
    window.title("Sign up")
    window.bind("<Return>", lambda e: add_user(create_username.get(), create_password.get()))
        
    prompt1.place(relx=0.2, y=70, anchor=CENTER)
    prompt2.place(relx=0.2, y=100, anchor=CENTER)
    create_username.place(relx=0.6, y=70, anchor=CENTER)
    create_password.place(relx=0.6, y=100, anchor=CENTER)
    sign_up_button.place(relx=0.5, y=130, anchor=CENTER)
    


def get_input():
    global username_text, password_text, login_good, username, password
    wrong_password = False

    username_text = username_input.get()
    password_text = password_input.get()

    for x in range(len(users)):
        if username_text == users[x]:
            username = users[x]
            password = passes[x]
            
    
    if username_text.strip() == username:
        if password_text.strip() == password:
            window.geometry("500x300+700+350")
            window.title("PC Kelly")
            username_input.destroy()
            password_input.destroy()
            login.destroy()
            img_label.destroy()
            error_label.destroy()
            sign_up.destroy()
            login_good = True
            wrong_password = False
        else:
            password_input.delete(0, "end")
            wrong_password = True
            wrong.set("Wrong password")
    else:
        password_input.delete(0, "end")
        wrong_password = True
        wrong.set("Invalid username")
    if wrong_password:
        error_label.place(relx=0.5, y=110, anchor=CENTER)

window = Tk()
window.geometry("230x170+850+400")
window.bind("<Return>", lambda e: get_input())
window.title("Login")
window.iconbitmap('icon.ico')

create_username = Entry()
create_password = Entry()
prompt1 = Label(text="Username")
prompt2 = Label(text="Password")
sign_up_button = Button(text="Sign up", command=lambda: add_user(create_username.get(), create_password.get()))
taken_label = Label(text="Username taken", fg="red")

img = PhotoImage(file='Logo.png')
img = img.subsample(2)
img_label = Label(image=img)
img_label.place(relx=0.5, y=30, anchor=CENTER)

wrong = StringVar()
error_label = Label(textvariable=wrong, fg="red")

login = Button(text="Login", command=get_input)
sign_up = Label(text="Sign up")
sign_up.bind("<Button-1>", lambda e: sign())

f = Font(sign_up, sign_up.cget("font"))
f.configure(underline=True)

sign_up.configure(font=f)

username_input = Entry()
password_input = Entry(show='*')

username_input.place(relx=0.5, y=67, anchor=CENTER)
password_input.place(relx=0.5, y=90, anchor=CENTER)
login.place(relx=0.5, y=135, anchor=CENTER)
sign_up.place(relx=0.5, y=155, anchor=CENTER)

get_logins()


if login_good:
    myText = StringVar(value = "Hello There")
    message = Label(window, textvariable=myText).pack()
    
