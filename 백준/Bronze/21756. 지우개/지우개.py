N = int(input())

arr = [i + 1 for i in range(N)]

while len(arr) != 1:
    tmp_arr = []
    for i in range(len(arr)):
        if i % 2 == 1:
            tmp_arr.append(arr[i])
    arr = tmp_arr

print(arr[0])