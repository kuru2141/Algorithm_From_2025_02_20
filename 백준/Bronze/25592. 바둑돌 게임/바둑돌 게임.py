N = int(input())

cnt = 0

while True:
    cnt += 1
    N -= cnt
    
    if cnt % 2 == 0 and N < 0:
        print(0)
        break
    elif cnt % 2 == 1 and N < 0:
        print(-N)
        break