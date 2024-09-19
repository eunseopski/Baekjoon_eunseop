import sys
input = sys.stdin.readline
from collections import deque

X = int(input())
queue = deque([(X, 0)])
visited = {X}

while queue:
    cur, cnt = queue.popleft()

    if cur == 1:
        print(cnt)
        exit()

    cur_123 = []
    if cur % 3 == 0:
        cur_123.append(cur // 3)
    if cur % 2 == 0:
        cur_123.append(cur // 2)
    cur_123.append(cur - 1)

    for c in cur_123:
        if c not in visited:
            visited.add(c)
            queue.append((c, cnt+1))

