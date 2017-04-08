import  os


while True:
    fname = input("pls input file name\n")
    if os.path.exists(fname):
        print("ERROR")
    else:
        break

print("input lines '.' to finish\n")

all = []

while True:
    entry = input('> ')
    if entry.endswith('.'):
        break
    else:
        all.append(entry)

f = open(fname,'w')
f.writelines([x for x in all])

f.close()
