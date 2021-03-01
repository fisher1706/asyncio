import threading

protected_resource = 0
unprotected_resource = 0

NUM = 500
mutex = threading.Lock()

def safe_plus():
    global protected_resource
    for i in range(NUM):
        mutex.acquire()
        protected_resource += 1
        mutex.release()

def safe_minus():
    global protected_resource
    for i in range(NUM):
        mutex.acquire()
        protected_resource -= 1
        mutex.release()

def risky_plus():
    global unprotected_resource
    for i in range(NUM):
        unprotected_resource += 1

def risky_minus():
    global unprotected_resource
    for i in range(NUM):
        unprotected_resource -= 1

thread1 = threading.Thread(target = safe_plus)
thread2 = threading.Thread(target = safe_minus)
thread3 = threading.Thread(target = risky_plus)
thread4 = threading.Thread(target = risky_minus)

thread1.start()
thread2.start()
thread3.start()
thread4.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()

print("Результат при работе с блокировкой %s" % protected_resource)
print("Результат без блокировки %s" % unprotected_resource)
