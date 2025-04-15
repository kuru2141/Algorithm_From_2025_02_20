def solution(arr):
    answer = [arr[0]]
    for e in arr[1:]:
        if e != answer[-1]:
            answer.append(e)
    return answer