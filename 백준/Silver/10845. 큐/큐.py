import sys
from collections import deque
q = deque()
for _ in range(int(sys.stdin.readline())):
    order = sys.stdin.readline().split()
    o = order[0]
    if o == 'push':
        q.append(order[1])
    elif o == 'pop':
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())
    elif o == 'size':
        print(len(q))
    elif o == 'empty':
        print(int(len(q)==0))
    elif o == 'front':
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
    elif o == 'back':
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])