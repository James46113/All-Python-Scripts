from datetime import datetime
import smtplib, ssl

port = 465
now = datetime.now()
current_time = now.strftime("%H:%M:%S")

context = ssl.create_default_context()
message = f"""\
Subject: Activity@{current_time}

Someone logged onto your PC at {current_time}."""

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login("9.qk.c.2xmpu@gmail.com", "9.qk.c.2xmpu123")
    server.sendmail("9.qk.c.2xmpu@gmail.com", "jamescaroe@gmail.com", message)
    print("sent")
