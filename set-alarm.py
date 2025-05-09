import time

alarm = input("Set alarm (HH:MM): ")

while True:
    now = time.strftime("%H:%M")
    if now == alarm: 
        print("⏰ Alarm! Wake up!")
        break
    time.sleep(10)