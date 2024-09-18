import sys
input = sys.stdin.readline

N, K = map(int, input().split())

values = []
for i in range(N):
    values.append(int(input()))

result = 0
result_list = []
for i in range(-1, -len(values)-1, -1):

    Q, R = divmod(K, values[i])

    if not Q:
        continue

    result += Q
    K = R

print(result)
