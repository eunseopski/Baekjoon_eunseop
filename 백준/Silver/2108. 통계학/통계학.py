import sys
from collections import Counter
import statistics

N = int(sys.stdin.readline())
numbers = [int(sys.stdin.readline()) for _ in range(N)]

# 1. 산술평균
mean = round(sum(numbers) / N)

# 2. 중앙값
median = statistics.median(numbers)

# 3. 최빈값
mode_counter = Counter(numbers)
modes = mode_counter.most_common()
if len(modes) > 1 and modes[0][1] == modes[1][1]:
    mode = sorted(num for num, count in modes if count == modes[0][1])[1]
else:
    mode = modes[0][0]

# 4. 범위
range_value = max(numbers) - min(numbers)

# 결과 출력
print(mean)
print(int(median))
print(mode)
print(range_value)