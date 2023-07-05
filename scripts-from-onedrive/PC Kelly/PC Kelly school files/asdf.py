def encrypt(key: str, text):
    letters = [chr(l) for l in range(32, 127)]
    key_count = 0
    if isinstance(text, list):
        encrypted = []
        for x in range(len(text)):
            new = ""
            for char in range(len(text[x])):
                temp = chr(ord(text[x][char]) + letters.index(key[key_count]))
                new += temp
                key_count += 1
                if key_count == len(key):
                    key_count = 0
            encrypted.append(new)
        return encrypted
    else:
        encrypted = ""
        for char in range(len(text)):
            temp = ord(text[char]) + letters.index(key[key_count])
            encrypted += chr(temp)
            key_count += 1
            if key_count == len(key):
                key_count = 0
        return encrypted


def decrypt(key: str, text):
    letters = [chr(l) for l in range(32, 127)]
    key_count = 0
    if isinstance(text, list):
        decrypted = []
        for x in range(len(text)):
            new = ""
            for char in range(len(text[x])):
                temp = text[x][char].encode('utf-8') - letters.index(key[key_count])
                temp = temp.decode('utf-8')
                new += temp
                key_count += 1
                if key_count == len(key):
                    key_count = 0
            decrypted.append(new)
        return decrypted
    else:
        decrypted = ""
        for char in range(len(text)):
            temp = (text[x][char].encode('utf-8') - letters.index(key[key_count])).decode('utf-8')
            decrypted += chr(temp)
            key_count += 1
            if key_count == len(key):
                key_count = 0
        return decrypted



with open("userpass.txt", "r", encoding="ANSI") as f:
    temp = f.read().split("\n")
    for x in temp:
        t_u = x.split(",")
        t_p = x.split(",")
        print(decrypt("asdf", t_u))
        print(decrypt("asdf", t_p))



while True:
    x = encrypt("asdf", input())
    if x != "":
        print("\n",x)
    else:
        break
