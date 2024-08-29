import sys
input = sys.stdin.readline

s = input().rstrip()
k = input().rstrip()

stack = []

for char in s:
    stack.append(char)
    if len(stack) >= len(k) and ''.join(stack[-len(k):]) == k:
        # 스택에서 폭발 문자열 길이만큼 제거
        del stack[-len(k):]

result = ''.join(stack)

if result:
    print(result)
else:
    print("FRULA")
