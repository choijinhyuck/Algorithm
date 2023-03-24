# https://school.programmers.co.kr/learn/courses/30/lessons/70129
# 이진 변환 반복하기, Lv 2


def convert(s, count):
    count += s.count("0")
    return format(s.count("1"), "b"), count


def solution(s):
    count = 0
    con_count = 0
    while s != "1":
        s, count = convert(s, count)
        con_count += 1
    return [con_count, count]
