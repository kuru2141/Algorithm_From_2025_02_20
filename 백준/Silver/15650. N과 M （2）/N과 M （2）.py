def combi(depth, M):
    if len(numbers) == M:
        for ele in numbers:
            print(ele, end = ' ')
        print()
        return
    
    if depth > N - 1:
        return
        
    numbers.append(arr[depth])
    combi(depth + 1, M)
    numbers.remove(arr[depth])
    combi(depth + 1, M)

N, M = map(int, input().split())
arr = [(i + 1) for i in range(N)]

numbers = []
combi(0, M)
