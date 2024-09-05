while True:
    N = input().rstrip()

    if N == '0':
        exit()

    if N == N[::-1]:
        print("yes")
    else:
        print("no")
