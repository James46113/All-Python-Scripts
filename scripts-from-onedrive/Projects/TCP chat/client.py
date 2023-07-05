import socket
import threading
from colorama import init
from win10toast import ToastNotifier

t = ToastNotifier()
init()
IP = input("Enter IP: ") #"192.168.137.1"  # input("Enter IP address: ")
nickname = input("Choose a nickname: ")
if nickname[0:5] == "admin" or nickname[0:5] == "owner":
    password = input("Enter password: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client.connect((IP, 55555))
except:
    print("The server is not active at the moment, please try again later")

stop_thread = False

RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
PINK = '\033[95m'
CYAN = '\033[96m'
GREY = '\033[37m'
WHITE = '\033[97m'
OWNER = '\033[31m'


def receive():
    while True:
        global stop_thread, nickname
        if stop_thread:
            break
        try:
            message = client.recv(1024).decode("ascii")
            if message == "NICK":
                client.send(nickname.encode("ascii"))
                next_message = client.recv(1024).decode("ascii")
                if next_message == "PASS":
                    client.send(password.encode("ascii"))
                    if client.recv(1024).decode("ascii") == "REFUSED":
                        print(f"{RED}Connection refused! Wrong password!{WHITE}")
                        stop_thread = True
                        quit()

                elif next_message == "BAN":
                    print(f"{RED}Connection refused because of ban!{WHITE}")
                    stop_thread = True

                elif next_message == "TAKEN":
                    print(f"{RED}Nickname taken!{WHITE}")
                    stop_thread = True

            elif message.startswith("NOTIF"):
                mes = message[len(nickname)+8:]
                print("got mes")
                msg = mes.split(": ")
                print(f"{msg[0]}\n{msg[1]}")
                t.show_toast(msg[0], msg[1], icon_path=None)
                print("sent notif")

            elif message.startswith("NIC"):
                nickname = message[4:]

            elif message.startswith("BCAST"):
                print(PINK+message[6:]+WHITE)

            elif message.startswith("GREEN"):
                print(GREEN+message[6:]+WHITE)

            elif message.startswith("RED"):
                print(RED+message[4:]+WHITE)

            elif message.startswith("YELLOW"):
                print(YELLOW+message[7:]+WHITE)

            elif message.endswith("by an admin!"):
                print(RED+message+WHITE)

            elif message.startswith("admin"):
                print(CYAN+message+WHITE)

            elif message.startswith("owner"):
                print(OWNER+message+WHITE)

            else:
                print(message)

        except Exception as e:
            print(f"{RED}Error: {e}")
            print(f"An error occurred{WHITE}")
            client.close()
            stop_thread = True
            break


def write():
    while True:
        global stop_thread
        if stop_thread:
            break
        message = f"{nickname}: {input('')}"
        if message != "":
            try:
                if message[len(nickname)+2] == '/':
                    if str(message[len(nickname)+2:]).startswith('/exit'):
                        client.send("EXIT".encode("ascii"))
                        stop_thread = True
                    elif str(message[len(nickname) + 2:]).startswith('/users'):
                        client.send("USERS".encode("ascii"))

                    elif nickname[0:5] == "admin" or nickname[0:5] == "owner":
                        if str(message[len(nickname)+2:]).startswith('/kick'):
                            client.send(f"KICK {message[len(nickname)+8:]}".encode("ascii"))

                        elif str(message[len(nickname)+2:]).startswith('/ban'):
                            client.send(f"BAN {message[len(nickname)+7:]}".encode("ascii"))

                        elif str(message[len(nickname)+2:]).startswith('/unban'):
                            client.send(f"UNBAN {message[len(nickname)+9:]}".encode("ascii"))

                        elif str(message[len(nickname)+2:]).startswith('/ipban'):
                            client.send(f"IPBAN {message[len(nickname)+9:]}".encode("ascii"))

                        elif str(message[len(nickname)+2:]).startswith('/broadcast'):
                            client.send(f"BCAST {message[len(nickname)+13:]}".encode("ascii"))

                        elif str(message[len(nickname)+2:]).startswith('/notif'):
                            client.send(f"NOTIF {message[len(nickname)+9:]}".encode("ascii"))

                        elif str(message[len(nickname)+2:]).startswith('/sudo'):
                            client.send(message[len(nickname)+8:].encode("ascii"))

                        elif nickname[0:5] == "owner":
                            if str(message[len(nickname)+2:]).startswith('/admin'):
                                client.send(f"ADMIN {message[len(nickname)+9:]}".encode("ascii"))

                            elif str(message[len(nickname)+2:]).startswith('/user'):
                                client.send(f"USER {message[len(nickname) + 7:]}".encode("ascii"))

                        else:
                            print(f"{RED}Invalid command!{WHITE}")

                    else:
                        print(f"{RED}Invalid Command!{WHITE}")
                else:
                    client.send(message.encode("ascii"))
            except Exception as e:
                print(e)


receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
