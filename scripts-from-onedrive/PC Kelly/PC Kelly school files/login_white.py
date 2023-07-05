from tkinter import *
from tkinter.font import *
from tkinter.commondialog import Dialog
from tempfile import mkstemp
from textwrap import fill


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
    if icon != "error" and icon != "info" and icon != "question" and icon != "warning":
        s = _show("Close?", "Do you want to close?", "warning", "yesno", **options)
    elif buttons != "abortretryignore" and buttons != "ok" and buttons != "okcancel" and buttons != "retrycancel" and buttons != "yesno" and buttons != "yesnocancel":
        s = _show("Close?", "Do you want to close?", icon, "yesno", **options)
    else:
        s = _show("Close?", "Do you want to close?", icon, buttons, **options)

    if s == "yes":
        root.destroy()


def login():
    global ICON_PATH, currentUser, key

    def get_info():
        nonlocal user_info
        f = open("userinfo.txt", "r")
        temp = f.read().split("\n")
        temp_arr = []
        for x in temp:
            user_info.append(x.split(','))
    """
    def decrypt(text):
        letters = [chr(l) for l in range(32, 127)]
        key_count = 0
        decrypted = []
        for x in range(len(text)):
            new = ""
            for char in range(len(text[x])):
                temp = chr(ord(text[x][char]) - letters.index(key[key_count]))
                new += temp
                key_count += 1
                if key_count == len(key):
                    key_count = 0
            decrypted.append(new)
        return decrypted

    def encrypt(text):
        letters = [chr(l) for l in range(32, 127)]
        key_count = 0
        encrypted = ""
        for char in range(len(text)):
            temp = ord(text[char]) + letters.index(key[key_count])
            encrypted += chr(temp)
            key_count += 1
            if key_count == len(key):
                key_count = 0
        return encrypted
    """
    def get_logins():
        nonlocal users, passes
        users = []
        passes = []
        with open("userpass.txt", "r") as f:
            temp = f.read().split("\n")
            for x in temp:
                tempuser, temppass = x.split(",")
                users.append(tempuser)
                passes.append(temppass)
        #users = decrypt(users)
        #passes = decrypt(passes)

    def email_check(email) -> bool:
        at = 0
        dot = 0

        for x in range(len(email)):
            if email[x] == "@":
                at = x
            elif email[x] == "." and at != 0:
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
        if street != "" and city != "" and postcode != "" and email != "":
            f = open("userinfo.txt", 'a')
            f.write("\n{},{},{},{},{}".format(username, street, city, postcode, email))
            f.close()
            return True

        else:
            taken_var.set("Fill all boxes")
            taken_label.place(relx=0.5, y=165, anchor=CENTER)
            return False

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

            if username in users:
                good = False
                taken_var.set("Username taken")

            if good:
                if email_check(email_input.get()):
                    if add_address():
                        file = open("userpass.txt", "a")
                        #both = "\n" + str(encrypt(username)) + "," + str(encrypt(password))
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
        if num == 0:
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

            street_input.delete(0, "end")
            city_input.delete(0, "end")
            postcode_input.delete(0, "end")
            email_input.delete(0, "end")

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
        if widgit.get() == text:
            widgit.delete(0, "end")
            widgit.insert(0, '')
            widgit.config(fg='black')

    def on_focus_out(widgit, text):
        if widgit.get() == '':
            widgit.insert(0, text)
            widgit.config(fg='grey')

    def on_focus_in2(event):
        if password_input.get() == 'Password':
            password_input.delete(0, "end")
            password_input.insert(0, '')
            password_input.config(fg='black', show='*')

    def on_focus_out2(event):
        if password_input.get() == '':
            password_input.config(show='')
            password_input.insert(0, 'Password')
            password_input.config(fg='grey')

    def login_func():
        window.quit()
        window.destroy()
        change("ac", "")

    def get_input():
        nonlocal login_good, username, password
        global currentUser

        username_text = username_input.get()
        password_text = password_input.get()

        for x in range(len(users)):
            if username_text == users[x]:
                username = users[x]
                password = passes[x]

        if username_text.strip() == username:
            if password_text.strip() == password:
                currentUser = username
                login_func()
                login_good = True
                wrong_password = False
            else:
                if password_input.get() != "Password":
                    password_input.delete(0, "end")
                wrong_password = True
                wrong.set("Wrong password")
        else:
            if password_input.get() != "Password":
                password_input.delete(0, "end")
            wrong_password = True
            wrong.set("Invalid username")
        if wrong_password:
            error_label.place(relx=0.5, y=148, anchor=CENTER)

    def do_binds(widget, text):
        widget.configure(fg="grey")
        widget.insert(0, text)
        widget.bind("<FocusIn>", lambda e: on_focus_in(widget, text))
        widget.bind("<FocusOut>", lambda e: on_focus_out(widget, text))

    username = "HdKjZolFk"
    password = "MAcOHzedp"
    login_good = False
    users = []
    passes = []
    user_info = []

    # Making window
    window = Toplevel(root)
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
    taken_label = Label(window, textvariable=taken_var, fg="red")

    # Logo image
    img = PhotoImage(file='Logo.png')
    img = img.subsample(2)
    img_label = Label(window, image=img, bd=0)
    img_label.bind("<Button-1>", lambda e: login_func())
    img_label.place(relx=0.5, y=30, anchor=CENTER)

    wrong = StringVar()

    # Making buttons and labels and binding them
    error_label = Label(window, textvariable=wrong, fg="red")
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
    f.configure(underline=True)
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
    #get_info()
    on_focus_out2("")
    window.mainloop()


