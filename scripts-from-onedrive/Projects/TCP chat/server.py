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

            if msg.decode("ascii").startswith("ADMIN"):
                if nicknames[clients.index(client)][0:5] == "owner":
                    try:
                        name_to_admin = msg.decode("ascii")[6:]
                        nicknames[nicknames.index(name_to_admin)] = "admin~" + name_to_admin
                        clients[nicknames.index(f"admin~{name_to_admin}")].send(f"NIC admin~{name_to_admin}".encode("ascii"))
                    except Exception as e:
                        print(e)
                else:
                    print("Did not work")

            elif msg.decode("ascii").startswith("USER"):
                if nicknames[clients.index(client)][0:5] == "owner":
                    try:
                        print(nicknames)
                        name_to_user = msg.decode("ascii")[6:]
                        nicknames[nicknames.index(name_to_user)] = name_to_user[6:]
                        print(name_to_user[6:])
                        clients[nicknames.index(f"{name_to_user[6:]}")].send(f"NIC {name_to_user[6:]}".encode("ascii"))
                    except Exception as e:
                        print(e)
                else:
                    print("Did not work")

            elif msg.decode("ascii").startswith("KICK"):
                if nicknames[clients.index(client)][0:5] == "admin" or nicknames[clients.index(client)][0:5] == "owner":
                    name_to_kick = msg.decode("ascii")[5:]
                    if name_to_kick != "ALL":
                        if name_to_kick[0:5] != "owner":
                            kick_user(name_to_kick)
                            print("asdf")
                        else:
                            client.send("RED You cannot kick an owner".encode("ascii"))
                            clients[nicknames.index(name_to_kick)].send(f"RED {nicknames[clients.index(client)]} tried to kick you!".encode("ascii"))

                    else:
                        for _ in range(4):
                            for na in nicknames:
                                if na[0:5] != "admin" and na[0:5] != "owner":
                                    kick_user(na)
                else:
                    client.send("RED Command was refused!".encode("ascii"))

            elif msg.decode("ascii").startswith("BAN"):
                if nicknames[clients.index(client)][0:5] == "admin" or nicknames[clients.index(client)][0:5] == "owner":
                    name_to_ban = msg.decode("ascii")[4:]
                    if name_to_ban != "ALL":
                        if name_to_ban[0:5] != "owner":
                            ban_user(name_to_ban)
                        else:
                            client.send("RED You cannot ban an owner".encode("ascii"))
                            clients[nicknames.index(name_to_ban)].send(f"RED {nicknames[clients.index(client)]} tried to ban you!".encode("ascii"))
                    else:
                        for _ in range(4):
                            for n in nicknames:
                                if n[0:5] != "admin" and n[0:5] != "owner":
                                    ban_user(n)
                else:
                    client.send("RED Command was refused!".encode("ascii"))

            elif msg.decode("ascii").startswith("UNBAN"):
                if nicknames[clients.index(client)][0:5] == "admin" or nicknames[clients.index(client)][0:5] == "owner":
                    name_to_unban = msg.decode("ascii")[6:]
                    unban_user(name_to_unban)
                else:
                    client.send("RED Command was refused!".encode("ascii"))

            elif msg.decode("ascii").startswith("IPBAN"):
                if nicknames[clients.index(client)][0:5] == "admin" or nicknames[clients.index(client)][0:5] == "owner":
                    name_to_ban = msg.decode("ascii")[6:]
                    if name_to_ban != "ALL":
                        if name_to_ban[0:5] != "owner":
                            ban_ip(name_to_ban)
                        else:
                            client.send("RED You cannot ipban an owner".encode("ascii"))
                            clients[nicknames.index(name_to_ban)].send(f"RED {nicknames[clients.index(client)]} tried to ipban you!".encode("ascii"))

                    else:
                        for _ in range(4):
                            for name in nicknames:
                                if name[0:5] != "admin" and name[0:5] != "owner":
                                    ban_ip(name)
                else:
                    client.send("RED Command was refused!".encode("ascii"))

            elif msg.decode("ascii").startswith("NOTIF"):
                if nicknames[clients.index(client)][0:5] == "admin" or nicknames[clients.index(client)][0:5] == "owner":
                    ms = msg.decode("ascii").split(" ")
                    who = ms[1]
                    what = msg.decode("ascii")[len(who)+1:]
                    if who != "ALL":
                        for name in nicknames:
                            if who == name:
                                ind = nicknames.index(name)
                                client_to_notif = clients[ind]
                                client_to_notif.send(f"NOTIF {what}".encode("ascii"))
                    else:
                        for cli in clients:
                            cli.send(f"NOTIF {what}".encode("ascii"))

                else:
                    client.send("RED Command was refused!".encode("ascii"))

            elif msg.decode("ascii").startswith("USERS"):
                for nickname in nicknames:
                    client.send(nickname.encode("ascii"))

            elif msg.decode("ascii").startswith("EXIT"):
                index = clients.index(client)
                clients.remove(client)
                client.close()
                nickname = nicknames[index]
                nicknames.remove(nickname)
                addresses.remove(addresses[index])
                broadcast(f"YELLOW {nickname} left the chat".encode("ascii"))
                break

            else:
                broadcast(message)
        except:
            if client in clients:
                index = clients.index(client)
                clients.remove(client)
                client.close()
                nickname = nicknames[index]
                broadcast(f"YELLOW {nickname} left the chat".encode("ascii"))
                nicknames.remove(nickname)
                addresses.remove(addresses[index])
                break


