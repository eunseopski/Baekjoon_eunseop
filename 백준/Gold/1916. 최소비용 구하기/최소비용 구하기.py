import sys
input = sys.stdin.readline
from heapq import heappop, heappush

N = int(input())
M = int(input())

adj = [[] for _ in range(N+1)]

for _ in range(M):
    s, e, w = map(int, input().split())
    adj[s].append((w, e))


S, E = map(int,input().split())
# 세팅(방문예정지, 방문기록지, 출발지)
dist = [float('inf')] * (N+1)
# 출발지 지정
heap = [(0, S)]

while heap:
    # 방문
    wei, cur = heappop(heap)

    if dist[cur] != float('inf'):
        continue

    #최초 방문일시 방문
    dist[cur] = wei

    # 탐색
    for n_wei, nxt in adj[cur]:
        if dist[nxt] == float('inf'):
            heappush(heap, (wei + n_wei, nxt))

print(dist[E])


