import sys
input = sys.stdin.readline

#find 함수
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

#union 함수
def union(a, b):
    a_root, b_root = find(a), find(b)

    if rank[a_root] < rank[b_root]:
        parent[b_root] = a_root
    elif rank[b_root] < rank[a_root]:
        parent[a_root] = b_root
    else:
        parent[b_root] = a_root
        rank[a_root] += 1


N, M = map(int, input().split())

edges = []
for _ in range(M):
    s, e, c = map(int, input().split())
    edges.append((c, s, e))
edges.sort()
# 이 길 중에서, 작은 순대로 뽑을거임.
# 그럼 비용이 최소가 되면서 모든 친구들이 이어지겠지.
# 그리고 마지막 놈들 없애면? 겜 끝

parent = [i for i in range(N+1)]
rank = [0]*(N+1)
wei = 0
cnt = 0
last = 0

# 간선을 차례대로 확인하면서
for w, x, y in edges:
    # a랑 b랑 이어져있는지 확인
    if find(x) == find(y):
        # 이어져 있으면 다른거
        continue
    #안이어져있으면 잇고 가중치추가, 길+1
    union(x, y)
    wei += w
    cnt += 1
    last = w

print(wei-last)
