from smtplib import SMTP_SSL, SMTPRecipientsRefused
from ssl import create_default_context
from tkinter import *
from time import sleep


def new_message():
    def send(message, to):
        nonlocal email
        port = 465
        context = create_default_context()
        with SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            server.login("[YOUR EMAIL]", "[YOUR PASSWORD]")
            try:
                server.sendmail("[YOUR EMAIL]", to, message)
                email = """\
                """
            except SMTPRecipientsRefused:
                email = """\
                """
                sent_message(-1)
                return None
            sent_message(0)

    def sent_message(num):
        to_email.place_forget()
        subject_box.place_forget()
        email_text.place_forget()
        if num == -1:
            l = Label(tk, text="Invalid email", fg="red", font=(None, 40))
        elif num == 0:
            l = Label(tk, text="Email sent", fg="green", font=(None, 30))
            to_email.delete(0, "end")
            subject_box.delete(0, "end")
            email_text.delete("1.0", END)
            on_focus_out(subject_box, "Subject")
            on_focus_out(to_email, "Recipient")

        l.place(relx=0.5, rely=0.5, anchor=CENTER)
        tk.update()
        sleep(2)
        tk.destroy()

    def on_focus_in(widget, text):
        if widget.get() == text:
            widget.delete(0, "end")
            widget.insert(0, '')
            widget.config(foreground='black')

    def on_focus_out(widget, text):
        if widget.get() == '':
            widget.insert(0, text)
            widget.config(foreground='grey')
        if subject_box.get() != "Subject":
            tk.title(subject_box.get())

    def get_text():
        nonlocal email
        email += "\n"+"Subject: "+subject_box.get()+"\n"
        email += "\n"+email_text.get("1.0", END)
        email += "\n\nJames Caroe"
        send(email, to_email.get())

    tk = Tk()
    tk.geometry('{}x{}+{}+{}'.format(530, 380, tk.winfo_screenwidth()//2-530//2, tk.winfo_screenheight()//2-370//2))
    tk.title("New email")
    tk.bind("<Control-Return>", lambda e: get_text())

    email = """\
    """

    to_email = Entry(tk, width=30)
    to_email.bind("<FocusIn>", lambda e: on_focus_in(to_email, "Recipient"))
    to_email.bind("<FocusOut>", lambda e: on_focus_out(to_email, "Recipient"))
    to_email.place(x=50, y=20)

    subject_box = Entry(tk, width=30)
    subject_box.bind("<FocusIn>", lambda e: on_focus_in(subject_box, "Subject"))
    subject_box.bind("<FocusOut>", lambda e: on_focus_out(subject_box, "Subject"))
    subject_box.place(x=294, y=20)

    email_text = Text(tk, font=("Helvetica", 10), width=61, height=18)
    email_text.place(x=50, y=50)

    on_focus_out(subject_box, "Subject")
    on_focus_out(to_email, "Recipient")

    tk.mainloop()


new_message()
