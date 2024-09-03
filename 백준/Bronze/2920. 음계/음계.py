import sys
input = sys.stdin.readline

num_list = list(map(int, input().split()))

result = num_list[0]
con = set()

for a in num_list[1:]:
    result -= a
    if result > 0:
        con.add(0)
    else:
        con.add(1)
    result = a

if len(con) == 2:
    print("mixed")
elif 1 in con:
    print("ascending")
else:
    print("descending")