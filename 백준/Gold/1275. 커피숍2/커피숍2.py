import math
import sys
input = sys.stdin.readline

def segment(left, right, i = 1):
    if left == right:
        tree[i] = nums[left]
        return tree[i]

    mid = (left + right) // 2
    tree[i] = segment(left, mid, i * 2) + segment(mid + 1, right, i * 2 + 1)
    return tree[i]

def search(start, end, left, right, i = 1):
    if left > end or right < start:
        return 0

    if left <= start and right >= end:
        return tree[i]

    mid = (start + end) // 2
    return search(start, mid, left, right, i * 2) + search(mid + 1, end, left, right, i * 2 + 1)

def update(start, end, idx, val, i = 1):
    if idx < start or idx > end:
        return

    tree[i] += val

    if start != end:
        mid = (start + end) // 2
        update(start, mid, idx, val, i * 2)
        update(mid + 1, end, idx, val, i * 2 + 1)

N, Q = map(int, input().split())
nums = list(map(int, input().split()))
tree = [0] * (2 ** (math.ceil(math.log(N, 2)) + 1))

segment(0, N - 1)

for _ in range(Q):
    x, y, a, b = map(int, input().split())
    if x <= y:
        print(search(0, N - 1, x - 1, y - 1))
    else:
        print(search(0, N - 1, y - 1, x - 1))

    update(0, N - 1, a - 1, b - nums[a - 1])
    nums[a - 1] = b