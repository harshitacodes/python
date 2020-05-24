t = int(input())
for i in range(t):
    n = int(input())
    a = 0
    b = 0
    c = 1
    while b <= n:
        b = b + c
        c = c + 1
    r = c - 2
    print(r)