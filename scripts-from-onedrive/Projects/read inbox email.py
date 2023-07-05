from smtplib import SMTP_SSL
from ssl import create_default_context
from imaplib import IMAP4


def send():
    message = """\
Subject: the subject
        
The message"""
    port = 465
    context = create_default_context()
    with SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("9.qk.c.2xmpu@gmail.com", "9.qk.c.2xmpu123")
        server.sendmail("9.qk.c.2xmpu@gmail.com", "jamescaroe@gmail.com", message)


imap = IMAP4("imap.gmail.com")
imap.login("9.qk.c.2xmpu@gmail.com", "9.qk.c.2xmpu123")
imap.check()
print("checked")
