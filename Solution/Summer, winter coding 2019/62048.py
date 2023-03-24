# https://school.programmers.co.kr/learn/courses/30/lessons/62048
# 멀쩡한 사각형, Lv 2

import math


def solution(w, h):
    # 최대공약수 구하기
    gcd = math.gcd(w, h)

    # 대각선으로 자른 정사각형 개수 구하기
    diagonal = w + h - gcd

    # 사용 가능한 정사각형 개수 구하기
    answer = w * h - diagonal

    return answer


# 대각선에 의해 잘리는 정사각형의 개수는, 사각형의 가로 길이 + 세로 길이 - 최대 공약수 이다.
# 대각선이 한 점에서 이동을 시작할 때 반대 점까지 이동하려면 가로의 길이 만큼 평행이동 해야하고 세로의 길이 만큼 수직이동해야한다. 마치 vector 처럼
# 하지만 실제로 지나는 정사각형을 체크해보면, 가로와 세로 방향으로 이동할 때 지나는 정사각형이 최대공약수 만큼 중복되어 count 된다는 것을 알 수 있다.
# 그러므로 가로 길이(가로 만큼 총 이동한 거리) + 세로 길이 (세로 만큼 총 이동한 거리) - 최대 공약수(중복으로 거쳐간 정사각형 개수)
