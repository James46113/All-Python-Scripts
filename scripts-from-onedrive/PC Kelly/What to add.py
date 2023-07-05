"""Add encrypt function"""


def encrypt(key: str, to_encrypt: str) -> str:
    global passes
    arr = [chr(x) for x in range(49, 123)]
    key_arr = [k for k in key]
    count = 0
    new = ""
    for char in range(len(to_encrypt)):
        temp = ord(to_encrypt[char]) - arr.index(key_arr[count]) + 39
        new += chr(temp)
        count += 1
        if count == len(key_arr):
            count = 0
    return new


"""Add decrypt function"""


def decrypt(key: str):
    global passes
    arr = [chr(x) for x in range(49, 123)]
    key_arr = [k for k in key]
    temp_arr = []
    count = 0
    for x in range(len(passes)):
        new = ""
        for char in range(len(passes[x])):
            temp = ord(passes[x][char]) + arr.index(key_arr[count]) - 39
            new += chr(temp)
            count += 1
            if count==len(key_arr):
                count = 0
        temp_arr.append(new)
    passes = temp_arr


"""Update get_logins function"""


def get_logins():
    global users, passes
    userpass = open("userpass.txt", "r")
    temp = userpass.read().split("\n")
    users = []
    passes = []
    for x in temp:
        tempuser, temppass = x.split(",")
        users.append(tempuser)
        passes.append(temppass)
    userpass.close()
    decrypt("hi")


"""Update add_user function"""


def add_user(username: str, password: str):
    if username!="" and password!="":
        good = True
        taken = False
        
        for x in username:
            if x==",":
                good = False
        for x in password:
            if x==",":
                good = False
        
        for x in users:
            if username==x:
                good = False
                taken = True
        
        if good:
            file = open("userpass.txt", "a")
            both = "\n" + username + "," + encrypt("hi", password)
            file.write(both)
            file.close()
            get_logins()
            show_sign_up(1)
        
        if taken:
            taken_label.place(relx=0.5, y=155, anchor=CENTER)
