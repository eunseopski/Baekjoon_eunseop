import sys
input = sys.stdin.readline

N, K = map(int, input().split())
n = N
n_result, k_result = 1, 1

while n != N-K:
    n_result *= n
    n -= 1

k = 1
while K:
    k_result *= K
    K -= 1

print(n_result // k_result)



