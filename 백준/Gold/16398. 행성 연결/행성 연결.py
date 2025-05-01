import sys
input = sys.stdin.readline

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    xRoot = find(x)
    yRoot = find(y)

    if xRoot <= yRoot:
        parent[yRoot] = xRoot
    else:
        parent[xRoot] = yRoot

N = int(input())
parent = [i for i in range(N)]
c_arr = [list(map(int, input().split())) for _ in range(N)]

arr = []
for i in range(N):
    for j in range(N):
        c = c_arr[i][j]
        if i < j:
            arr.append((i, j, c))
arr.sort(key = lambda x: x[2])

result = 0

for a, b, c in arr:
    aRoot = find(a)
    bRoot = find(b)

    if aRoot != bRoot:
        union(a, b)
        result += c

print(result)