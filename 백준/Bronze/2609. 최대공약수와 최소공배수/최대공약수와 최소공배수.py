a, b = map(int,input().split())
def GCD(a, b):
    while b:
        a, b = b, a%b
    return a
print(GCD(a,b))

def LCM(a, b):
    return (a*b) // GCD(a,b)
print(LCM(a,b))