import sys
input = sys.stdin.readline

N = int(input())
score = []
for _ in range(N):
    score.append(int(input()))
score = sorted(score)
result = 0

if N == 0:
    print(0)
    exit()

N_rest = N * 15 / 100
# print(N_rest)
_, mod = divmod(N_rest, 1)
if mod >= 0.5:
    N_rest += 1

N_rest = int(N_rest)
if N_rest:
    score = score[N_rest:-N_rest]
    result = sum(score) / len(score)
else:
    result = score[0]

_, mod = divmod(result, 1)
if mod >= 0.5:
    result += 1

print(int(result))