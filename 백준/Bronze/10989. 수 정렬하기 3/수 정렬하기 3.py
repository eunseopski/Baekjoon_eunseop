import sys
input = sys.stdin.readline

N = int(input())

coeff = [0] * 10001

for _ in range(N):
    n = int(input())
    coeff[n] += 1

for i in range(1, len(coeff)):
    while coeff[i]:
        print(i)
        coeff[i] -= 1

