# https://school.programmers.co.kr/learn/courses/30/lessons/68935
# 3진법 뒤집기, Lv 1

def solution(n):
    tri = []
    if n < 3:
        return n
    while True:
        tri.append(str(n%3))
        n //= 3
        if n < 3:
            tri.append(str(n))
            break
    return int(''.join(tri), base=3)
