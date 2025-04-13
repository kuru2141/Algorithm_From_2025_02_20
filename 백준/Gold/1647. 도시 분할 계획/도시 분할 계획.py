import sys
input = sys.stdin.readline

def find(x):
    if x == parent[x]:
        return x

    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    xRoot = find(x)
    yRoot = find(y)

    if xRoot != yRoot:
        parent[yRoot] = xRoot

N, M = map(int, input().split())
parent = [e for e in range(N + 1)]
arr = [tuple(map(int, input().split())) for _ in range(M)]
arr.sort(key = lambda x: x[2])

result = 0
for a, b, c in arr:
    if find(a) != find(b):
        union(a, b)
        result += c
        max_result = c
        
print(result - max_result)