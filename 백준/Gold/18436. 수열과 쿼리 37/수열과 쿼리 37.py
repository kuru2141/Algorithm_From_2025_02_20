import math
import sys
input = sys.stdin.readline

def segment(left, right, i = 1):
    if left == right:
        tree[i] = (1, 0) if nums[left] % 2 == 0 else (0, 1)
        return tree[i]

    mid = (left + right) // 2
    x1, y1 = segment(left, mid, i * 2)
    x2, y2 = segment(mid + 1, right, i * 2 + 1)
    tree[i] = (x1 + x2, y1 + y2)
    return tree[i]

def search(start, end, left, right, i = 1):
    if left > end or right < start:
        return (0, 0)

    if left <= start and right >= end:
        return tree[i]

    mid = (start + end) // 2
    x1, y1 = search(start, mid, left, right, i * 2)
    x2, y2 = search(mid + 1, end, left, right, i * 2 + 1)
    return (x1 + x2, y1 + y2)

def update(start, end, idx, val, i = 1):
    if idx < start or idx > end:
        return

    if start != end:
        mid = (start + end) // 2
        update(start, mid, idx, val, i * 2)
        update(mid + 1, end, idx, val, i * 2 + 1)

        x1, y1 = tree[i * 2]
        x2, y2 = tree[i * 2 + 1]
        tree[i] = (x1 + x2, y1 + y2)
    else:
        tree[i] = (1, 0) if val % 2 == 0 else (0, 1)
    

N = int(input())
nums = list(map(int, input().split()))
tree = [0] * (2 ** (math.ceil(math.log(N, 2)) + 1))

segment(0, N - 1)

M = int(input())
for _ in range(M):
    a, b, c = map(int, input().split())

    if a == 1:
        update(0, N - 1, b - 1, c)
    elif a == 2:
        print(search(0, N - 1, b - 1, c - 1)[0])
    else:
        print(search(0, N - 1, b - 1, c - 1)[1])