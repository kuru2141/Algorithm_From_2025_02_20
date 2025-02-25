class Edge:
    def __init__(self, from_e, to_e, weight):
        self.from_e = from_e
        self.to_e = to_e
        self.weight = weight

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

def union(a, b, weight):
    global total_weight
    
    aRoot = find(a)
    bRoot = find(b)

    if aRoot == bRoot:
        return False

    parents[aRoot] = bRoot
    total_weight += weight
    return True


N = int(input())
M = int(input())

edgeList = []
parents = make(N)
total_weight = 0

for _ in range(M):
    from_e, to_e, weight = map(int, input().split())
    edgeList.append(Edge(from_e, to_e, weight))

edgeList.sort(key = lambda x: x.weight)

for edge in edgeList:
    union(edge.from_e, edge.to_e, edge.weight)
    
print(total_weight)