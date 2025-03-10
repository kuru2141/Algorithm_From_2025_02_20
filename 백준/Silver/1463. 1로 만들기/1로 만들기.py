from collections import deque

N = int(input())
queue = deque()

queue.append((N, 0))

cnt = []

while queue:
    n, c = queue.popleft()
    if n == 1:
        cnt.append(c)
        break
    
    if n % 3 == 0:
        queue.append((n // 3, c + 1))
    if n % 2 == 0:
        queue.append((n // 2, c + 1))
    queue.append((n - 1, c + 1))    

print(min(cnt))
