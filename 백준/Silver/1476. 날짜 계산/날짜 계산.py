E, S, M = map(int, input().split())
e, s, m = 1, 1, 1
year = 1
while True:
    if e == E and s == S and m == M:
        print(year)
        break
    e += 1
    s += 1
    m += 1
    if e > 15:
        e -= 15
    if s > 28:
        s -= 28
    if m > 19:
        m -= 19
    year += 1