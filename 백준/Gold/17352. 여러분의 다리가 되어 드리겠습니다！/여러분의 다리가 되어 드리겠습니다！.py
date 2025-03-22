import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

def dfs(v):
    if v not in dic:
        return
    
    for ele in dic[v]:
        if not visited[ele]:
            visited[ele] = 1
            dfs(ele)

N = int(input())
dic = dict()
visited = [0] * (N + 1)

if N == 2:
    print(1, 2)
else:
    for _ in range(N - 2):
        x, y = map(int, input().split())
        if x not in dic:
            dic[x] = [y]
        else:
            dic[x].append(y)
        if y not in dic:
            dic[y] = [x]
        else:
            dic[y].append(x)

    v = list(dic.keys())[0]
    visited[v] = 1

    dfs(v)

    for i in range(1, len(visited)):
        if not visited[i]:
            if v != i:
                print(v, i)
            break