def count_factorial_zeros(n):
    count = 0
    i = 5
    while i <= n:
        count += n // i
        i *= 5
    return count

N = int(input())
print(count_factorial_zeros(N))