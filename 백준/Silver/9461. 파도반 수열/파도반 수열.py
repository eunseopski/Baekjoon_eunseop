import sys
input = sys.stdin.readline

def come_on_result(n):
    
    if n <= 3:
        return 1
    elif nums[n] == 0:
        nums[n] = come_on_result(n-2) + come_on_result(n-3)
        return nums[n]
    else:
        return nums[n]


T = int(input())

nums = [0] * 101

nums[1] = 1
nums[2] = 1
nums[3] = 1

for t in range(T):
    N = int(input())

    print(come_on_result(N))
    
    
    
