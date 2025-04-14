import sys
input = sys.stdin.readline

def find(x):
    if parent[x] == x:
        return x

    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    xRoot = find(x)
    yRoot = find(y)

    if xRoot != yRoot:
        parent[yRoot] = xRoot

while True:
    m, n = map(int, input().split())

    if not m and not n:
        break

    arr = [tuple(map(int, input().split())) for _ in range(n)]
    parent = [e for e in range(m)]

    arr.sort(key = lambda x: x[2])

    sum_c = 0
    for ele in arr:
        sum_c += ele[2]

    result = 0
    for a, b, c in arr:
        if find(a) != find(b):
            union(a, b)
            result += c
            
    print(sum_c - result)