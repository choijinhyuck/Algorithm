# https://school.programmers.co.kr/learn/courses/30/lessons/87377
# 교점에 별 만들기, Lv 2

import random


def solution(line):
    point = set()
    for i, (a, b, e) in enumerate(line[:-1]):
        for c, d, f in line[i + 1 :]:
            lower = a * d - b * c
            if lower == 0:
                continue
            x_upper = b * f - e * d
            y_upper = e * c - a * f
            if x_upper % lower != 0 or y_upper % lower != 0:
                continue
            point.add((x_upper // lower, y_upper // lower))

    x_max, y_max = random.sample(point, 1)[0]
    x_min, y_min = x_max, y_max

    for x, y in point:
        x_max = max(x_max, x)
        x_min = min(x_min, x)
        y_max = max(y_max, y)
        y_min = min(y_min, y)

    ncol = x_max - x_min + 1
    nrow = y_max - y_min + 1
    result = [["." for _ in range(ncol)] for _ in range(nrow)]
    for x, y in point:
        result[y_max - y][x - x_min] = "*"
    answer = []
    for r in result:
        answer.append("".join(r))
    return answer


# 행렬을 활용해서 2차 방정식에서 X와 Y를 손쉽게 구할 수 있다.
# 그냥 연립 방정식을 사용해 X와 Y를 각각 구하는 식을 만든다.
# 역행렬이 존재하지 않으면 (각 해의 분모가 0 이면) 2차원 직교 좌표계에서 기울기가 같은 평행항 직선이거나 똑같은 직선임을 의미한다.
# 입력값으로 같은 직선은 들어오지 않으므로 기울기가 같은 평행한 직선이고 교점은 존재하지 않음을 알 수 있다.
# X와 Y를 구하는 식을 만드는 명령문을 바탕으로 입력값을 받아 결과값을 구하고 int 로 casting 하여 소수점을 버린다.
# .과 *을 가로 세로 길이를 고려하여 적절히 잘 배치하도록 한다. 위아래, 좌우가 반전되지 않도록 유의한다.
