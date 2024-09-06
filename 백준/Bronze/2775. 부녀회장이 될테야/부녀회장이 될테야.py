import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())

    num = [[x for x in range(1, n+1)]]
    num.extend([[0]*n for _ in range(k)])

    for K in range(1, k+1):
        num[K][0] = 1

    for K in range(1, k+1):
        for N in range(1, n):
            num[K][N] = num[K-1][N] + num[K][N-1]

    print(num[k][n-1])
