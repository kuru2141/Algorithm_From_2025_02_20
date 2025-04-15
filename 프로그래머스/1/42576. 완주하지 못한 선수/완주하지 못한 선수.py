def solution(participant, completion):
    dic = dict()
    for ele in participant:
        if ele not in dic:
            dic[ele] = 1
        else:
            dic[ele] += 1
        
    for ele in completion:
        dic[ele] -= 1
    
    for ele in dic.keys():
        if dic[ele]:
            return ele
        
        
    
    