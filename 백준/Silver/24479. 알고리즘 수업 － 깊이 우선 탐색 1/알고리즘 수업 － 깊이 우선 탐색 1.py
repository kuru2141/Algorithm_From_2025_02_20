import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

def dfs(x):
    global idx

    if x not in dic:
        return
    
    for ele in dic[x]:
        if not visited[ele]:
            visited[ele] = idx
            idx += 1
            dfs(ele)

N, M, R = map(int, input().split())
dic = dict()
visited = [0] * (N + 1)
visited[R] = 1

for _ in range(M):
    u, v = map(int, input().split())
    if u not in dic:
        dic[u] = [v]
    else:
        dic[u].append(v)
    if v not in dic:
        dic[v] = [u]
    else:
        dic[v].append(u)

for li in dic:
    dic[li].sort()

idx = 2
dfs(R)

for i in range(1, len(visited)):
    print(visited[i])