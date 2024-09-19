import sys
input = sys.stdin.readline

T = int(input())
zero_one = [(1, 0), (0, 1)] + [0] * 39

def zero_one_num(n):
    if n == 0:
        return zero_one[n]
    elif n == 1:
        return zero_one[n]
    elif zero_one[n]:
        zero_num1, one_num1 = zero_one[n - 2]
        zero_num2, one_num2 = zero_one[n - 1]
    else:
        zero_num1, one_num1 = zero_one_num(n - 2)
        zero_num2, one_num2 = zero_one_num(n - 1)

    zero_one[n] = zero_num1 + zero_num2, one_num1 + one_num2
    return zero_one[n]

for _ in range(T):
    N = int(input())
    print(*zero_one_num(N))

