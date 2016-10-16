from collections import  deque
def search(lines,pattern,history=5):
    previous_lines = deque(maxlen=history)
    for li in lines:
        if pattern in li:
            yield li,previous_lines
        previous_lines(li)

nines = "fsdf" \
        "sfd" \
        "sfd" \
        "sf"

for i in search(nines,'s'):
    print i
