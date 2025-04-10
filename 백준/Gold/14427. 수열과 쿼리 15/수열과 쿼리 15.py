import math
import sys
input = sys.stdin.readline

def segment(left, right, i = 1):
    if left == right:
        tree[i] = (nums[left], left)
        return tree[i]

    mid = (left + right) // 2
    a = segment(left, mid, i * 2)
    b = segment(mid + 1, right, i * 2 + 1)
    tree[i] = a if a[0] <= b[0] else b
    return tree[i]

def update(start, end, idx, val, i = 1):
    if idx < start or idx > end:
        return

    
    if start != end:
        mid = (start + end) // 2
        update(start, mid, idx, val, i * 2)
        update(mid + 1, end, idx, val, i * 2 + 1)
        tree[i] = min(tree[i * 2], tree[i * 2 + 1])
    else:
        tree[i] = (val, idx)
        

N = int(input())
nums = list(map(int, input().split()))
tree = [0] * (2 ** (math.ceil(math.log(N, 2)) + 1))
segment(0, N - 1)

M = int(input())
for _ in range(M):
    tmp = list(map(int, input().split()))
    if tmp[0] == 1:
        update(0, N - 1, tmp[1] - 1, tmp[2])
    else:
        print(tree[1][1] + 1)