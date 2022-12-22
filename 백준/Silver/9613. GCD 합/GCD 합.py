def GCD(a, b):
    while b:
        a, b = b, a%b
    return a

for _ in range(int(input())):
    res = 0
    A = list(map(int, input().split()))
    for i in range(1, A[0]+1):
        for j in range(i+1, A[0]+1):
            res += GCD(A[i], A[j])
    print(res)