def GCD(a,b):
    while b:
        a,b = b,a%b
    return a

def LCM(a,b):
    return (a*b)//GCD(a,b)

#최소공배수
for _ in range(int(input())):
    a, b = map(int,input().split())
    print(LCM(a,b))