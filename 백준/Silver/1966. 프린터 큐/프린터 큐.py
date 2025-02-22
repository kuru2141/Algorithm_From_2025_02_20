from collections import deque

def find_idx(queue, arr_ipt):
    global M
    
    cnt = 0
    while queue:
        for ele in arr_ipt:
            while True:
                a, b = queue.popleft()

                if b != ele:
                    queue.append((a, b))
                else:
                    cnt += 1
                    if a == M:
                        return cnt
                    break

tmp = int(input())

for _ in range(tmp):
    queue = deque()
    
    N, M = map(int, input().split())
    # N개의 문서가 있으며, index가 M인 문서의 인쇄 순서를 출력해야 함
    arr = list(map(int, input().split()))

    arr_ipt = arr.copy()
    arr_ipt.sort(reverse = True)
    # 중요도를 내림차순으로 정리
    
    for i in range(N):
        queue.append((i, arr[i]))

    print(find_idx(queue, arr_ipt))