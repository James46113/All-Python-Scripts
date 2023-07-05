from tkinter import *
from tkinter.font import *
from tkinter.messagebox import askokcancel


username = "HdKjZolFk"
password = "MAcOHzedp"
login_good = False
users = []
passes = []


def pop_up(event):
    menu.post(event.x_root, event.y_root)


def logout():
    global username_input, password_input

    window.geometry('{}x{}+{}+{}'.format(230, 180, window.winfo_screenwidth()//2-230//2, window.winfo_screenheight()//2-170//2))
    username_input.place(relx=0.5, y=67, anchor=CENTER)
    password_input.place(relx=0.5, y=90, anchor=CENTER)

    img_label.place(relx=0.5, y=30, anchor=CENTER)

    login.place(relx=0.5, y=125, anchor=CENTER)
    sign_up.place(relx=0.5, y=165, anchor=CENTER)
    background.pack()
    
    f = Font(sign_up, sign_up.cget("font"))
    f.configure(underline=True)
    
    sign_up.configure(font=f)
    on_focusout("")
    on_focusout2("")
    

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
        
        for x in username:
            if x == ",":
                good = False
                taken_var.set('Username cannot contain ","')
        for x in password:
            if x == ",":
                good = False
                taken_var.set('Password cannot contain ","')


        for x in users:
            if username == x:
                good = False
                taken_var.set("Username taken")
        
        if good:
            file = open("userpass.txt", "a")
            both = "\n" + username + "," + password
            file.write(both)
            file.close()
            get_logins()
            show_sign_up(1)
            
        else:
            taken_label.place(relx=0.5, y=150, anchor=CENTER)


def show_sign_up(num: int):
    if num == 0:
        login.place_forget()
        sign_up.place_forget()
        error_label.place_forget()

        username_input.delete(0, "end")
        password_input.delete(0, "end")
        on_focusout("")
        on_focusout2("")
        

    else:
        login.place(relx=0.5, y=125, anchor=CENTER)
        sign_up.place(relx=0.5, y=167, anchor=CENTER)
        img_label.place(relx=0.5, y=30, anchor=CENTER)


        back.place_forget()
        sign_up_button.place_forget()
        taken_label.place_forget()
        
        window.title("Login")         
        window.bind("<Return>", lambda e: get_input())
        username_input.delete(0, "end")
        password_input.delete(0, "end")
        on_focusout("")
        on_focusout2("")


def sign():
    show_sign_up(0)
    
    window.title("Sign up")
    window.bind("<Return>", lambda e: add_user(username_input.get(), password_input.get()))
        
    sign_up_button.place(relx=0.5, y=125, anchor=CENTER)
    back.place(relx=0.5, y=167, anchor=CENTER)
    

def username_in(event):
    if username_input.get() == 'Username':
       username_input.delete(0, "end")
       username_input.insert(0, '')
       username_input.config(fg='black')

       
def on_focusout(event):
    if username_input.get() == '':
        username_input.insert(0, 'Username')
        username_input.config(fg = 'grey')

       
def username_in2(event):
    if password_input.get() == 'Password':
       password_input.delete(0, "end")
       password_input.insert(0, '')
       password_input.config(fg = 'black', show='*')

       
def on_focusout2(event):
    if password_input.get() == '':
        password_input.config(show='')
        password_input.insert(0, 'Password')
        password_input.config(fg = 'grey')
        

def get_input():
    global login_good, username, password, menu

    username_text = username_input.get()
    password_text = password_input.get()

    for x in range(len(users)):
        if username_text == users[x]:
            username = users[x]
            password = passes[x]
    
    if username_text.strip() == username:
        if password_text.strip() == password:
            window.title("PC Kelly")
            window.geometry('{}x{}+{}+{}'.format(500, 300, window.winfo_screenwidth() // 2 - 500 // 2,
                                                           window.winfo_screenheight() // 2 - 300 // 2))
            window.bind("<Button-3>", pop_up)
            username_input.place_forget()
            password_input.place_forget()
            login.place_forget()
            img_label.place_forget()
            error_label.place_forget()
            sign_up.place_forget()
            background.pack_forget()
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
        error_label.place(relx=0.5, y=148, anchor=CENTER)


def on_closing():
    if askokcancel(None, "Are you sure you want to close?"):
        window.destroy()
        quit(0)


window = Tk()
window.geometry('{}x{}+{}+{}'.format(230, 180, window.winfo_screenwidth()//2-230//2, window.winfo_screenheight()//2-170//2))
window.bind("<Return>", lambda e: get_input())
window.title("Login")
window.iconbitmap('icon.ico')
window.protocol("WM_DELETE_WINDOW", on_closing)
window.resizable(False, False)


bg_img = PhotoImage(file="background.png")
bg_img = bg_img.subsample(4)
background = Label(image=bg_img)
background.pack()

menu = Menu(window, tearoff=0)
menu.add_command(label="Logout", command=logout)


taken_var = StringVar()


sign_up_button = Button(text="Sign up", bg="#07681c", width=10, command=lambda: add_user(username_input.get(), password_input.get()))
taken_label = Label(textvariable=taken_var, bg="#127403", fg="red")

img = PhotoImage(file='_Logo_.png')
img = img.subsample(2)
img_label = Label(image=img, bd=0)
img_label.place(relx=0.5, y=30, anchor=CENTER)


wrong = StringVar()
error_label = Label(textvariable=wrong, bg="#127903", fg="red")


login = Button(text="Login", width=10, bg="#07681c", command=get_input)
sign_up = Label(text="Sign up", fg="white", bg="#127903")
sign_up.bind("<Button-1>", lambda e: sign())
back = Label(text="Back", fg="white", bg="#127903")
back.bind("<Button-1>", lambda e: show_sign_up(1))

f = Font(sign_up, sign_up.cget("font"))
f.configure(underline=True)
sign_up.configure(font=f)
back.configure(font=f)

username_input = Entry()
password_input = Entry()
username_input.bind("<FocusIn>", username_in)
username_input.bind("<FocusOut>", on_focusout)
password_input.bind("<FocusIn>", username_in2)
password_input.bind("<FocusOut>", on_focusout2)
                              
username_input.place(relx=0.5, y=67, anchor=CENTER)
password_input.place(relx=0.5, y=95, anchor=CENTER)
login.place(relx=0.5, y=125, anchor=CENTER)
sign_up.place(relx=0.5, y=167, anchor=CENTER)

get_logins()
on_focusout("")
on_focusout2("")

window.mainloop()
