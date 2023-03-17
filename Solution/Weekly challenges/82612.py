# https://school.programmers.co.kr/learn/courses/30/lessons/82612
# 부족한 금액 계산하기, LV 1

def solution(price, money, count):
    total = 0
    for i in range(count):
        total += price * (i+1)

    if total > money:
        return total - money
    else:
        return 0
