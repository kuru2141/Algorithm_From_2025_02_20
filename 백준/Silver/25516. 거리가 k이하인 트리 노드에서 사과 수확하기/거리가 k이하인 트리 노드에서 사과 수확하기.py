import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

def dfs(v, cnt):
    global sum_apple

    visited[v] = 1
    
    if cnt <= k and arr[v]:
        sum_apple += 1
    
    for ele in graph[v]:
        if not visited[ele]:
            dfs(ele, cnt + 1)

n, k = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)

arr = list(map(int, input().split()))
visited = [0] * (n + 1)
sum_apple = 0

dfs(0, 0)

    
print(sum_apple)