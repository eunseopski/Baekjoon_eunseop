N = list(map(int, input().split()))

print(sum(list(map(lambda x: x**2, N)))%10)