def receive():
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}")

        client.send("NICK".encode("ascii"))
        nickname = client.recv(1024).decode("ascii")

        with open("ip_bans.txt", "r") as f:
            ip_bans = f.readlines()

        if address[0]+"\n" in ip_bans:
            client.send("BAN".encode("ascii"))
            client.close()
            continue

        with open("name_bans.txt", "r") as f:
            name_bans = f.readlines()

        if nickname+"\n" in name_bans:
            client.send("BAN".encode("ascii"))
            client.close()
            continue

        if nickname[0:5] == "admin" or nickname[0:5] == "owner":
            client.send("PASS".encode("ascii"))
            password = client.recv(1024).decode("ascii")

            if password != "adminpass" and nickname[0:5] == "admin":
                client.send("REFUSED".encode("ascii"))
                client.close()
                continue

            elif password != "ownerpass" and nickname[0:5] == "owner":
                client.send("REFUSED".encode("ascii"))
                client.close()
                continue

        if nickname in nicknames:
            client.send("TAKEN".encode("ascii"))
            client.close()
            continue

        nicknames.append(nickname)
        clients.append(client)
        addresses.append(address[0])

        print(f"Nickname of client is {nickname}")
        broadcast(f"YELLOW {nickname} joined the chat".encode("ascii"))
        client.send(f"GREEN Connected to the server\nYour IP: {address[0]}, PORT: {address[1]}".encode("ascii"))
        print(addresses)

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


def unban_user(name):
    new_names = []
    with open("name_bans.txt", "r") as f:
        names = f.readlines()
    for n in names:
        if n != name+"\n":
            new_names.append(n)

    with open("name_bans.txt", "w") as f:
        f.writelines(new_names)

    broadcast(f"RED {name} was unbanned by an admin!".encode("ascii"))


def ban_user(name):
    if name in nicknames:
        with open("name_bans.txt", "a") as f:
            f.write(f"{name}\n")
        name_index = nicknames.index(name)
        client_to_kick = clients[name_index]
        clients.remove(client_to_kick)
        client_to_kick.send("You were banned by an admin!".encode("ascii"))
        client_to_kick.close()
        addresses.remove(addresses[name_index])
        nicknames.remove(name)
        broadcast(f"{name} was banned by an admin!".encode("ascii"))


def ban_ip(name):
    if name in nicknames:
        index = nicknames.index(name)
        ip = addresses[index]
        with open("ip_bans.txt", "a") as f:
            f.write(f"{ip}\n")
        with open("name_bans.txt", "a") as f:
            f.write(f"{name}\n")
        client_to_kick = clients[index]
        clients.remove(client_to_kick)
        nicknames.remove(name)
        addresses.remove(ip)
        client_to_kick.send("You were permanently banned by an admin!".encode("ascii"))
        client_to_kick.close()
        broadcast(f"{name} was permanently banned by an admin!".encode("ascii"))


def kick_user(name):
    if name in nicknames:
        name_index = nicknames.index(name)
        client_to_kick = clients[name_index]
        clients.remove(client_to_kick)
        client_to_kick.send("You were kicked by an admin!".encode("ascii"))
        client_to_kick.close()
        addresses.remove(addresses[name_index])
        nicknames.remove(name)
        broadcast(f"{name} was kicked by an admin!".encode("ascii"))


print("Server active...")
receive()
