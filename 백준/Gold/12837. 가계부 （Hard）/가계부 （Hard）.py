import math
import sys
input = sys.stdin.readline

def search(start, end, left, right, i = 1):
    if left > end or right < start:
        return 0

    if left <= start and right >= end:
        return tree[i]

    mid = (start + end) // 2
    return search(start, mid, left, right, i * 2) + search(mid + 1, end, left, right, i * 2  + 1)

def update(start, end, idx, val, i = 1):
    if idx < start or idx > end:
        return

    tree[i] += val

    if start != end:
        mid = (start + end) // 2
        update(start, mid, idx, val, i * 2)
        update(mid + 1, end, idx, val, i * 2 + 1)

N, Q = map(int, input().split())
nums = [0] * (N + 1)
tree = [0] * (2 ** (math.ceil(math.log(N, 2)) + 1))

for _ in range(Q):
    n, p, q = map(int, input().split())

    if n == 1:
        update(0, N - 1, p - 1, q)
    else:
        print(search(0, N - 1, p - 1, q - 1))