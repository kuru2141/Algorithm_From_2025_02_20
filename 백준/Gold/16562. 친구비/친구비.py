def make(N):
    parents = []

    for i in range(N + 1):
        parents.append(i)

    return parents

def find(V):
    if parents[V] == V:
        return V

    parents[V] = find(parents[V])
    return parents[V]

def union(a, b):
    aRoot = find(a)
    bRoot = find(b)
    if aRoot == bRoot:
        return False

    parents[aRoot] = bRoot
    return True

N, M, k = map(int, input().split())
money = list(map(int, input().split()))

parents = make(N)

for _ in range(M):
    a, b = map(int, input().split())
    union(a, b)

for i in range(N):
    find(i)

parents = parents[1:] # 0번째 친구 제거
dic = dict()

for i in range(len(parents)):
    ele = parents[i]
    if ele not in dic:
        dic[ele] = money[i]
    else:
        if dic[ele] > money[i]:
            dic[ele] = money[i]

sum_dict = 0

for ele in dic:
    sum_dict += dic[ele]
print(sum_dict if sum_dict <= k else 'Oh no')