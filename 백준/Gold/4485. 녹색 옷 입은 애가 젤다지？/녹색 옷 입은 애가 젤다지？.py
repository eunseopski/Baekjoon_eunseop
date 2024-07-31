import sys
input = sys.stdin.readline
from heapq import heappop, heappush

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
j = 0

# dist를 2차원리스트로 만들고 각 칸에 무한대를 넣어준다.
while True:
    j += 1

    N = int(input())

    if not N:
        break

    adj = [list(map(int, input().split())) for _ in range(N)]

    dist = [[float('inf')] * (N) for _ in range(N)]

    heap = [(adj[0][0], 0, 0)]

    while heap:
        w, r, c = heappop(heap)

        if dist[r][c] != float('inf'):
            continue

        dist[r][c] = w

        # print(w, r, c)
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < N and 0 <= nc < N and dist[nr][nc] == float('inf'):
                heappush(heap, (w + adj[nr][nc], nr, nc))

    print(f'Problem {j}: {dist[N-1][N-1]}')