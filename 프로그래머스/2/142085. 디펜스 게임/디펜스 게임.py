import heapq
from collections import deque

def solution(n, k, enemy):
    cnt = 0
    lst = []
    new_lst = []

    new_enemy = deque(enemy)

    cnt = 0

    while new_enemy:
        x = new_enemy.popleft()
        
        if len(lst) < k:
            heapq.heappush(lst, x)
        else:
            tmp = heapq.heappop(lst)
            
            if n >= min(tmp, x):
                if tmp > x:
                    n -= x
                    heapq.heappush(lst, tmp)
                else:
                    n -= tmp
                    heapq.heappush(lst, x)
                cnt += 1
            else:
                break
            
    return min(len(lst) + cnt + 1, len(enemy))