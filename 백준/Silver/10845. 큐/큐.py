import sys
input = sys.stdin.readline

def do(x, queue):
    
    if x[0] == 'push':
        queue.append(int(x[1]))
    
    elif x[0] == 'pop':
        if not len(queue):
            print(-1)
        else:
            print(queue[0])
            queue = queue[1:]

    elif x[0] == 'size':
        print(len(queue))

    elif x[0] == 'empty':
        if queue:
            print(0)
        else:
            print(1)

    elif x[0] == 'front':
        if not len(queue):
            print(-1)
        else:
            print(queue[0])

    elif x[0] == 'back':
        if not len(queue):
            print(-1)
        else:
            print(queue[-1])

    return queue

N = int(input())
queue = []

for _ in range(N):
    tmp = list(input().split())
    
    queue = do(tmp, queue)