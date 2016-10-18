def smaple():
    yield "IS"
    yield "Chicago"
    yield "Not"
    yield "Chicago"


for i in smaple():
    print(i)
    

print('--'.join(smaple()))