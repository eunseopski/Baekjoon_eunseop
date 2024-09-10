import sys
input = sys.stdin.readline

N = int(input())
result = 0
five = N // 5


for i in range(five, -1, -1):
    # 5로 나누어지는 경우
    if N - i * 5 == 0:

        print(i)
        exit()
    # 5로 나누어지지 않는 경우
    elif (N - i * 5) % 3 == 0:
        # 3으로 나누어지면
        print(i + (N - i * 5) // 3)
        exit()

print(-1)