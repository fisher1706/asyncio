import threading

print('Waiting...')

def timer_test():
    print("The timer has done its job!")


tim = threading.Timer(5, timer_test)
tim.start()