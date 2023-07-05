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
nicknames = []
addresses = []


def broadcast(message):
    for client in clients:
        client.send(message)


def handle(client):
    while True:
        try:
            msg = message = client.recv(1024)
            print(msg.decode("ascii"))

            if msg.decode("ascii").startswith("EXIT"):
                index = clients.index(client)
                clients.remove(client)
                client.close()
                nickname = nicknames[index]
                nicknames.remove(nickname)
                addresses.remove(addresses[index])
                broadcast(f"{nickname} left the chat\n".encode("ascii"))
                break

            else:
                broadcast(message)
        except:
            if client in clients:
                index = clients.index(client)
                clients.remove(client)
                client.close()
                nickname = nicknames[index]
                nicknames.remove(nickname)
                addresses.remove(addresses[index])
                broadcast(f"{nickname} left the chat\n".encode("ascii"))
                break


def receive():
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}")

        client.send("NICK".encode("ascii"))
        nickname = client.recv(1024).decode("ascii")

        if nickname in nicknames:
            client.send("TAKEN".encode("ascii"))
            client.close()
            continue

        nicknames.append(nickname)
        clients.append(client)
        addresses.append(address[0])

        print(f"Nickname of client is {nickname}")
        broadcast(f"{nickname} joined the chat\n".encode("ascii"))
        client.send(f"Connected to the server\nYour IP: {address[0]}, PORT: {address[1]}\n".encode("ascii"))
        print(addresses)

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


print("Server active...")
receive()
