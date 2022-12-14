import sys
for _ in range(int(sys.stdin.readline())):
    st = []
    lst = list(sys.stdin.readline().strip())
    if lst[0] == ')':
        print('NO')
        continue
    flag = True
    for ele in lst:
        if ele == '(':
            st.append(ele)
        else:
            if len(st) != 0:
                st.pop()
            else:
                flag = False
                break
    if flag and len(st)==0:
        print('YES')
    else:
        print('NO')