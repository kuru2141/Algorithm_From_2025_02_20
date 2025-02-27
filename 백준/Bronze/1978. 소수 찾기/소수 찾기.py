import math

N = int(input())
arr = list(map(int, input().split()))
cnt = 0

for ele in arr:
    if ele == 1:
        continue

    is_prime = True
    for i in range(2, int(math.sqrt(ele) + 1)):
        j = i
        while i * j <= ele:
            if ele % i == 0:
                is_prime = False
                break
            j += 1
    if is_prime:    
        cnt += 1

print(cnt)