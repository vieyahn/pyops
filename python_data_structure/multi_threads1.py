import threading
import time
def haha(x):
    for i in range(x):
        time.sleep(1)
        print(i)

threads = []
for i in range(3):
    t = threading.Thread(target=haha,args=(5,))
    threads.append(t)

for thr in threads:
    thr.start()
    
for thr in threads:
    if thr.isAlive():
        thr.join()

