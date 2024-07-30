import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

#union을 이렇게 짜는 이유가 뭘까?? 졸아서 모르겠네
def union(x, y): # 루트끼리 합치기
    x_root, y_root = find(x), find(y)

    if rank[x_root] > rank[y_root]:
        parent[y_root] = x_root

    elif rank[x_root] < rank[y_root]:
        parent[x_root] = y_root

    else: #임의로 일단 갖다붙힘
        parent[x_root] = y_root
        rank[y_root] += 1


n, m = map(int, input().split())
parent = [i for i in range(n+1)]
rank = [0] * (n+1)


for _ in range(m):
    command, a, b = map(int, input().split())

    if command: # x가 1이면
        # find 연산
        if find(a) == find(b):
            print("yes")
        else:
            print('no')
    else:
        #union 연산
        union(a, b)