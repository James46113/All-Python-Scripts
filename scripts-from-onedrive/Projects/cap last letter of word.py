phrase_lst = input("enter phrase: ").split(" ")
capped_lst, capped = [], ""

for word in phrase_lst:
    if word == "":
        continue
    temp = ""
    puncts = ""
    punct_num = 0
    while 32 < ord(word[-1]) < 48 or 57 < ord(word[-1]) < 65 or 90 < ord(word[-1]) < 97 or 112 < ord(word[-1]) < 127:
        punct_num += 1
        puncts += word[-1]
        word = word[:-1]
        
    for ind in range(len(word)-1):
        temp += word[ind].lower()
    temp += word[-1].upper()
    if punct_num > 0:
        temp += puncts
    capped_lst.append(temp)


for word in capped_lst:
    capped += word + " "
print(capped)
