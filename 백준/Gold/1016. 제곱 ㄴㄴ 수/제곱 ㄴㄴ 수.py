import math

a, b = map(int, input().split())

# min_val부터 max_val까지 제곱ㄴㄴ수를 판별할 배열 (True로 초기화)
find_sq = [True] * (b - a + 1)

for i in range(2, int(math.sqrt(b)) + 1):
    sq = i * i

    # a 이상인 첫 번째 square의 배수 찾기
    start = ((a + sq - 1) // sq) * sq

    # 제곱수의 배수를 False로 설정
    for j in range(start, b + 1, sq):
        find_sq[j - a] = False

# 제곱ㄴㄴ수의 개수를 반환 (True로 남은 수를 셈)
print(sum(find_sq))
