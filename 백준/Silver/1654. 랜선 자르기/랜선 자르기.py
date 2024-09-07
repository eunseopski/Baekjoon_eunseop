import sys
input = sys.stdin.readline

K, N = map(int, input().split())
K_list = [int(input()) for _ in range(K)]

r = max(K_list)
l = 1
visited = set()

while True:
    num_LAN = 0
    K_len = (r + l) // 2

    for a in K_list:
        num_LAN += a // K_len
    # print(l, r, K_len, num_LAN)
    if num_LAN >= N:
        # N개보다 크면 K_LAN을 반으로 줄인당
        visited.add(K_len)

        l = K_len + 1
    else:
        # N개보다 작으면 K_LAN의 값을 크게
        r = K_len - 1

    if l > r:
        # print(K_len)
        print(max(visited))
        # print(visited)
        exit()