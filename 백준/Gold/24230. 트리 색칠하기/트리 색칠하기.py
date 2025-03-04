import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

N = int(input())
color = [0] + list(map(int, input().split()))
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
visited[1] = 1

for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(v):
    global cnt

    for ele in graph[v]:
        if not visited[ele]:
            visited[ele] = 1
            if color[ele] != color[v]:
                cnt += 1
            dfs(ele)

if not color[1]:
    cnt = 0
else:
    cnt = 1
dfs(1)

print(cnt)
