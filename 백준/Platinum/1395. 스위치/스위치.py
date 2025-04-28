import sys
input = sys.stdin.readline

def propagation(start, end, i):
    tmp = lazy[i] % 2
    if tmp:
        tree[i] = (end - start + 1) - tree[i]

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

def update(start, end, left, right, i = 1):
    propagation(start, end, i)

    if left > end or right < start:
        return

    if left <= start and right >= end:
        tree[i] = (end - start + 1) - tree[i]

        if start != end:
            lazy[i * 2] += 1
            lazy[i * 2 + 1] += 1
        return

    mid = (start + end) // 2
    update(start, mid, left, right, i * 2)
    update(mid + 1, end, left, right, i * 2 + 1)

    tree[i] = tree[i * 2] + tree[i * 2 + 1]

N, M = map(int, input().split())
tree_len = N * 4
tree = [0] * tree_len
lazy = [0] * tree_len

nums = [0] * N

for _ in range(M):
    a, b, c = map(int, input().split())

    if not a:
        update(0, N - 1, b - 1, c - 1)
    else:
        print(search(0, N - 1, b - 1, c - 1))