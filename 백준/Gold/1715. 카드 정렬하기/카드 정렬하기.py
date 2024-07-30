import sys
input = sys.stdin.readline

N = int(input())
# # 정렬한 nums를 heap자료구조의 리프노드에 모두 넣는다.
# # 거기서 부모노드는 그 자식노드의 합으로 만든다. -> 루트를 출력
# nums = []
# for _ in range(N):
#     num = int(input())
#     nums.append(num)
#
# nums = sorted(nums)


from heapq import heappush, heappop, heapify
# cards = [int(input()) for _ in range(N)]
# #cards를 힙 자료구조로 바꿈
# heapify(cards)

cards = []
for _ in range(N):
    heappush(cards, int(input()))

cnt = 0

while len(cards) > 1:
    A, B = heappop(cards), heappop(cards)

    cnt += A + B

    heappush(cards, A+B)

print(cnt)