import sys
input = sys.stdin.readline

N = int(input())
n = 1
num = 666
while True:

    if '666' in str(num):
        if n == N:
            print(num)
            exit()

        n += 1
    num += 1