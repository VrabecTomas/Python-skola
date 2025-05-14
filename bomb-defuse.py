import time, threading

code, defused = "1234", False

def timer():
    for i in range(10, 0, -1):
        if defused: return
        print(f"{i}...", end='\r')
        time.sleep(1)
    if not defused: print("\n💥 Boom!")

threading.Thread(target=timer).start()
if input("Code: ") == code:
    defused = True
    print("✅ Defused!")