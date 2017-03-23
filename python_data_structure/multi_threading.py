import threading
import time


def dewraps(f):
    def wrap(f,*args,**kwargs):
        start = time.time()
        f(args,kwargs)
        end = time.time()
        print("Cost Time:",end-start)
    return wrap



def haha(max_num):
    for i in range(max_num):
        time.sleep(1)
        print(i)


for x in range(3):
        t = threading.Thread(target=haha,args=(5,))
        t.setDaemon(False)

        t.start()
        t.join()

