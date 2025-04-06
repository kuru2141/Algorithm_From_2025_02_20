from itertools import permutations
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))

for ele in sorted(list(set(permutations(arr, M)))):
    for e in ele:
        print(e, end = ' ')
    print()