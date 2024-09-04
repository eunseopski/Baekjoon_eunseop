import sys
input = sys.stdin.readline

N = int(input())

size_ = list(map(int, input().split()))

T, P = map(int, input().split())

t = 0
for a in size_:
    if a == 0:
        t += 0
        continue
    t += (a-1) // T + 1

print(t)
print(*divmod(N, P))
