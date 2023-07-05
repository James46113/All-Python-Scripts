class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def check(self, username, password):
        if username == self.username:
            if password == self.password:
                print("login sucsesful!")
    

user = User("u", "p")
user.check("u", "f")