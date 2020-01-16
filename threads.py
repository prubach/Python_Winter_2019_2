from threading import Thread
import time

class myThread(Thread):
    def __init__(self, threadId, name, counter, delay, shared_list):
        Thread.__init__(self)
        self.threadId = threadId
        self.name = name
        self.counter = counter
        self.delay = delay
    def run(self):
        print('Starting: ' + self.name)
        while self.counter:
            time.sleep(self.delay)
            print('%s: %s' % (self.name, time.ctime(time.time())))
            self.shared_list.append(self.name + '_' + str(self.counter))
            self.counter-=1
        print('Exiting: ' + self.name)

shared_list = []
thread1 = myThread(1, "Thread 1", 5, 1, shared_list)
thread2 = myThread(2, "Thread 2", 4, 2, shared_list)
thread1.start()
thread2.start()
print('Exiting main thread')