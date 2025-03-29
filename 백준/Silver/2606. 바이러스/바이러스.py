import sys
input = sys.stdin.readline

def dfs(x):
    global result

    if x not in dic:
        return
    
    for ele in dic[x]:
        if not visited[ele]:
            visited[ele] = 1
            result += 1
            dfs(ele)


N = int(input())
dic = dict()

for _ in range(int(input())):
    a, b = map(int, input().split())
    if a not in dic:
        dic[a] = [b]
    else:
        dic[a].append(b)
    if b not in dic:
        dic[b] = [a]
    else:
        dic[b].append(a)

visited = [0] * (N + 1)
visited[1] = 1

result = 0
dfs(1)

print(result)