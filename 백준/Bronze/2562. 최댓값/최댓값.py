max_num = 0
max_index = 0

for i in range(1, 10):
    num = int(input())
    if num > max_num:
        max_num = num
        max_index = i

print(max_num)
print(max_index)