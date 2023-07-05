from tkinter import *
from tkinter.font import *


username = "HdKjZolFk"
password = "MAcOHzEdp"
login_good = False
users = []
passes = []
root = Tk()
root.withdraw()


def pop_up(event):
    menu.post(event.x_root, event.y_root)


def logout():
    global username_input, password_input
    window.geometry('{}x{}+{}+{}'.format(230, 170, window.winfo_screenwidth() // 2 - 230 // 2,
                                                   window.winfo_screenheight() // 2 - 170 // 2))
    window.title("Login")
    # window.iconbitmap('icon.ico')

    username_input.place(relx=0.5, y=67, anchor=CENTER)
    password_input.place(relx=0.5, y=90, anchor=CENTER)

    img_label.place(relx=0.5, y=30, anchor=CENTER)

    login.place(relx=0.5, y=135, anchor=CENTER)
    sign_up.place(relx=0.5, y=155, anchor=CENTER)
    
    f = Font(sign_up, sign_up.cget("font"))
    f.configure(underline=True)
    
    sign_up.configure(font=f)
    
    username_input.delete(0, "end")
    password_input.delete(0, "end")


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
    decrypt("hi")


def encrypt(key: str, to_encrypt: str) -> str:
    global passes
    arr = [chr(x) for x in range(49, 123)]
    key_arr = [k for k in key]
    count = 0
    new = ""
    for char in range(len(to_encrypt)):
        temp = ord(to_encrypt[char]) - arr.index(key_arr[count]) + 39
        new += chr(temp)
        count += 1
        if count == len(key_arr):
            count = 0
    return new


def decrypt(key: str):
    global passes
    arr = [chr(x) for x in range(49, 123)]
    key_arr = [k for k in key]
    temp_arr = []
    count = 0
    for x in range(len(passes)):
        new = ""
        for char in range(len(passes[x])):
            temp = ord(passes[x][char]) + arr.index(key_arr[count]) - 39
            new += chr(temp)
            count += 1
            if count==len(key_arr):
                count = 0
        temp_arr.append(new)
    passes = temp_arr


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
            both = "\n" + username + "," + encrypt("hi", password)
            file.write(both)
            file.close()
            get_logins()
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
    global login_good, username, password

    username_text = username_input.get()
    password_text = password_input.get()

    for x in range(len(users)):
        if username_text == users[x]:
            username = users[x]
            password = passes[x]
    
    if username_text.strip() == username:
        if password_text.strip() == password:
            window.geometry('{}x{}+{}+{}'.format(500, 300, window.winfo_screenwidth() // 2 - 500 // 2,
                                                           window.winfo_screenheight() // 2 - 300 // 2))
            window.title("PC Kelly")
            username_input.place_forget()
            password_input.place_forget()
            login.place_forget()
            img_label.place_forget()
            error_label.place_forget()
            sign_up.place_forget()
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
        
        
window = Toplevel()
window.geometry('{}x{}+{}+{}'.format(230, 170, window.winfo_screenwidth()//2-230//2, window.winfo_screenheight()//2-170//2))
window.bind("<Button-3>", pop_up)
window.bind("<Return>", lambda e: get_input())
window.title("Login")
#window.iconbitmap('icon.ico')

create_username = Entry(window)
create_password = Entry(window)
prompt1 = Label(window, text="Username")
prompt2 = Label(window, text="Password")
sign_up_button = Button(window, text="Sign up", command=lambda: add_user(create_username.get(), create_password.get()))
taken_label = Label(window, text="Username taken", fg="red")

#img = PhotoImage(file='Logo.png')
#img = img.subsample(2)
img_label = Label(window, text="Logo", font=(None, 30))#image=img)
img_label.place(relx=0.5, y=30, anchor=CENTER)

wrong = StringVar()
error_label = Label(window, textvariable=wrong, fg="red")


login = Button(window, text="Login", bg="dark green", command=get_input)
sign_up = Label(window, text="Sign up")
sign_up.bind("<Button-1>", lambda e: sign())

menu = Menu(window, tearoff=0)
menu.add_command(label="Logout", command=logout)

f = Font(sign_up, sign_up.cget("font"))
f.configure(underline=True)

sign_up.configure(font=f)

username_input = Entry(window)
password_input = Entry(window, show='*')

username_input.place(relx=0.5, y=67, anchor=CENTER)
password_input.place(relx=0.5, y=90, anchor=CENTER)
login.place(relx=0.5, y=135, anchor=CENTER)
sign_up.place(relx=0.5, y=155, anchor=CENTER)

get_logins()


if login_good:
    myText = StringVar(value = "Hello There")
    message = Label(window, textvariable=myText).pack()

window.mainloop()
