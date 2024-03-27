# 100,000 * 1,000 = 100,000,000
import sys
from collections import defaultdict

input = sys.stdin.readline

def main():
    n = int(input())
    score = defaultdict(int)
    nums = list(map(int, input().split()))
    nums_set = set(nums)
    for num in nums:
        for i in range(1, int(num ** 0.5) + 1):
            if not num % i:  # 나누어서 0이 되면
                if i in nums_set:  # 나누는 수가 nums_set에 있으면
                    score[i] += 1
                    score[num] -= 1
                if num != i ** 2 and num // i != num and num // i in nums_set:  # num // i가 nums_set에 있으면
                    score[num // i] += 1
                    score[num] -= 1

    result = []
    for num in nums:
        result.append(score[num])

    print(' '.join(map(str, result)))

if __name__ == '__main__':
    main()