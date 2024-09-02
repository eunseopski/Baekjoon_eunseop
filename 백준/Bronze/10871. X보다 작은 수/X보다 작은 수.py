N, X = map(int, input().split())
L = list(map(int, input().split()))
for a in L:
    if a < X:
        print(a, end=" ")