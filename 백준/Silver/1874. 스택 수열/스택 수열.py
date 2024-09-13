import sys
input = sys.stdin.readline

n = int(input())
list_n = []

for _ in range(n):
    list_n.append(int(input()))
stack = []
i = 1
result = []

for N in list_n:
    while i <= N:
        stack.append(i)
        result.append("+")
        i += 1

    if stack and stack[-1] == N:
        stack.pop()
        result.append("-")
    else:
        print("NO")
        exit()

for a in result:
    print(a)