import sys
input = sys.stdin.readline

N = int(input())

n_list = [0]*2000001

for _ in range(N):
    n_list[int(input())+1000000] += 1

for i in range(len(n_list)):
    if n_list[i]:
        print(i-1000000)
