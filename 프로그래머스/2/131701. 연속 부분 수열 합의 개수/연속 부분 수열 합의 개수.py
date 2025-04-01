def solution(elements):
    arr = elements * 2

    result = []

    for i in range(len(elements)):
        for j in range(1, len(elements) + 1):
            result.append(sum(arr[i:i + j]))
            
    return len(set(result))