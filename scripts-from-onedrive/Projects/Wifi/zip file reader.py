import zipfile, os

password = ""
for num in [83, 97, 110, 100, 50, 48, 50, 48]:
    password += chr(num)

with zipfile.ZipFile("C:/Users/James/OneDrive/Documents/Projects/Zip files/passwords.zip") as f:
    ex = f.extractall(path="C:/Users/James/OneDrive/Documents/Projects/Zip files", pwd=password.encode("ASCII"))

with open("asdf.txt", "r") as f:
    print(f.read())

os.remove("C:/Users/James/OneDrive/Documents/Projects/Zip files/asdf.txt")
    
