import sys
input = sys.stdin.readline
from collections import defaultdict

T = int(input())  # 테스트 케이스의 수

for _ in range(T):
    n = int(input())  # 의상의 수
    clothes = defaultdict(int)

    for _ in range(n):
        _, category = input().split()
        clothes[category] += 1

    result = 1
    for count in clothes.values():
        result *= (count + 1)  # 해당 종류의 의상을 입지 않는 경우 포함

    print(result - 1)  # 아무것도 입지 않는 경우 제외