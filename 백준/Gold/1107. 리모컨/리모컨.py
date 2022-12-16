target = int(input())
n = int(input())
if n > 0:
    broken = list(map(int, input().split()))
    cnt = abs(100 - target)

    for num in range(1000001):
        num = str(num)
        for i in range(len(num)):
            if int(num[i]) in broken:
                break
            elif i == len(num)-1:
                cnt = min(cnt, abs(int(num)-target)+len(num))
    print(cnt)
else:
    print(min(len(str(target)), abs(100 - target)))