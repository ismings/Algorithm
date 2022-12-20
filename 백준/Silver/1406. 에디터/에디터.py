import sys
input = sys.stdin.readline
st_l = list(input().strip())
st_r = []
for i in range(int(input())):
    command = input().split()
    if command[0] == 'L' and st_l:
        st_r.append(st_l.pop())
    elif command[0] == 'D' and st_r:
        st_l.append(st_r.pop())
    elif command[0] == 'B' and st_l:
        st_l.pop()
    elif command[0] == 'P':
        st_l.append(command[1])
st_l = st_l + st_r[::-1]
print(''.join(st_l))