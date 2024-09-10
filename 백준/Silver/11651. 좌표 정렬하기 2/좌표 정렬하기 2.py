import sys
input = sys.stdin.readline

N = int(input())
list_ = []

for _ in range(N):
    x, y = map(int,input().split())
    list_.append((x,y))

for X, Y in sorted(list_, key=lambda x: (x[1], x[0])):
    print(X, Y)