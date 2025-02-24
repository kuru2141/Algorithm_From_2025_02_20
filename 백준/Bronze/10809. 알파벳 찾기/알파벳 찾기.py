S = input()

arr = [-1] * 26

for i in range(len(S)):
    tmp = ord(S[i]) - ord('a')

    if arr[tmp] != -1:
        arr[tmp] = min(i, arr[tmp])
    else:
        arr[tmp] = i

for ele in arr:
    print(ele, end = ' ')