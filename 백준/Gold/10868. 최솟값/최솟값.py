import math
import sys
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

N, M = map(int, input().split())
nums = [int(input()) for _ in range(N)]
tree = [0] * (2 ** (math.ceil(math.log(N, 2)) + 1))

segment(0, N - 1)

for _ in range(M):
    a, b = map(int, input().split())
    print(search(0, N - 1, a - 1, b - 1))