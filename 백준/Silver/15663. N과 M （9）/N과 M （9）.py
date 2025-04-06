import sys
input = sys.stdin.readline

def combi(depth):    
    if len(numbers) == M:
        result.add(tuple(numbers))
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            numbers.append(arr[i])
            combi(depth + 1)
            visited[i] = 0
            numbers.pop()

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

result = set()
visited = [0] * N
numbers = []

combi(0)

for ele in sorted(result):
    for e in ele:
        print(e, end = ' ')
    print()
