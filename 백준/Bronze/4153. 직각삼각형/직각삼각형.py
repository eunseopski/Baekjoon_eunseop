import sys
input = sys.stdin.readline

while True:
    nums = list(map(int,input().split()))
    flag = False

    if sum(nums) == 0:
        exit()
    for i in range(3):
        if nums[0]**2 + nums[1] **2 == nums[2]**2:
            print("right")
            flag = True
            break
        nums.append(nums.pop(0))

    if not flag:
        print("wrong")