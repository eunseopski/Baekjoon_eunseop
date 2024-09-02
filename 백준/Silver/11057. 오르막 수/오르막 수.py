import sys
input = sys.stdin.readline

N = int(input())

save_num = [[1 for i in range(10)]]
save_num.extend([[0]*10 for i in range(N)])

for i in range(1, N+1):
    for j in range(10):
        save_num[i][j] = sum(save_num[i-1][j:])


# print(save_num)
print(save_num[N][0] % 10007)
