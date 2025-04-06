import sys
input = sys.stdin.readline

def combi(depth):
    if len(numbers) == M:
        for ele in numbers:
            print(ele, end = ' ')
        print()
        return

    if depth > len(arr) - 1:
        return

    numbers.append(arr[depth])
    combi(depth)

    numbers.remove(arr[depth])
    combi(depth + 1)
    
N, M = map(int, input().split())
arr = sorted(list(set(map(int, input().split()))))

numbers = []
combi(0)