# https://school.programmers.co.kr/learn/courses/30/lessons/12987
# 숫자 게임, Lv 3

from collections import deque

def solution(A, B):
    A.sort(reverse=True)
    B_q = deque(sorted(B, reverse=True))
    answer = 0
    
    b = B_q.popleft()
    for a in A:
        if a >= b:
            continue
        if a < b:
            answer += 1
        if len(B_q) == 0:
            return answer
        b = B_q.popleft()

    return answer

# A를 내림차순 정렬, B도 내림차순 정렬해서 첫 번째 원소부터 B가 A보다 큰 경우만 answer를 1 올리고 아닌 경우는 skip
# A나 B 원소 다 탐색하면 answer Return.
