n = int(input())
A = list(map(int, input().split()))
increase = [1] * n
decrease = [1] * n
for i in range(1, n):
    for j in range(i):
        if A[i] > A[j]:
            increase[i] = max(increase[i], increase[j]+1)
A.reverse()
for i in range(1,n):
    for j in range(i):
        if A[i] > A[j]:
            decrease[i] = max(decrease[i], decrease[j]+1)

res = [0] * n
for i in range(n):
    res[i] = increase[i] + decrease[n-i-1] - 1
print(max(res))