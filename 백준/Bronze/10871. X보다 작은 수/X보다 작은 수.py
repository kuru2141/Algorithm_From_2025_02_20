N, X = map(int, input().split())

arr = list(map(int, input().split()))
for ele in arr:
    if ele < X:
        print(ele, end = ' ')