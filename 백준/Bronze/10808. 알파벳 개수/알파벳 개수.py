a = [0] * 26
for s in input():
    a[ord(s)-97] += 1
for s in a:
    print(s, end =' ')