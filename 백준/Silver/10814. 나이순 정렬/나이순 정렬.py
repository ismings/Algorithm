l = []
for _ in range(int(input())):
    l.append(input().split())
for a, n in sorted(l, key= lambda x: int(x[0])):
    print(a, n)