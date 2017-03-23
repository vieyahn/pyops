import  threading
import time

class haha(threading.Thread):
    def __init__(self,max_num):
        threading.Thread.__init__(self)
        self.max_num = max_num
    def run(self):
        for i in range(self.max_num):
            time.sleep(1)
            print(i)
if __name__ == '__main__':
    threads = []
    for x in range(3):
        t = haha(5)
        threads.append(t)
    for thr in threads:
        thr.start()
    for thr in threads:
        if thr.isAlive():
            thr.join()
