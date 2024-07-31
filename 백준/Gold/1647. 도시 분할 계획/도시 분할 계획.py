import sys
input = sys.stdin.readline
#
#
# def find(x): # 재귀를 이용해서 경로압축하기.
#     if parent[x] != x:
#         parent[x] = find(parent[x])
#     return parent[x]
#
#     # union 연산
# rank = [0] * 5
# def union(x, y): # 루트끼리 합치기
#     x_root, y_root = find(x), find(y)
#     if rank[x_root] > rank[y_root]:
#         parent[y_root] = x_root
#     elif rank[x_root] < rank[y_root]:
#         parent[x_root] = y_root
#     else: #임의로 일단 갖다붙힘
#         parent[x_root] = y_root
#         rank[y_root] += 1
#
# # N: 집의 개수, M: 길의 개수
# N, M = map(int, input().split())
#
# # 크루스칼 풀이
# # 마지막 간선이 남은 간선들 중 제일 비용이 클 것이다.
# # 마지막 간선만 없애면 마을을 2개로 나누면서
# # 다른 마을들이 최소 비용으로 이어지게 할 수 있다.
#
# edges = []
# for _ in range(M):
#     a, b, w = map(int, input().split())
#     # 가중치를 앞으로 보내면 정렬하기가 좀 더 편함
#     edges.append((w, a, b))
#
# #크루스칼을 위한 가중치 정렬
# edges.sort()
# # 0번 인덱스는 사용하지 않을 것임
# parent = [i for i in range(N+1)]
# # 마찬가지로 0번은 안 씀
# rank = [0] * (N+1)
# # 간선 몇 개 뽑았는지 세기 위함
# cnt = 0
# # 가중치 계산할 놈
# ans = 0
#
#
# #간선에서 하나씩 뽑으면서 확인
# for w, a, b in edges:
#     # 같은 집합인지 확인
#     if find(a) == find(b):
#         continue
#
#     # 아니라면 합쳐주기
#     union(a, b)
#     # 간선 갯수 세고
#     cnt += 1
#     # 가중치 더해주기
#     ans += w
#
#     if cnt == N-2:
#         break
#
# print(ans)

from heapq import heappop, heappush

V, E = map(int, input().split())

adj = [[] for _ in range(V+1)]

for _ in range(E):
    s, e, w = map(int, input().split())
    adj[s].append((w, e))
    adj[e].append((w, s))

#세팅: 방문예정지, 방문기록지, 출발지
heap = []
heappush(heap, (0, 1))

# dist는 거리가 들어가는 배열 0번 인덱스느 사용안함.
# 거리의 최솟값을 넣을거임. visited 처럼 쓰임.
dist = [float('inf')] * (V + 1)
dist[0] = 0 # 0번은 안쓸거니까

# #visited로 해당 정점 타고 들어간 간선 가중치
# visited = []

while heap:
    # 방문
    w, cur = heappop(heap)

    # 한 번 다녀갔던 곳인지 확인, 사이클 방지
    if dist[cur] != float('inf'):
        continue

    #갱신,
    dist[cur] = w

    # 탐색
    # 다음 이동할 곳 뭐뭐 있는지 확인
    for nxt_w, nxt_cur in adj[cur]:
        # 방문 했던 곳인지 확인
        if dist[nxt_cur] == float('inf'):
            # 방문예정지에 추가
            heappush(heap, (nxt_w, nxt_cur))

print(sum(dist) - max(dist))

