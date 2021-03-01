import threading

def writer():
    global text
    global wcount

    while True:
        with wcounter:
            wcount += 1
            if wcount == 1:
                read_try.acquire()

        with resourece:
            print(f'Writing being done by {threading.current_thread().name}.')
            text += f'Writing was done by {threading.current_thread().name}.'

        with wcounter:
            wcount -= 1
            if wcount == 0:
                read_try.release()

def reader():
    global rcount

    while True:
        with read_try:
            with rcounter:
                rcount += 1
                if rcount == 1:
                    resourece.acquire()

            print(f'Reading being done by {threading.current_thread().name}:')
            print(text)

        with rcounter:
            rcount -= 1
            if rcount == 0:
                resourece.release()

text = 'This is some text.'
rcount = 0
wcount = 0

wcounter = threading.Lock()
rcounter = threading.Lock()
resourece = threading.Lock()
read_try = threading.Lock()

threads = [threading.Thread(target=reader) for i in range(3)] + [threading.Thread(target=writer) for i in range(2)]

for thread in threads:
    thread.start()