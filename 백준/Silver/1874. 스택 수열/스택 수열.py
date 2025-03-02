import sys
input = sys.stdin.readline

n = int(input())

arr = [int(input()) for _ in range(n)]
num_arr = [i for i in range(n, 0, -1)]

stack = []
tmp = 0

result = ''

for ele in arr:
    if ele > tmp:
        while num_arr:
            x = num_arr.pop()
            result += '+'
            if ele == x:
                result += '-'
                tmp = x
                break

            stack.append(x)

    else:
        x = stack.pop()
        result += '-'
        if ele != x:
            result = 'NO'
            break
        
if result == 'NO':
    print(result)
else:
    for ele in result:
        print(ele)