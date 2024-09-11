import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
queue = deque([])

for _ in range(N):
    S = input().rstrip()

    if len(S.split()) == 2:
        queue.append(int(S.split()[1]))

    if S == "pop":
        if queue:
            print(queue.popleft())
        else:
            print(-1)

    if S == "size":
        print(len(queue))

    if S == "empty":
        if queue:
            print(0)
        else:
            print(1)

    if S == "front":
        if queue:
            print(queue[0])
        else:
            print(-1)

    if S == "back":
        if queue:
            print(queue[-1])
        else:
            print(-1)