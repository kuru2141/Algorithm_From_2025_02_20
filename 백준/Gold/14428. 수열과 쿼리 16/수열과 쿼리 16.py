import math
import sys
input = sys.stdin.readline

def segment(left, right, i = 1):
    if left == right:
        tree[i] = (nums[left], left)
        node_index[left] = i
        return tree[i]

    mid = (left + right) // 2
    
    x = segment(left, mid, i * 2)
    y = segment(mid + 1, right, i * 2 + 1)
    
    tree[i] = x if x[0] <= y[0] else y
    return tree[i]

def search(start, end, left, right, i = 1):
    if left > end or right < start:
        return (float('inf'), len(tree) - 1)

    if left <= start and right >= end:
        return tree[i]

    mid = (start + end) // 2

    x = search(start, mid, left, right, i * 2)
    y = search(mid + 1, end, left, right, i * 2 + 1)
    
    return x if x[0] <= y[0] else y

def update(start, end, idx, val, prev_val, i = 1):
    global b
    
    if idx < start or idx > end:
        return

    if start != end:
        mid = (start + end) // 2
        update(start, mid, idx, val, prev_val, i * 2)
        update(mid + 1, end, idx, val, prev_val, i * 2 + 1)

        if tree[i][0] == prev_val:
            x =tree[i * 2]
            y = tree[i * 2 + 1]
            tree[i] = x if x[0] <= y[0] else y
        else:
            if val < tree[i][0]:
                tree[i] = (val, b - 1)
            elif val == tree[i][0]:
                if b - 1 < tree[i][1]:
                    tree[i] = (val, b - 1)

N = int(input())
nums = list(map(int, input().split()))
tree = [float('inf')] * (2 ** (math.ceil(math.log(N, 2)) + 1))
node_index = [0] * N

segment(0, N - 1)

for _ in range(int(input())):
    a, b, c = map(int, input().split())

    if a == 1:
        tree[node_index[b - 1]] = (c, b - 1)
        update(0, N - 1, b - 1, c, nums[b - 1])
        nums[b - 1] = c
    else:
        if b > c:
            b, c = c, b
        print(search(0, N - 1, b - 1, c - 1)[1] + 1)