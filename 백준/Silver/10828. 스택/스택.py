import sys
st = []
for _ in range(int(sys.stdin.readline())):
    order = sys.stdin.readline().split()
    o = order[0]
    if o == 'push':
        st.append(order[1])
    elif o == 'pop':
        if len(st) == 0:
            print(-1)
        else:
            print(st.pop())
    elif o == 'size':
        print(len(st))
    elif o == 'empty':
        print(int(len(st)==0))
    elif o == 'top':
        if len(st) == 0:
            print(-1)
        else:
            print(st[-1])