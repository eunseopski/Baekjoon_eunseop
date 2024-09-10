import sys
input = sys.stdin.readline


def compare(eight_list, list_, row_, column_): #바꿔야 하는 갯수 비교
    ans = 0
    for i in range(8):
        for j in range(8):
            if eight_list[i][j] != list_[i+row_][j+column_]:
                ans += 1

    return ans


N, M = map(int, input().split())

#입력 받기
M_N = []
for _ in range(N):
    row_M = list(input())
    M_N.append(row_M)

# 비교할 리스트 생성
start_W = [['B'] * 8 for _ in range(8)]
start_B = [['W'] * 8 for _ in range(8)]
for i in range(8):
    for j in range(8):
        # 시작
        if i % 2 == j % 2:
            start_W[i][j] = 'W'
            start_B[i][j] = 'B'

# 8x8의 0,0 좌표가 갈 수 있는 범위
row, column = N-8, M-8
ans_min = 64

for X in range(row+1):
    for Y in range(column+1):
        ans_B = compare(start_B, M_N, X, Y)
        ans_W = compare(start_W, M_N, X, Y)
        if ans_min > min(ans_B, ans_W):

            ans_min = min(ans_B, ans_W)
            # print(ans_min, X, Y, row, column)


print(ans_min)
