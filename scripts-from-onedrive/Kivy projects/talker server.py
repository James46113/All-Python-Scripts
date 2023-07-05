from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
import socket
from threading import Thread
from kivy.core.window import Window


hostname = socket.gethostname()
host = socket.gethostbyname(hostname)
port = 55555
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
print(f"IP: {server.getsockname()[0]}\nPORT: {server.getsockname()[1]}")
server.listen()

clients = []


def broadcast(message):
    global clients
    for client in clients:
        try:
            client.send(message.encode("ascii"))
        except Exception as e:
            print(e)
            clients.remove(client)
            if len(clients) != 0:
                print("A computer left")
            else:
                print("There are no computers connected")


def receive():
    global clients
    while True:
        client, address = server.accept()
        clients.append(client)
        print(clients)


class LoginScreen(GridLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        Window.bind(on_key_down=self.key_action)
        self.cols = 1
        self.add_widget(Label(text='Enter Message'))
        self.message = TextInput(multiline=False)
        self.message.text = server.getsockname()[0]
        self.add_widget(self.message)
        self.button = Button(text='Send')
        self.button.bind(on_press=lambda e: [broadcast(self.message.text), self.wipe_message()])
        self.add_widget(self.button)

    def wipe_message(self):
        self.message.text = ""

    def key_action(self, *args):
        if list(args)[1] == 13:
            broadcast(self.message.text)
            self.wipe_message()


class MyApp(App):
    def build(self):
        return LoginScreen()


if __name__ == '__main__':
    t = Thread(target=receive)
    t.start()
    MyApp().run()