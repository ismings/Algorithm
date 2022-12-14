a = [-1] * 26
s = input()
for i in range(len(s)):
    if a[ord(s[i])-97] == -1:
     a[ord(s[i])-97] = i
for s in a:
    print(s, end =' ')