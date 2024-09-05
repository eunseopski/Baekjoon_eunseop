import sys
input = sys.stdin.readline

L = int(input())
S = input().rstrip()

S_ = {chr(key) : value for key, value in zip(range(ord("a"), ord("z")+1), range(1, 27))}

H = 0
for i in range(L):
    H += S_[S[i]] * (31**i)

H %= 1234567891
print(H)