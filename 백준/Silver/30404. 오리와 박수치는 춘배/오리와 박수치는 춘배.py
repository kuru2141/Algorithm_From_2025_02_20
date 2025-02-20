from collections import deque

N, K = map(int, input().split())

arr = list(map(int, input().split()))

queue = deque(arr)

count = 0

while queue:
    x = queue.popleft() + K
    while queue:
        tmp = queue.popleft()
        if tmp > x:
            queue.appendleft(tmp)
            break
    count += 1
    
print(count)