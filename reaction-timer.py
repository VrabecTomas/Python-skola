import time, random

input("Press Enter to start...")
wait = random.uniform(2, 5)
time.sleep(wait)
start = time.time()
input("NOW! Press Enter!")
end = time.time()

reaction = round(end - start, 3)
print(f"Your reaction time: {reaction} seconds")