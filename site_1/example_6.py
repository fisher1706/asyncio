import threading, random

counter = 0
re_mutex = threading.RLock()

def step_one():
    global counter
    re_mutex.acquire()
    counter = random.randint(1, 100)
    print("Random number %s" % counter)
    re_mutex.release()

def step_two():
    global counter
    re_mutex.acquire()
    counter *= 2
    print("Doubled = %s" % counter)
    re_mutex.release()

def walkthrough():
    re_mutex.acquire()
    try:
        step_one()
        step_two()
    finally:
        re_mutex.release()

t1 = threading.Thread(target=walkthrough)
t2 = threading.Thread(target=walkthrough)

t1.start()
t2.start()

t1.join()
t2.join()