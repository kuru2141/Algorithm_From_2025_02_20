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

def propagation(start, end, i):
    tree[i] += (end - start + 1) * lazy[i]
    
    if start != end:
        lazy[i * 2] += lazy[i]
        lazy[i * 2 + 1] += lazy[i]
        
    lazy[i] = 0

def search(start, end, left, right, i = 1):
    propagation(start, end, i)

    if left > end or right < start:
        return 0

    if left <= start and right >= end:
        return tree[i]

    mid = (start + end) // 2
    return search(start, mid, left, right, i * 2) + search(mid + 1, end, left, right, i * 2 + 1)

def update(start, end, left, right, val, i = 1):
    propagation(start, end, i)

    if left > end or right < start:
        return

    if left <= start and right >= end:
        tree[i] += (end - start + 1) * val
        if start != end:
            lazy[i * 2] += val
            lazy[i * 2 + 1] += val
        return
    
    mid = (start + end) // 2
    update(start, mid, left, right, val, i * 2)
    update(mid + 1, end, left, right, val, i * 2 + 1)

    tree[i] = tree[i * 2] + tree[i * 2 + 1]

N, M, K = map(int, input().split())
nums = [int(input()) for _ in range(N)]

tree_len = 2 ** (math.ceil(math.log(N, 2)) + 1)
tree = [0] * tree_len
lazy = [0] * tree_len

segment(0, N - 1)

for _ in range(M + K):
    tmp = list(map(int, input().split()))

    if tmp[0] == 1:
        b, c, d = tmp[1:]
        update(0, N - 1, b - 1, c - 1, d)
    else:
        b, c = tmp[1:]
        print(search(0, N - 1, b - 1, c - 1))