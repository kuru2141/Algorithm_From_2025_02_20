import sys
input = sys.stdin.readline

T = int(input())

result = []

for _ in range(T):
    result.append(sum(list(map(int, input().split()))))

for ele in result:
    print(ele)