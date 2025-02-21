from collections import deque

N = int(input())

arr = [input() for _ in range(N)]
cnt = 0

for ele in arr:
    queue = deque()
    queue.appendleft(ele[0])
    
    for i in range(1, len(ele)):
        
        if not queue: # queue가 비어있다면
                queue.appendleft(ele[i])
        else:
            if ele[i] == queue[0]:
                queue.popleft()
            else:
                queue.appendleft(ele[i])
        
    if not queue:
        cnt += 1

print(cnt)