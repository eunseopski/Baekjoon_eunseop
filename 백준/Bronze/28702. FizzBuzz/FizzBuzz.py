import sys
input = sys.stdin.readline

one = input().rstrip()
two = input().rstrip()
three = input().rstrip()

if str.isdigit(one):
    result = int(one) + 3

if str.isdigit(two):
    result = int(two) + 2

if str.isdigit(three):
    result = int(three) + 1

if result % 3 == 0:
    if result % 5 == 0:
        print("FizzBuzz")
        exit()
    else:
        print("Fizz")
        exit()
else:
    if result % 5 == 0:
        print("Buzz")
        exit()

print(str(result))