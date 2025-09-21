import sys
input = sys.stdin.readline

N = int(input())
arr = []

for _ in range(N):
    command = list(map(str, input().split()))

    if command[0] == 'push':
        arr.append(int(command[1]))
    elif command[0] == 'top':
        if not arr:
            print(-1)
        else:
            print(arr[-1])
    elif command[0] == 'size':
        print(len(arr))
    elif command[0] == 'empty':
        if not arr:
            print(1)
        else:
            print(0)
    elif command[0] == 'pop':
        if not arr:
            print(-1)
        else:
            print(arr.pop())
    else:
        print(-1)