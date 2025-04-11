import sys
import math
input = sys.stdin.readline

def segment(left, right, i = 1):
    if left == right:
        tree[i] = nums[left]
        return tree[i]

    mid = (left + right) // 2
    tree[i] = min(segment(left, mid, i * 2), segment(mid + 1, right, i * 2 + 1))
    return tree[i]

def search(start, end, left, right, i = 1):
    if left > end or right < start:
        return float('inf')

    if left <= start and right >= end:
        return tree[i]

    mid = (start + end) // 2
    return min(search(start, mid, left, right, i * 2), search(mid + 1, end, left, right, i * 2 + 1))

def update(start, end, idx, val, i = 1):
    if idx < start or idx > end:
        return

    if start != end:
        mid = (start + end) // 2
        update(start, mid, idx, val, i * 2)
        update(mid + 1, end, idx, val, i * 2 + 1)
        tree[i] = min(tree[i * 2], tree[i * 2 + 1])
    else:
        tree[i] = val

N = int(input())
nums = list(map(int, input().split()))
tree = [0] * (2 ** (math.ceil(math.log(N, 2)) + 1))

segment(0, N - 1)


M = int(input())
for _ in range(M):
    a, b, c = map(int, input().split())
    
    if a == 1:
        update(0, N - 1, b - 1, c)
    else:
        print(search(0, N - 1, b - 1, c - 1))