# https://school.programmers.co.kr/learn/courses/30/lessons/12977
# 소수 만들기, Lv 1

from itertools import combinations


def is_prime(num):
    for i in range(2, int(num ** (1 / 2)) + 1):
        if num % i == 0:
            return False
    return True


def solution(nums):
    count = 0
    nums_c = list(combinations(nums, 3))
    for c in nums_c:
        if is_prime(sum(c)):
            count += 1
    return count


# 해당 수와 제곱근의 사이에는 약수가 존재하지 않음을 이용해 제곱근까지만 약수가 존재하는지 탐색한다.
