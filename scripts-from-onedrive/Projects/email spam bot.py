import smtplib, ssl

port = 465

context = ssl.create_default_context()
message = f"""\
Subject: Message {1}

Hi! I have spammed you {1} time"""

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login("9.qk.c.2xmpu@gmail.com", "9.qk.c.2xmpu123")
    for x in range(5):
        server.sendmail("9.qk.c.2xmpu@gmail.com", "jamescaroe@gmail.com", message)
