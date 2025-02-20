N = int(input())

arr_mat = []
arr_list = []

def combi(depth, start):
    if depth == R:
        arr_list.append(numbers[:])
        return
    for i in range(start, N):
        numbers[depth] = arr_mat[i]
        combi(depth + 1, i + 1)

for _ in range(N):
    arr_mat.append(list(map(int, input().split())))

for R in range(1, N + 1):
    numbers = [0] * R
    combi(0, 0)

min_value = 999999

for arr in arr_list:
    S = 1
    B = 0

    for ele in arr:
        S *= ele[0]
        B += ele[1]
        
    tmp = abs(S - B)

    if tmp < min_value:
        min_value = tmp
        
print(min_value)