N, M = map(int, input().split())
t = 0

while M != 0:
    if N % M == 0:
        break
    elif M % N == 0:
        t += M - N
        break
    else:
        N %= M
        t += N
        M -= N

print(t)
