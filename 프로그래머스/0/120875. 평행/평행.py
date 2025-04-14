def solution(dots):    
    a = (dots[0][1] - dots[1][1]) / (dots[0][0] - dots[1][0]) # 0 - 1
    b = (dots[2][1] - dots[3][1]) / (dots[2][0] - dots[3][0]) # 2 - 3

    c = (dots[0][1] - dots[2][1]) / (dots[0][0] - dots[2][0]) # 0 - 2
    d = (dots[1][1] - dots[3][1]) / (dots[1][0] - dots[3][0]) # 1 - 3
    
    e = (dots[0][1] - dots[3][1]) / (dots[0][0] - dots[3][0]) # 0 - 3
    f = (dots[1][1] - dots[2][1]) / (dots[1][0] - dots[2][0]) # 1 - 2

    if a == b or c == d or e == f:
        return 1
    return 0