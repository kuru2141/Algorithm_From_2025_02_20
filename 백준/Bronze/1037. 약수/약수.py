def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x

N  = int(input())

arr = list(map(int, input().split()))

max_arr = max(arr)

lcm_tmp = arr[0]

for i in range(1, len(arr)):
    tmp = lcm_tmp
    gcd_tmp = gcd(tmp, arr[i])
    lcm_tmp = tmp * arr[i] // gcd_tmp

if lcm_tmp in arr:
    print(lcm_tmp * min(arr))
else:
    print(lcm_tmp)