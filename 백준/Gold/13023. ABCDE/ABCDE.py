import sys
input = sys.stdin.readline

def dfs(ele, visited, cnt):
    global check
    
    if cnt == 5:
        check = 1
        return

    if ele in dic.keys():
        for e in dic[ele]:
            if not visited[e]:
                visited[e] = 1
                dfs(e, visited, cnt + 1)
                visited[e] = 0
                
    
def checkTree(dic):
    global check
    
    for ele in dic.keys():
        check = 0
        visited = [0] * N
        visited[ele] = 1
        dfs(ele, visited, 1)

        if check == 1:
            return 1
    return 0

N, M = map(int, input().split())
dic = dict()

check = 0

for _ in range(M):
    a, b = map(int, input().split())
    if a not in dic.keys():
        dic[a] = [b]
    else:
        dic[a].append(b)

    if b not in dic.keys():
        dic[b] = [a]
    else:
        dic[b].append(a)

print(checkTree(dic))