import threading

def writer():
    global text

    while True:
        with service:
            resourece.acquire()

        print(f'Writing being done by {threading.current_thread().name}.')
        text += f'Writing was done by {threading.current_thread().name}.'

        resourece.release()

def reader():
    global rcount

    while True:
        with service:
            rcounter.acquire()
            rcount += 1
            if rcount == 1:
                resourece.acquire()
        rcounter.release()

        print(f'Reading being done by {threading.current_thread().name}:')
        # print(text)

        with rcounter:
            rcount -= 1
            if rcount == 0:
                resourece.release()

text = 'This is some text.'
rcount = 0

rcounter = threading.Lock()
resourece = threading.Lock()
service = threading.Lock()

threads = [threading.Thread(target=reader) for i in range(3)] + [threading.Thread(target=writer) for i in range(2)]

for thread in threads:
    thread.start()