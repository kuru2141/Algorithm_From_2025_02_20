import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

N = int(input())
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)

for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(v):
    for ele in graph[v]:
        if not visited[ele]:
            visited[ele] = v
            dfs(ele)

dfs(1)

for i in range(2, len(visited)):
    print(visited[i])
