import sys
input = sys.stdin.readline

A, B = map(int,input().split())

i = 1
sero = []

while True:

    if A % i == 0 and B % i == 0:
        A //= i
        B //= i
        sero.append(i)
        i = 1

    if i == min(A, B):
        two = A*B
        break

    i += 1



one = 1
for a in sero:
    one *= a

print(one)
print(one * two)
