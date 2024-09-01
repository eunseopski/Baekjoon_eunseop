import sys
input = sys.stdin.readline

N = int(input())
save_list = [[], [1] * 10]
save_list.extend([[0]*10 for i in range(N-1)])

def get_sum(I, num):
    #I번째 자릿수, num의 답을 바로 알고 있다면
    if save_list[I][num]:
        return save_list[I][num]
    # 모른다면 I-1번째 자릿수의 각 옆 얘들을 더하고 리스트에 저장
    else:
        if num == 0:
            save_list[I][num] = get_sum(I-1, num+1)
            return save_list[I][num]
        elif num == 9:
            save_list[I][num] = get_sum(I-1, num-1)
            return save_list[I][num]
        else:
            save_list[I][num] = get_sum(I-1, num-1) + get_sum(I-1, num+1)
            return save_list[I][num]


for i in range(1, 10):
    get_sum(N, i)

print(sum(save_list[N][1:]) % 1000000000)

