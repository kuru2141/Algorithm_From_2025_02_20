def check_valid(arr):
    a, b = ord(arr[0][0]) - ord('A') + 1, int(arr[0][1])
    
    for i in range(1, len(arr)):
        x, y = a, b
        a, b = ord(arr[i][0]) - ord('A') + 1, int(arr[i][1])
        
        if ((abs(x - a) == 2) and (abs(y - b) == 1)) or ((abs(x - a) == 1) and (abs(y - b) == 2)):
            continue
        else:
            return 0

    return 1

arr = []
for i in range(36):
    arr.append(input())
arr.append(arr[0])


if len(set(arr)) != 36:
    print('Invalid')
else:
    if check_valid(arr):
        print('Valid')
    else:
        print('Invalid')