import sys
from collections import deque
dq = deque()
for _ in range(int(sys.stdin.readline())):
    order = sys.stdin.readline().split()
    o = order[0]
    if o == 'push_back':
        dq.append(order[1])

    elif o == 'push_front':
        dq.appendleft(order[1])

    elif o == 'pop_front':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq.popleft())

    elif o == 'pop_back':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq.pop())

    elif o == 'size':
        print(len(dq))

    elif o == 'empty':
        print(int(len(dq)==0))

    elif o == 'front':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[0])
            
    elif o == 'back':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[-1])