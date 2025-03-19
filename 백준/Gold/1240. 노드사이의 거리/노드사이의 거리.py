import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

def dfs(x, y, r):
    if x == y:
        result_arr.append(r)
    for ele in dic[x]:
        if not visited[ele]:
            visited[ele] = 1
            dfs(ele, y, r + distance[x][ele])

N, M = map(int, input().split())
dic = dict()
distance = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

for _ in range(N - 1):
    x, y, d = map(int, input().split())
    if x not in dic:
        dic[x] = [y]
    else:
        dic[x].append(y)
    if y not in dic:
        dic[y] = [x]
    else:
        dic[y].append(x)
    distance[x][y] = d
    distance[y][x] = d

for _ in range(M):
    a, b = map(int, input().split())
    result_arr = []
    visited = [0 for _ in range(N + 1)]
    visited[a] = 1
    
    dfs(a, b, 0)

    print(min(result_arr))