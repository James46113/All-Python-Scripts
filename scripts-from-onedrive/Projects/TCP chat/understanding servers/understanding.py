import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 55555))
s.listen()

while True:
    client, address = s.accept()
    print(f"Connected to {address}")
    client.send("You are connected".encode("UTF-8"))
    client.close()