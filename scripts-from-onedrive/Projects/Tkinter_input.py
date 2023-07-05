from tkinter import *

#the_file = open("C:\\James\\Python\\Projects\\password.txt", "r")
#username = the_file.readline().strip()
#password = the_file.readline()
username = "u"
password = "p"
username_text = ""
password_text = ""
good_login = False


def get_input():
    global username_text
    global password_text
    global good_login
    wrong = False
    username_text = username_input.get()
    password_text = password_input.get()
    if username_text.strip() == username.strip():
        if password_text.strip() == password.strip():
            the_label.destroy()
            username_input.destroy()
            password_input.destroy()
            login.destroy()
            login_window.destroy()
            good_login = True
        else:
            password_input.delete(0, "end")
            wrong = True
    else:
        password_input.delete(0, "end")
        wrong = True
    if wrong:
        wrong_label = Label(text="Wrong username or password", fg="red")
        wrong_label.pack()


login_window = Tk()
login_window.geometry("200x120+650+300")
login = Button(text="Login", command=get_input)
the_label = Label(text="Enter login details")
username_input = Entry()
password_input = Entry(show='*')


the_label.pack()
username_input.pack()
password_input.pack()
login.pack()

login_window.mainloop()
if good_login:
    window = Tk()
    window.geometry("500x200+500+200")
    welcome_label = Label(text="Well done, you have guessed the username and password!")
    welcome_label.pack()
    window.mainloop()
