import time

text = "Ahoj jak se mas"
print("Type this:", text)
input("Press Enter to start...")
start = time.time()
typed = input("Start typing: ")
print(f"Time: {time.time() - start:.2f}s") if typed == text else print("Try again!")
