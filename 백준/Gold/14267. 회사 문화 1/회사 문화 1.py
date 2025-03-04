import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

def dfs(i):
    for ele in graph[i]:
        if not visited[ele]:
            ching_chan[ele] += ching_chan[i]
            visited[ele] = 1
            dfs(ele)

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

arr = list(map(int, input().split()))
for i in range(1, n):
    graph[arr[i]].append(i + 1)

ching_chan = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    ching_chan[a] += b
    
visited = [0] * (n + 1)
dfs(1)

for i in range(1, len(ching_chan)):
    print(ching_chan[i], end = ' ')