import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

N = int(input())

graph = [[] for _ in range(N)]
visited = [0] * N
input_arr = list(map(int, input().split()))

for i in range(N):
    if input_arr[i] != -1:
        graph[input_arr[i]].append(i)
    else:
        root = i

k = int(input())
result = 0

def dfs(v, past_v):
    global k, result
    
    if v == k:
        if len(graph[past_v]) == 1:
            result += 1
        return

    if not graph[v]:
        result += 1
    else:
        for ele in graph[v]:
            if not visited[ele]:
                visited[ele] = v
                dfs(ele, v)

dfs(root, -1)
print(result)
