from pynput.keyboard import Key, Controller, Events
from time import sleep
#import os
#os.system('start self_writer.docx')
Keyboard = Controller()
#file = open("C:\James\spam_bot_source.txt", "r")
#phrase = file.read()
phrase = "Stop changing my name, I will not stop spamming. I have free speach!!!"
sleep(10)
for x in range(1000):
#while True:
    for letter in phrase:
        Keyboard.press(letter)
        Keyboard.release(letter)
#    for y in range(100):
#        Keyboard.press(Key.shift)
#        Keyboard.pres050s(Key.enter)
#        Keyboard.release(Key.shift)
#        Keyboard.release(Key.enter)
#    for letter in phrase:
#        Keyboard.press(letter)
#        Keyboard.release(letter)
    Keyboard.press(Key.enter)
    Keyboard.release(Key.enter)

