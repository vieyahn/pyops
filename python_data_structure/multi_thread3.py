import threading
def do(event):
    print("start")
    event.wait()
    print("finish")

eve_obj = threading.Event()

for i in range(10):
    t  = threading.Thread(target=do,args=(eve_obj,))
    t.start()

eve_obj.clear()
inp = input("Input:")
if inp == 'true':
    eve_obj.set()
