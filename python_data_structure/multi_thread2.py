import threading
import time

gnum = 0


def work(max_num):
    global gnum
    gnum += 2
    time.sleep(1)

def my_lock():
    global gnum
    work(10)
    gnum += 1
    print("gum is ",gnum)

threads = []

for x in range(5):

    t = threading.Thread(target=my_lock)
    threads.append(t)

for it in threads:
    it.start()


