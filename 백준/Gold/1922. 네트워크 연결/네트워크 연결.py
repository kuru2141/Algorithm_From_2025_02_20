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

N = int(input())
M = int(input())

parent = [e for e in range(N + 1)]

arr = [tuple(map(int, input().split())) for _ in range(M)]
arr.sort(key = lambda x: x[2])

result = 0
for a, b, c in arr:
    if find(a) != find(b):
        union(a, b)
        result += c

print(result)