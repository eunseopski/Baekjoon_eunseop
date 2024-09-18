import sys
input = sys.stdin.readline

N, M = map(int, input().split())

NH = set()
NS = set()

for _ in range(N):
    NH.add(input().rstrip())

for _ in range(M):
    NS.add(input().rstrip())

NHS = NH & NS
print(len(NHS))
NHS = sorted(NHS)
for a in NHS:
    print(a)