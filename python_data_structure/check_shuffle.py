import numpy as np
import  random
def check(s1,s2):
    alist = list(s2)

    pos1 = 0

    stillOK = True

    while pos1<len(s1) and stillOK:

        pos2 = 0

        found = False

        while pos2<len(s2) and not found:
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 += 1

        if found:
            alist[pos2] = None
        else:
            stillOK = False

        pos1 += 1

    return stillOK



s = "fsdkgjfkdg"
mid = list(s)


random.shuffle(mid)




print(check("vance","ancev"))