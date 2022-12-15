S = list(input())
st = ['(']
cnt = 0
for i in range(1, len(S)):
    if S[i] == ')':
        if S[i-1] == '(':
            if not st: continue
            else:
                st.pop()
                cnt += len(st)
        else:
            st.pop()
            cnt += 1
    else: 
        st.append('(')
print(cnt)