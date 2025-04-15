def solution(lottos, win_nums):
    answer = []
    cnt = 0
    zero_cnt = 0
    for ele in lottos:
        if ele == 0:
            zero_cnt += 1
        elif ele in win_nums:
            cnt += 1
    tmp = 1 if cnt + zero_cnt == 0 else cnt + zero_cnt
    cnt = 1 if cnt == 0 else cnt
    answer = sorted([7- cnt, 7 - tmp])
    return answer