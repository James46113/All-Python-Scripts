from datetime import datetime, date
from playsound import playsound
from time import sleep
today = date.today()
now = datetime.now()

the_date = today.strftime("%d/%m/%Y")
the_time = now.strftime("%H:%M")
current_time = now.strftime("%H:%M:%S")

print(the_date)
print("Current Time =", the_time)

alarm_date = input("Enter date for alarm\n>>>")
alarm_time = input("Enter time for alarm\n>>>")
while True:
    today = date.today()
    now = datetime.now()
    
    current_time = now.strftime("%H:%M:%S")
    the_date = today.strftime("%d/%m/%Y")
    the_time = now.strftime("%H:%M")
    
    if alarm_date != the_date:
        if alarm_time != the_time:
            break
    print(the_time)
    sleep(0.9)
    
playsound("C:\\James\\Python\\Projects\\Soundboard\\Sounds\\foghorn.mp3")
