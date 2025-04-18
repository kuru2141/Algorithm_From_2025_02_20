import math
import sys
input = sys.stdin.readline

def segment(left, right, i = 1):
    if left == right:
        tree[i] = nums[left]
        return tree[i]

    mid = (left + right) // 2
    tree[i] = segment(left, mid, i * 2) ^ segment(mid + 1, right, i * 2 + 1)
    return tree[i]

def propagation(start, end, i = 1):
    tree[i] ^= lazy[i]

    if start != end:
        lazy[i * 2] ^= lazy[i]
        lazy[i * 2 + 1] ^= lazy[i]

    lazy[i] = 0

def search(start, end, idx, i = 1):
    propagation(start, end, i)
    
    if idx > end or idx < start:
        return 0

    if start != end:
        mid = (start + end) // 2
        return search(start, mid, idx, i * 2) ^ search(mid + 1, end, idx, i * 2 + 1)
    else:
        return tree[i]

def update(start, end, left, right, val, i = 1):
    propagation(start, end, i)
    
    if left > end or right < start:
        return

    if left <= start and right >= end:
        tree[i] ^= val

        if start != end:
            lazy[i * 2] ^= val
            lazy[i * 2 + 1] ^= val
 
        return

    mid = (start + end) // 2
    update(start, mid, left, right, val, i * 2)
    update(mid + 1, end, left, right, val, i * 2 + 1)

    tree[i] = tree[i * 2] ^ tree[i * 2 + 1]

n = int(input())
nums = list(map(int, input().split()))

tree_len = 2 ** (math.ceil(math.log(n, 2)) + 1)
tree = [0] * tree_len
lazy = [0] * tree_len

segment(0, n - 1)

for _ in range(int(input())):
    tmp = list(map(int, input().split()))
    if tmp[0] == 1:
        a, b, c = tmp[1:]
        update(0, n - 1, a, b, c)
    else:
        a = tmp[1]
        print(search(0, n - 1, a))