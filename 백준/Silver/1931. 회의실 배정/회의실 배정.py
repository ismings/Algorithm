n = int(input())
classes = [list(map(int, input().split())) for _ in range(n)]
classes.sort(key=lambda x: (x[1],x[0]))

end = 0
res = 0
for s,e in classes:
    if s >= end:
        res += 1
        end = e
print(res)