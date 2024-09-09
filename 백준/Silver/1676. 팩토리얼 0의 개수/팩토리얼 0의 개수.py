import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def fact(num):

    if num <= 1:
        return 1
    else:
        return num * fact(num-1)

def check_index(s):
    for i in range(-1, -len(s)-1, -1):
        if s[i] != '0':
            return -(i+1)


N = int(input())

print(check_index(str(fact(N))))
