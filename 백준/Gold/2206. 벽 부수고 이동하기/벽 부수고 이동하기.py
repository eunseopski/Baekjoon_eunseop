import sys
sys.setrecursionlimit(10**9)
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

maze = [[int(x) for x in input().rstrip()] for _ in range(N)]

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

# r, c cnt, 벽 파괴 기회
stack = deque([(0, 0, 1, 1)])
visited = {(0, 0, 1)}

while stack:
    r, c, cnt, chance = stack.popleft()

    if (r, c) == (N-1, M-1):
        print(cnt)
        exit()

    # 탐색
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < N and 0 <= nc < M and (nr, nc, chance) not in visited:

            # 0이면 다음 방문지에 추가
            if not maze[nr][nc]:
                stack.append((nr, nc, cnt + 1, chance))
                visited.add((nr, nc, chance))

            # 1이면서 벽 파괴 기회가 있다면 한 번 부숨
            if maze[nr][nc] and chance:
                stack.append((nr, nc, cnt + 1, chance - 1))
                visited.add((nr, nc, chance - 1))


print(-1)


