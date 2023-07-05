passes = []
f = open("userpass_encrypt.txt", "r")
temp = f.read().split("\n")
for x in temp:
    tempuser, temppass = x.split(",")
    passes.append(temppass)

print(passes)
encrypt_passes = []


def encrypt(key: str):
    global passes, encrypt_passes
    key_arr = [k for k in key]
    encrypt_passes = []
    count = 0
    for x in range(len(passes)):
        new = ""
        for char in range(len(passes[x])):
            temp = ord(passes[x][char]) + ord(key_arr[count])
            #print(temp)
            new += chr(temp)
            count += 1
            if count == len(key_arr):
                count = 0
        encrypt_passes.append(new)
        
    for x in encrypt_passes:
        print(x)


def decrypt(key: str):
    global passes, encrypt_passes
    key_arr = [k for k in key]
    temp_passes = []
    count = 0
    for x in range(len(encrypt_passes)):
        new = ""
        for char in range(len(encrypt_passes[x])):
            temp = ord(encrypt_passes[x][char]) - ord(key_arr[count])
            new += chr(temp)
            count += 1
            if count == len(key_arr):
                count = 0
        temp_passes.append(new)
    passes = temp_passes
    
    print(passes)


#  use vigenere cipher or caesar cipher
encrypt("hello")
decrypt("hello")
