import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

n, k = map(int, input().split())
graph = [[] for _ in range(n)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)

arr = list(map(int, input().split()))
for i in range(len(arr)):
    if arr[i] == k:
        tmp = i

visited = [0] * (n)
result = 0

def dfs(v, cnt):
    global k, result
    
    if v == tmp:
        result = cnt
        return
    
    for ele in graph[v]:
        if not visited[ele]:
            visited[ele] = v
            dfs(ele, cnt + 1)

dfs(0, 0)

print(result)
