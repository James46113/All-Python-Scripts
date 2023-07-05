from tkinter import Tk, CENTER, PhotoImage, Toplevel, StringVar, NW
from tkinter.font import *
from tkinter.commondialog import Dialog
from tempfile import mkstemp
from tkinter.ttk import *


def login():
    class Message(Dialog):
        command = "tk_messageBox"
    
    def _show(title=None, message=None, _icon=None, _type=None, **options):
        if _icon and "icon" not in options:    options["icon"] = _icon
        if _type and "type" not in options:    options["type"] = _type
        if title:   options["title"] = title
        if message: options["message"] = message
        res = Message(**options).show()
        return str(res)
    
    def close_window(icon: str, buttons: str, **options):
        if icon!="error" and icon!="info" and icon!="question" and icon!="warning":
            s = _show("Close?", "Do you want to close?", "warning", "yesno", **options)
        elif buttons!="abortretryignore" and buttons!="ok" and buttons!="okcancel" and buttons!="retrycancel" and buttons!="yesno" and buttons!="yesnocancel":
            s = _show("Close?", "Do you want to close?", icon, "yesno", **options)
        else:
            s = _show("Close?", "Do you want to close?", icon, buttons, **options)
        
        if s=="yes":
            window.destroy()
            quit(0)
    
    def logout():
        window.deiconify()
    
    def get_info():
        nonlocal user_info
        f = open("userinfo.txt", "r")
        temp = f.read().split("\n")
        temp_arr = []
        for x in temp:
            user_info.append(x.split(','))
    
    def get_logins():
        nonlocal users, passes
        users = []
        passes = []
        userpass = open("userpass.txt", "r")
        temp = userpass.read().split("\n")
        for x in temp:
            tempuser, temppass = x.split(",")
            users.append(tempuser)
            passes.append(temppass)
        userpass.close()
    
    def email_check(email) -> bool:
        at = 0
        dot = 0
        
        for x in range(len(email)):
            if email[x]=="@":
                at = x
            elif email[x]=="." and at!=0:
                dot = x
        
        if dot - at >= 3 and at > 1 and len(email) - dot >= 2:
            return True
        else:
            taken_var.set("Invalid email")
            return False
    
    def add_address():
        street = street_input.get()
        city = city_input.get()
        postcode = postcode_input.get()
        email = email_input.get()
        username = username_input.get()
        if street!="" and city!="" and postcode!="" and email!="":
            f = open("userinfo.txt", 'a')
            f.write("\n{},{},{},{},{}".format(username, street, city, postcode, email))
            f.close()
            return True
        
        else:
            taken_var.set("Fill all boxes")
            taken_label.place(relx=0.5, y=165, anchor=CENTER)
            return False
    
    def add_user(username: str, password: str):
        if username!="" and password!="":
            good = True
            
            for x in username:
                if x==",":
                    good = False
                    taken_var.set('Username cannot contain ","')
            for x in password:
                if x==",":
                    good = False
                    taken_var.set('Password cannot contain ","')
            
            if username in users:
                good = False
                taken_var.set("Username taken")
            
            if good:
                if email_check(email_input.get()):
                    if add_address():
                        file = open("userpass.txt", "a")
                        both = "\n" + username + "," + password
                        file.write(both)
                        file.close()
                        get_logins()
                        show_sign_up(1)
                    else:
                        good = False
                else:
                    good = False
            
            if not good:
                taken_label.place(relx=0.5, y=265, anchor=CENTER)
    
    def show_sign_up(num: int):
        window.focus()
        if num==0:
            login.place_forget()
            sign_up.place_forget()
            error_label.place_forget()
            window.geometry('{}x{}+{}+{}'.format(230, 290, window.winfo_screenwidth() // 2 - 230 // 2,
                                                           window.winfo_screenheight() // 2 - 280 // 2))
            
            acount_info.place(x=5, y=57, anchor=NW)
            personal_info.place(x=2, y=113, anchor=NW)
            
            street_input.place(relx=0.5, y=123, anchor=CENTER)
            city_input.place(relx=0.5, y=151, anchor=CENTER)
            postcode_input.place(relx=0.5, y=179, anchor=CENTER)
            email_input.place(relx=0.5, y=207, anchor=CENTER)
            
            username_input.delete(0, "end")
            password_input.delete(0, "end")
            on_focus_out(username_input, "Username")
            on_focus_out2("")
        
        else:
            window.geometry('{}x{}+{}+{}'.format(230, 180, window.winfo_screenwidth() // 2 - 230 // 2,
                                                           window.winfo_screenheight() // 2 - 170 // 2))
            
            login.place(relx=0.5, y=125, anchor=CENTER)
            sign_up.place(relx=0.5, y=167, anchor=CENTER)
            img_label.place(relx=0.5, y=30, anchor=CENTER)
            
            acount_info.place_forget()
            personal_info.place_forget()
            
            street_input.place_forget()
            city_input.place_forget()
            postcode_input.place_forget()
            email_input.place_forget()
            
            back.place_forget()
            sign_up_button.place_forget()
            taken_label.place_forget()
            
            window.title("Login")
            window.bind("<Return>", lambda e: get_input())
            username_input.delete(0, "end")
            password_input.delete(0, "end")
            on_focus_out(username_input, "Username")
            on_focus_out2("")
    
    def sign():
        show_sign_up(0)
        
        window.title("Sign up")
        window.bind("<Return>", lambda e: add_user(username_input.get(), password_input.get()))
        
        sign_up_button.place(relx=0.5, y=240, anchor=CENTER)
        back.place(relx=0.5, y=280, anchor=CENTER)
    
    def on_focus_in(widgit, text):
        if widgit.get()==text:
            widgit.delete(0, "end")
            widgit.insert(0, '')
            widgit.config(foreground='black')
    
    def on_focus_out(widgit, text):
        if widgit.get()=='':
            widgit.insert(0, text)
            widgit.config(foreground='grey')
    
    def on_focus_in2(event):
        if password_input.get()=='Password':
            password_input.delete(0, "end")
            password_input.insert(0, '')
            password_input.config(foreground='black', show='*')
    
    def on_focus_out2(event):
        if password_input.get()=='':
            password_input.config(show='')
            password_input.insert(0, 'Password')
            password_input.config(foreground='grey')
    
    def login_func():
        window.quit()
        window.destroy()
    
    def get_input():
        nonlocal login_good, username, password
        
        username_text = username_input.get()
        password_text = password_input.get()
        
        for x in range(len(users)):
            if username_text==users[x]:
                username = users[x]
                password = passes[x]
        
        if username_text.strip()==username:
            if password_text.strip()==password:
                login_func()
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
    
    def do_binds(widget, text):
        widget.configure(foreground="grey")
        widget.insert(0, text)
        widget.bind("<FocusIn>", lambda e: on_focus_in(widget, text))
        widget.bind("<FocusOut>", lambda e: on_focus_out(widget, text))
    
    username = "HdKjZolFk"
    password = "MAcOHzedp"
    login_good = False
    users = []
    passes = []
    user_info = []
    
    ICON = (b'\x00\x00\x01\x00\x01\x00\x10\x10\x00\x00\x01\x00\x08\x00h\x05\x00\x00'
            b'\x16\x00\x00\x00(\x00\x00\x00\x10\x00\x00\x00 \x00\x00\x00\x01\x00'
            b'\x08\x00\x00\x00\x00\x00@\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
            b'\x00\x01\x00\x00\x00\x01') + b'\x00' * 1282 + b'\xff' * 64
    
    _, ICON_PATH = mkstemp()
    with open(ICON_PATH, 'wb') as icon_file:
        icon_file.write(ICON)
    
    # Making window
    window = Toplevel()
    window.geometry('{}x{}+{}+{}'.format(230, 180, window.winfo_screenwidth() // 2 - 230 // 2,
                                                   window.winfo_screenheight() // 2 - 170 // 2))
    window.bind("<Return>", lambda e: get_input())
    window.title("Login")
    window.iconbitmap('icon.ico')
    window.iconbitmap(default=ICON_PATH)
    window.protocol("WM_DELETE_WINDOW", lambda: close_window("warning", "yesno"))
    window.resizable(False, False)
    
    taken_var = StringVar()
    
    sign_up_button = Button(window, text="Sign up", width=10,
        command=lambda: add_user(username_input.get(), password_input.get()))
    taken_label = Label(window, textvariable=taken_var, foreground="red")
    
    # Logo image
    img = PhotoImage(file='Logo.png')
    img = img.subsample(2)
    img_label = Label(window, image=img)
    img_label.bind("<Button-1>", lambda e: login_func())
    img_label.place(relx=0.5, y=30, anchor=CENTER)
    
    wrong = StringVar()
    
    # Making buttons and labels and binding them
    error_label = Label(window, textvariable=wrong, foreground="red")
    login = Button(window, text="Login", width=10, command=get_input)
    sign_up = Label(window, text="Sign up")
    sign_up.bind("<Button-1>", lambda e: sign())
    back = Label(window, text="Back")
    back.bind("<Button-1>", lambda e: show_sign_up(1))
    
    # Prompt labels
    acount_info = Label(window, text="Acount:")
    personal_info = Label(window, text="Address:")
    
    # Making fonts
    f = Font(sign_up, sign_up.cget("font"))
    f.configure(underline=True, size=9)
    sign_up.configure(font=f)
    back.configure(font=f)
    
    # Making address and email inputs
    street_input = Entry(window)
    do_binds(street_input, "Street & house")
    
    city_input = Entry(window)
    do_binds(city_input, "City")
    
    postcode_input = Entry(window)
    do_binds(postcode_input, "Postcode")
    
    email_input = Entry(window)
    do_binds(email_input, "Email")
    
    # Making the password and username inputs
    username_input = Entry(window)
    do_binds(username_input, "Username")
    
    password_input = Entry(window)
    password_input.bind("<FocusIn>", on_focus_in2)
    password_input.bind("<FocusOut>", on_focus_out2)
    
    # Placing the widgets
    username_input.place(relx=0.5, y=67, anchor=CENTER)
    password_input.place(relx=0.5, y=95, anchor=CENTER)
    login.place(relx=0.5, y=125, anchor=CENTER)
    sign_up.place(relx=0.5, y=167, anchor=CENTER)
    
    get_logins()
    get_info()
    on_focus_out2("")
    
    window.mainloop()
    return login_good


root = Tk()
root.withdraw()
if login():
    print("Logged in")
