
N = int(input())

a = [0, 1, 2, 4] + [0] * 7

def A(n):

    if a[n]:
        return a[n]
    else:
        a[n] = A(n-1) + A(n-2) + A(n-3)
        return a[n]

for _ in range(N):
    I = int(input())
    print(A(I))
    

    
