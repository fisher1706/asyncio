from threading import Thread

class MyThread(Thread):
    def __init__(self, num):
        super().__init__(name="threddy_" + num)
        self.num = num
    def run(self):
        print("Thread ", self.num)


thread1 = MyThread("1")
thread2 = MyThread("2")

thread1.start()
print(thread1.ident)
print(thread1.getName())

thread2.start()
print(thread2.ident)
print(thread2.getName())


thread1.join()
thread2.join()

