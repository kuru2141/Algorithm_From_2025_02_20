def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x

N = int(input())

for _ in range(N):
    a, b = map(int, input().split())

    gcd_ab = gcd(a, b)
    print(a * b // gcd_ab)