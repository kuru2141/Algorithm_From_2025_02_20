T = int(input())

# a가 중복되면 안된다는 조건이 없기 때문에 항상 가능 
for _ in range(T):
    A, B = map(int, input().split())
    print('yes')
