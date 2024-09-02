N = int(input())

if N % 4 == 0:
    if N % 100 == 0:
        if N % 400 == 0:
            print(1)
            exit()
        print(0)
        exit()
    print(1)
    exit()

print(0)
    



# 1. 4의 배수여야함
# 2. 근데 100의 배수는 안됨
# 3. 근데 400의 배수는 됨