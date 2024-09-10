import sys
input = sys.stdin.readline

N = int(input())

names = [[] for _ in range(201)]

for i in range(N):
    y, n = input().rstrip().split()
    names[int(y)].append(n)

for i in range(len(names)):
    if names[i]:
        for A in names[i]:
            print(i, A)
