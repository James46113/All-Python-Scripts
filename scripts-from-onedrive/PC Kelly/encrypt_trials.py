passes = []
temp_passes = []
f = open("userpass_encrypt.txt", "r")
temp = f.read().split("\n")
for x in temp:
    tempuser, temppass = x.split(",")
    temp_passes.append(temppass)


def encrypt(key: str):
    global passes
    key_arr = [ord(k) for k in key]
    temp_arr = []
    count = 0
    for x in range(len(passes)):
        new = ""
        for char in range(len(passes[x])):
            temp = ord(passes[x][char]) - key_arr[count] + 120
            new += chr(temp)
            count += 1
            if count == len(key_arr):
                count = 0
        temp_arr.append(new)
    
    passes = temp_arr


def decrypt(key: str):
    global passes
    key_arr = [ord(k) for k in key]
    temp_arr = []
    count = 0
    for x in range(len(passes)):
        new = ""
        for char in range(len(passes[x])):
            temp = ord(passes[x][char]) + key_arr[count] - 100
            new += chr(temp)
            count += 1
            if count == len(key_arr):
                count = 0
        temp_arr.append(new)
    passes = temp_arr
    

encrypt("dAke")
print(passes)
decrypt("dAke")
print(passes)