def ac():
    global ICON_PATH, login

    def logout():
        current_screen.set("Login")
        ac_window.destroy()
        login()

    def change_func(event):
        menu.post(ac_window.winfo_x() + 570, ac_window.winfo_y() + 70)

    ac_window = Toplevel(root)
    ac_window.focus_set()
    ac_window.geometry('{}x{}+{}+{}'.format(700, 500, ac_window.winfo_screenwidth() // 2 - 700 // 2,
                                            ac_window.winfo_screenheight() // 2 - 500 // 2))
    ac_window.title("PC Kelly")
    ac_window.iconbitmap('icon.ico')
    ac_window.iconbitmap(default=ICON_PATH)
    ac_window.protocol("WM_DELETE_WINDOW", lambda: close_window("warning", "yesno"))
    ac_window.resizable(False, False)

    img = PhotoImage(file='Logo.png')
    img = img.subsample(2)
    img_label = Label(ac_window, image=img, bd=0)
    img_label.place(x=10, y=15)

    menu = Menu(ac_window, tearoff=0)
    menu.add_command(label="My boiler",
                     command=lambda: [current_screen.set("My boiler ▾"), change("boiler", ac_window)])
    menu.add_command(label="Plumbing services",
                     command=lambda: [current_screen.set("Plumbing services ▾"), change("plumb", ac_window)])
    menu.add_command(label="Other products",
                     command=lambda: [current_screen.set("Other products ▾"), change("prod", ac_window)])
    menu.add_command(label="Special offers",
                     command=lambda: [current_screen.set("Special offers ▾"), change("SO", ac_window)])
    menu.add_command(label="Logout", command=lambda: logout())

    current_screen = StringVar()
    current_screen.set("Air conditioning ▾")
    changel = Label(ac_window, textvariable=current_screen, font=(None, 12))
    changel.bind("<Button-1>", change_func)
    changel.place(x=620, y=27, anchor=CENTER)

    line = Label(ac_window, text="___" * 50)
    line.place(x=-10, y=50)

    if get_user_ac_data().endswith("quote."):
        ac_img = PhotoImage(file="ac_image.png")
        ac_img = ac_img.subsample(3)
        ac_img_label = Label(ac_window, image=ac_img, bd=0)
        ac_img_label.place(relx=0.8, rely=0.4, anchor=CENTER)

        info = """PC Kelly offer a range of installation services, which begin with a member of our team visiting your premises to discuss your needs.

Operating throughout the country we’re never far away. PC Kelly also offer service and maintenance programs to keep your equipment in a safe and good working condition."""

        ac_info = Label(ac_window, text=fill(info, 85)).place(relx=0.35, rely=0.4, anchor=CENTER)

        contact_img = PhotoImage(file="contact_us.png")
        contact_img = contact_img.subsample(2)
        contact_label = Label(ac_window, image=contact_img, bd=0)
        contact_label.place(relx=0.55, rely=0.775, anchor=CENTER)

    l = Label(ac_window, text=get_user_ac_data(), font=(None, 14))
    l.place(relx=0.5, rely=0.2, anchor=CENTER)

    ac_window.focus_set()
    ac_window.mainloop()


def boiler():
    global ICON_PATH, login

    def logout():
        current_screen.set("Login")
        boiler_window.destroy()
        login()

    def change_func(event):
        menu.post(boiler_window.winfo_x() + 570, boiler_window.winfo_y() + 70)

    boiler_window = Toplevel(root)
    boiler_window.focus_set()
    boiler_window.geometry('{}x{}+{}+{}'.format(700, 500, boiler_window.winfo_screenwidth() // 2 - 700 // 2,
                                                boiler_window.winfo_screenheight() // 2 - 500 // 2))
    boiler_window.title("PC Kelly")
    boiler_window.iconbitmap('icon.ico')
    boiler_window.iconbitmap(default=ICON_PATH)
    boiler_window.protocol("WM_DELETE_WINDOW", lambda: close_window("warning", "yesno"))
    boiler_window.resizable(False, False)

    img = PhotoImage(file='Logo.png')
    img = img.subsample(2)
    img_label = Label(boiler_window, image=img, bd=0)
    img_label.place(x=10, y=15)

    menu = Menu(boiler_window, tearoff=0)
    menu.add_command(label="My air conditioning",
                     command=lambda: [current_screen.set("My Air Con ▾"), change("ac", boiler_window)])
    menu.add_command(label="Plumbing services",
                     command=lambda: [current_screen.set("Plumbing services ▾"), change("plumb", boiler_window)])
    menu.add_command(label="Other products",
                     command=lambda: [current_screen.set("Other products ▾"), change("prod", boiler_window)])
    menu.add_command(label="Special offers",
                     command=lambda: [current_screen.set("Special offers ▾"), change("SO", boiler_window)])
    menu.add_command(label="Logout", command=lambda: logout())

    current_screen = StringVar()
    current_screen.set("My Boiler ▾")
    changel = Label(boiler_window, textvariable=current_screen, font=(None, 12))
    changel.bind("<Button-1>", change_func)
    changel.place(x=620, y=27, anchor=CENTER)

    line = Label(boiler_window, text="___" * 50)
    line.place(x=-10, y=50)

    if get_user_ac_data().endswith("quote."):
        b_img = PhotoImage(file="boiler_image.png")
        b_img = b_img.subsample(4)
        b_img_label = Label(boiler_window, image=b_img, bd=0)
        b_img_label.place(relx=0.9, rely=0.4, anchor=CENTER)

        info = """PC Kelly offer a range of installation services, which begin with a member of our team visiting your premises to discuss your needs.
Operating throughout the country we’re never far away. PC Kelly also offer service and maintenance programs to keep your equipment in a safe and good working condition."""

        Label(boiler_window, text=fill(info, 85)).place(relx=0.45, rely=0.4, anchor=CENTER)

    contact_img = PhotoImage(file="contact_us.png")
    contact_img = contact_img.subsample(2)
    contact_label = Label(boiler_window, image=contact_img, bd=0)
    contact_label.place(relx=0.55, rely=0.775, anchor=CENTER)

    l = Label(boiler_window, text=get_user_boiler_data(), font=(None, 14))
    l.place(relx=0.5, rely=0.2, anchor=CENTER)

    boiler_window.focus_set()
    boiler_window.mainloop()


def plumb():
    global ICON_PATH, login

    def logout():
        current_screen.set("Login")
        plumbing_window.destroy()
        login()

    def change_func(event):
        menu.post(plumbing_window.winfo_x() + 570, plumbing_window.winfo_y() + 70)

    plumbing_window = Toplevel(root)
    plumbing_window.focus_set()
    plumbing_window.geometry('{}x{}+{}+{}'.format(700, 500, plumbing_window.winfo_screenwidth() // 2 - 700 // 2,
                                                plumbing_window.winfo_screenheight() // 2 - 500 // 2))
    plumbing_window.title("PC Kelly")
    plumbing_window.iconbitmap('icon.ico')
    plumbing_window.iconbitmap(default=ICON_PATH)
    plumbing_window.protocol("WM_DELETE_WINDOW", lambda: close_window("warning", "yesno"))
    plumbing_window.resizable(False, False)

    img = PhotoImage(file='Logo.png')
    img = img.subsample(2)
    img_label = Label(plumbing_window, image=img, bd=0)
    img_label.place(x=10, y=15)

    menu = Menu(plumbing_window, tearoff=0)
    menu.add_command(label="My air conditioning" ,
                     command=lambda: [current_screen.set("My Air Con ▾"), change("ac", plumbing_window)])
    menu.add_command(label="Plumbing services",
                     command=lambda: [current_screen.set("Plumbing services▾"), change("plumb", plumbing_window)])
    menu.add_command(label="Other products",
                     command=lambda: [current_screen.set("Other products ▾"), change("prod", plumbing_window)])
    menu.add_command(label="Special offers",
                     command=lambda: [current_screen.set("Special offers ▾"), change("SO", plumbing_window)])
    menu.add_command(label="Logout", command=lambda: logout())

    current_screen = StringVar()
    current_screen.set("Plumbing services ▾")
    changel = Label(plumbing_window, textvariable=current_screen, font=(None, 12))
    changel.bind("<Button-1>", change_func)
    changel.place(x=620, y=27, anchor=CENTER)

    line = Label(plumbing_window, text="___" * 50)
    line.place(x=-10, y=50)

    if get_user_p_data().endswith("quote."):
        p_img = PhotoImage(file="plumbing-image.png")
        p_img = p_img.subsample(4)
        p_img_label = Label(plumbing_window, image=p_img, bd=0)
        p_img_label.place(relx=0.9, rely=0.4, anchor=CENTER)

        info = """PC Kelly offer a range of installation services, which begin with a member of our team visiting your premises to discuss your needs.
    Operating throughout the country we’re never far away. PC Kelly also offer service and maintenance programs to keep your equipment in a safe and good working condition."""

        Label(plumbing_window, text=fill(info, 85)).place(relx=0.45, rely=0.4, anchor=CENTER)

    contact_img = PhotoImage(file="contact_us.png")
    contact_img = contact_img.subsample(2)
    contact_label = Label(plumbing_window, image=contact_img, bd=0)
    contact_label.place(relx=0.55, rely=0.775, anchor=CENTER)

    l = Label(plumbing_window, text=get_user_p_data(), font=(None, 14))
    l.place(relx=0.5, rely=0.2, anchor=CENTER)

    plumbing_window.focus_set()
    plumbing_window.mainloop()


def prod():
    global ICON_PATH, login

    def logout():
        current_screen.set("login")
        prod_window.destroy()
        login()

    def change_func(event):
        menu.post(prod_window.winfo_x() + 570, prod_window.winfo_y() + 70)

    prod_window = Toplevel(root)
    prod_window.focus_set()
    prod_window.geometry('{}x{}+{}+{}'.format(700, 500, prod_window.winfo_screenwidth() // 2 - 700 // 2,
                                                  prod_window.winfo_screenheight() // 2 - 500 // 2))
    prod_window.title("PC Kelly")
    prod_window.iconbitmap('icon.ico')
    prod_window.iconbitmap(default=ICON_PATH)
    prod_window.protocol("WM_DELETE_WINDOW", lambda: close_window("warning", "yesno"))
    prod_window.resizable(False, False)

    img = PhotoImage(file='Logo.png')
    img = img.subsample(2)
    img_label = Label(prod_window, image=img, bd=0)
    img_label.place(x=10, y=15)

    menu = Menu(prod_window, tearoff=0)
    menu.add_command(label="My air conditioning",
                     command=lambda: [current_screen.set("My Air Con ▾"), change("ac", prod_window)])
    menu.add_command(label="Plumbing services",
                     command=lambda: [current_screen.set("Plumbing services▾"), change("plumb", prod_window)])
    menu.add_command(label="Other products",
                     command=lambda: [current_screen.set("Other products ▾"), change("prod", prod_window)])
    menu.add_command(label="Special offers",
                     command=lambda: [current_screen.set("Special offers ▾"), change("SO", prod_window)])
    menu.add_command(label="Logout", command=lambda: logout())

    current_screen = StringVar()
    current_screen.set("Other products ▾")
    changel = Label(prod_window, textvariable=current_screen, font=(None, 12))
    changel.bind("<Button-1>", change_func)
    changel.place(x=620, y=27, anchor=CENTER)

    line = Label(prod_window, text="___" * 50)
    line.place(x=-10, y=50)

    info = """PC Kelly offer a range of installation services, we service and provide air conditioning, boilers, and plumbing.
If you would like to see some of our products, please contact us with the infomation below. One of our expert team members will come and have a look at what would suit you best."""


    info_img = PhotoImage(file="products.png")
    info_img = info_img.subsample(2)
    info_label = Label(prod_window, image=info_img, bd=0)
    info_label.place(relx=0.5, rely=0.45, anchor=CENTER)

    Label(prod_window, font=(None, 12), text=fill(info, 100)).place(relx=0.5, rely=0.2, anchor=CENTER)

    contact_img = PhotoImage(file="contact_us.png")
    contact_img = contact_img.subsample(2)
    contact_label = Label(prod_window, image=contact_img, bd=0)
    contact_label.place(relx=0.55, rely=0.775, anchor=CENTER)

    prod_window.focus_set()
    prod_window.mainloop()


def SO():
    global ICON_PATH, login

    def logout():
        current_screen.set("login")
        so_window.destroy()
        login()

    def change_func(event):
        menu.post(so_window.winfo_x() + 570, so_window.winfo_y() + 70)

    so_window = Toplevel(root)
    so_window.focus_set()
    so_window.geometry('{}x{}+{}+{}'.format(700, 500, so_window.winfo_screenwidth() // 2 - 700 // 2,
                                              so_window.winfo_screenheight() // 2 - 500 // 2))
    so_window.title("PC Kelly")
    so_window.iconbitmap('icon.ico')
    so_window.iconbitmap(default=ICON_PATH)
    so_window.protocol("WM_DELETE_WINDOW", lambda: close_window("warning", "yesno"))
    so_window.resizable(False, False)

    img = PhotoImage(file='Logo.png')
    img = img.subsample(2)
    img_label = Label(so_window, image=img, bd=0)
    img_label.place(x=10, y=15)

    menu = Menu(so_window, tearoff=0)
    menu.add_command(label="My air conditioning",
                     command=lambda: [current_screen.set("My Air Con ▾"), change("ac", so_window)])
    menu.add_command(label="Plumbing services",
                     command=lambda: [current_screen.set("Plumbing services▾"), change("plumb", so_window)])
    menu.add_command(label="Other products",
                     command=lambda: [current_screen.set("Other products ▾"), change("prod", so_window)])
    menu.add_command(label="Special offers",
                     command=lambda: [current_screen.set("Special offers ▾"), change("SO", so_window)])
    menu.add_command(label="Logout", command=lambda: logout())

    current_screen = StringVar()
    current_screen.set("Special Offers ▾")
    changel = Label(so_window, textvariable=current_screen, font=(None, 12))
    changel.bind("<Button-1>", change_func)
    changel.place(x=620, y=27, anchor=CENTER)

    line = Label(so_window, text="___" * 50)
    line.place(x=-10, y=50)

    info = """PC Kelly provides special offers for first time and long-time customers. These include 10% off your first air conditioning unit, 40% of your 5th boiler service, etc.
Contact us to see if you are eligable today!"""

    info_img = PhotoImage(file="products.png")
    info_img = info_img.subsample(2)
    info_label = Label(so_window, image=info_img, bd=0)
    info_label.place(relx=0.5, rely=0.45, anchor=CENTER)

    Label(so_window, font=(None, 12), text=fill(info, 100)).place(relx=0.5, rely=0.2, anchor=CENTER)

    contact_img = PhotoImage(file="contact_us.png")
    contact_img = contact_img.subsample(2)
    contact_label = Label(so_window, image=contact_img, bd=0)
    contact_label.place(relx=0.55, rely=0.775, anchor=CENTER)

    so_window.focus_set()
    so_window.mainloop()


def change(to, curr):
    if curr != "":
        curr.destroy()
    if to == "ac":
        ac()
    elif to == "boiler":
        boiler()
    elif to == "plumb":
        plumb()
    elif to == "prod":
        prod()
    elif to == "SO":
        SO()


def get_user_ac_data():
    global currentUser
    usernames = []
    userdata = []

    with open("useracdata.txt", "r") as f:
        temp = f.readlines()
        if temp != None:
            for x in temp:
                if x != "":
                    tempn, tempd = x.split(",", 1)
                    usernames.append(tempn)
                    userdata.append(tempd)
    if currentUser in usernames:
        pos = usernames.index(currentUser)
        return userdata[pos]
    else:
        create_user_ac_data()
        return "No air con found, contact PC Kelly for a free quote."


def create_user_ac_data():
    with open("userdata.txt", "a") as f:
        f.write(f"\n{currentUser},No air con found, contact PC Kelly for a free quote.")


def get_user_p_data():
    global currentUser
    usernames = []
    userdata = []

    with open("userpdata.txt", "r") as f:
        temp = f.readlines()
        if temp != None:
            for x in temp:
                if x != "":
                    tempn, tempd = x.split(",", 1)
                    usernames.append(tempn)
                    userdata.append(tempd)
    if currentUser in usernames:
        pos = usernames.index(currentUser)
        return userdata[pos]
    else:
        create_user_ac_data()
        return "No plumbing found, contact PC Kelly for a free quote."


def create_user_p_data():
    with open("userpdata.txt", "a") as f:
        f.write(f"\n{currentUser},No plumbing found, contact PC Kelly for a free quote.")


def get_user_boiler_data():
    global currentUser
    usernames = []
    userdata = []

    with open("userboilerdata.txt", "r") as f:
        temp = f.readlines()
        if temp != None:
            for x in temp:
                if x != "":
                    tempn, tempd = x.split(",", 1)
                    usernames.append(tempn)
                    userdata.append(tempd)
    if currentUser in usernames:
        pos = usernames.index(currentUser)
        return userdata[pos]
    else:
        create_user_ac_data()
        return "No boiler found, contact PC Kelly for a free quote."


def create_user_boiler_data():
    with open("userdata.txt", "a") as f:
        f.write(f"\n{currentUser},No boiler found, contact PC Kelly for a free quote.")


try:
    ICON = (b'\x00\x00\x01\x00\x01\x00\x10\x10\x00\x00\x01\x00\x08\x00h\x05\x00\x00'
            b'\x16\x00\x00\x00(\x00\x00\x00\x10\x00\x00\x00 \x00\x00\x00\x01\x00'
            b'\x08\x00\x00\x00\x00\x00@\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
            b'\x00\x01\x00\x00\x00\x01') + b'\x00' * 1282 + b'\xff' * 64

    _, ICON_PATH = mkstemp()
    with open(ICON_PATH, 'wb') as icon_file:
        icon_file.write(ICON)
except Exception as e:
    import sys

    print(e)
    sys.exit()

currentUser = ""
key = "asdf"
root = Tk()
root.withdraw()
root.title("root")
login()
