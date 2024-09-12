import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    level = list(map(int, input().split()))
    i = 0
    m = M

    while level:
        max_level = max(level)
        left = level.pop(0)

        if max_level == left:
            i += 1
            if m == 0:
                print(i)
                break
        else:
            level.append(left)
            if m == 0:
                m = len(level)
        m -= 1
