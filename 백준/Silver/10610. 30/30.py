n = input()
n = sorted(n, reverse= True)
num = 0

if '0' not in n:
    print(-1)
else:
    for e in n:
        num += int(e)
    if num % 3 != 0:
        print(-1)
    else:
        print(''.join(n))