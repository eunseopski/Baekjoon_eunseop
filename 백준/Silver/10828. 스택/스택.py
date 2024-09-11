import sys
input = sys.stdin.readline

N = int(input())
stack = []

for _ in range(N):
    S = input().rstrip()

    if len(S.split()) == 2:
        stack.append(S.split()[1])

    if S == "pop":
        if stack:
            print(stack.pop())
        else:
            print(-1)

    if S == "size":
        print(len(stack))

    if S == "empty":
        if stack:
            print(0)
        else:
            print(1)

    if S == "top":
        if stack:
            print(stack[-1])
        else:
            print(-1)