from collections import deque
import sys
input = sys.stdin.readline

N, d, k, c = map(int, input().split())
dic = dict()
dic[c] = 1

arr = deque([int(input()) for _ in range(N)])
queue = deque()
for _ in range(k):
    x = arr.popleft()
    queue.append(x)
    arr.append(x)
    
    if x in dic:
        dic[x] += 1
    else:
        dic[x] = 1

result = len(dic)

for _ in range(N):
    x = arr.popleft()
    queue.append(x)
    
    if x in dic:
        dic[x] += 1
    else:
        dic[x] = 1

    if len(queue) == k + 1:
        y = queue.popleft()

        if dic[y] == 1:
            del(dic[y])
        else:
            dic[y] -= 1
            
    result = max(result, len(dic))

print(result)