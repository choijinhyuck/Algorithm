# https://school.programmers.co.kr/learn/courses/30/lessons/87377
# 교점에 별 만들기, Lv 2

import random

def solution(line):
    point = set()
    for i, (a, b, e) in enumerate(line[:-1]):
        for c, d, f in line[i+1:]:
            lower = a*d - b*c
            if lower == 0: continue
            x_upper = b*f - e*d
            y_upper = e*c - a*f
            if x_upper % lower != 0 or y_upper % lower != 0: continue
            point.add((x_upper//lower, y_upper//lower))
    
    x_max, y_max = random.sample(point, 1)[0]
    x_min, y_min = x_max, y_max
    
    for x, y in point:
        x_max = max(x_max, x)
        x_min = min(x_min, x)
        y_max = max(y_max, y)
        y_min = min(y_min, y)
    
    ncol = x_max - x_min + 1
    nrow = y_max - y_min + 1
    result = [['.' for _ in range(ncol)] for _ in range(nrow)]
    for x, y in point:
        result[y_max - y][x - x_min] = '*'
    answer = []
    for r in result:
        answer.append("".join(r))
    return answer
