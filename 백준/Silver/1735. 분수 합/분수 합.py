def gcd(x, y):
    while x % y:
        x, y = y, x % y
    return y

a, b = map(int, input().split())
c, d = map(int, input().split())

a *= d
c *= b

x = a + c
y = b * d

gcd_val = gcd(x, y)

x //= gcd_val
y //= gcd_val

print(x, y)