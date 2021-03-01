import threading
import random; random.seed(0)
import time

def update(pause_period):
    global counter

    with count_lock:
        current_counter = counter
        time.sleep(pause_period)
        counter = current_counter + 1

pause_periods = [random.randint(0,1) for i in range(20)]

counter = 0
count_lock = threading.Lock()
threads = [threading.Thread(target=update, args=(pause_periods[i],)) for i in range(20)]
start = time.perf_counter()

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print('--Concurrent version--')
print(f'Final counter: {counter}.')
print(f'Took {time.perf_counter() - start : .2f} seconds.')
print('Finished.')
