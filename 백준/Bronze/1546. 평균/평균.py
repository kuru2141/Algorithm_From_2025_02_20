import math

N = int(input())

arr = list(map(int, input().split()))
new_arr = []
M = max(arr)

for ele in arr:
    new_arr.append(ele / M * 100)


sum_value = 0
for ele in new_arr:
    sum_value += ele

print(sum_value / N)