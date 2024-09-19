import sys
input = sys.stdin.readline

N = int(input())
i_list = sorted(list(map(int, input().split())))
len_i_list = len(i_list)
result = 0

for a in i_list:
    result += a * len_i_list
    len_i_list -= 1

print(result)