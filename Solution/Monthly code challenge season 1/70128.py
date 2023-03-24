# https://school.programmers.co.kr/learn/courses/30/lessons/70128
# 내적, Lv 1


def solution(a, b):
    return sum(map(lambda x: x[0] * x[1], zip(a, b)))
