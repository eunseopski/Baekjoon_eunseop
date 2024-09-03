import sys
input = sys.stdin.readline

for i in range(int(input())):
    H, W, N = map(int, input().split())

    floor = N % H
    ho = N // H + 1
    if floor == 0:
        floor = H
        ho -= 1
    ho = str(ho)
    if int(ho) < 10:
        ho = '0' + ho
    print(str(floor) + ho)

