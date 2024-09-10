import sys
input = sys.stdin.readline

N = int(input())

N_list = [0] * 20000001

N_ = list(map(int, input().split()))

for a in N_:
    N_list[a] += 1

M = int(input())

M_list = list(map(int, input().split()))

for i in M_list:
    print(N_list[i], end=" ")