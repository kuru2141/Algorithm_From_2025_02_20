import sys
input = sys.stdin.readline

def choose(depth):
    if len(numbers) == M:
        for ele in numbers:
            print(ele, end = ' ')
        print()
        return

    if depth > N - 1:
        return
    
    if arr[depth] not in numbers:
        numbers.append(arr[depth])
        choose(0)
        numbers.remove(arr[depth])
        choose(depth + 1)
    else:
        choose(depth + 1)

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

for ele in arr:
    numbers = [ele]
    choose(0)