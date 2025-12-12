import sys
input = sys.stdin.readline

N = int(input())
K = N
idx = 0

while True:
    if K < 10:
        K = K * 10 + K

    else:
        x = K % 10
        K = (x + K // 10) % 10 + x * 10

    idx += 1

    if K == N:
        break

print(idx)