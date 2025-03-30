from itertools import combinations

N, M = map(int, input().split())

arr = [i for i in range(1, N + 1)]

for ele in combinations(arr, M):
    for e in ele:
        print(e, end = ' ')
    print()