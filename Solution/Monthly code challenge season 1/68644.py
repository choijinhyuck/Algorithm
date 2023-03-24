# https://school.programmers.co.kr/learn/courses/30/lessons/68644
# 두 개 뽑아서 더하기, Lv 1

from itertools import combinations


def solution(numbers):
    return sorted(list(set(map(sum, combinations(numbers, 2)))))
