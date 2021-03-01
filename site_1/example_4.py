from datetime import datetime
import threading

def factorial(number):
    fact = 1
    for n in range(1, number + 1):
        fact *= n
    return fact

number = 100000
thread_1 = threading.Thread(target=factorial, args=(number,))
thread_2 = threading.Thread(target=factorial, args=(number,))

startTime = datetime.now()

thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()

endTime = datetime.now()
print("Время выполнения: ", endTime - startTime)

