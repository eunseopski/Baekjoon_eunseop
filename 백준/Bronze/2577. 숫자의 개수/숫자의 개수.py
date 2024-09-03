import sys
input = sys.stdin.readline

A = int(input())
B = int(input())
C = int(input())

mul = A * B * C
_list = []
for a in str(mul):
    _list.append(int(a))

for i in range(10):
    print(_list.count(i))