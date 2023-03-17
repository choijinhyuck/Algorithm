# https://school.programmers.co.kr/learn/courses/30/lessons/12985
# 예상 대진표, Lv 2

def solution(n,a,b):
    count = 0
    while a != b:
        a = (a + 1)//2 if a % 2 else a//2
        b = (b + 1)//2 if b % 2 else b//2
        count += 1
    return count
