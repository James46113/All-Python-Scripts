import threading
import socket

hostname = socket.gethostname()
host = socket.gethostbyname(hostname)
port = 55555
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
print(f"IP: {server.getsockname()[0]}\nPORT: {server.getsockname()[1]}")
server.listen()

clients = []


def broadcast(message):
    for client in clients:
        try:
            client.send(message)
        except Exception as e:
            print(e)
            clients.remove(client)
            if len(clients) != 0:
                print("A computer left")
            else:
                print("There are no computers connected")


def receive():
    while True:
        client, address = server.accept()
        clients.append(client)


t = threading.Thread(target=receive)
t.start()
while True:
    broadcast(input("Enter message: ").encode("ascii"))
