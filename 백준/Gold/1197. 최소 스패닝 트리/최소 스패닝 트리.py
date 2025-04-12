import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

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

V, E = map(int, input().split())
parent = [e for e in range(V + 1)]
arr = [tuple(map(int, input().split())) for _ in range(E)]
arr.sort(key = lambda x: x[2])

cnt = 0
for a, b, c in arr:
    if find(a) != find(b):
        union(a, b)
        cnt += c
        
print(cnt)