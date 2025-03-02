import sys
input = sys.stdin.readline

def do(x, stack):
    
    if x[0] == 'push':
        stack.append(int(x[1]))
    
    elif x[0] == 'pop':
        if not stack:
            print(-1)
        else:
            print(stack[-1])
            stack = stack[:-1]

    elif x[0] == 'size':
        print(len(stack))

    elif x[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)

    elif x[0] == 'top':
        if not stack:
            print(-1)
        else:
            print(stack[-1])

    return stack

N = int(input())
stack = []

for _ in range(N):
    tmp = list(input().split())
    
    stack = do(tmp, stack)