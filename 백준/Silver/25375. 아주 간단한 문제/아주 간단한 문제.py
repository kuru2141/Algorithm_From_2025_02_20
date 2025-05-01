import sys, math
input = sys.stdin.readline

Q = int(input())

for _ in range(Q):
    a, b = map(int, input().split())

    if b // a == b / a and b > a:
        print(1)
    else:
        print(0)