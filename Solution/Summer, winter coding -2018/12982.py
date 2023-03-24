# https://school.programmers.co.kr/learn/courses/30/lessons/12982
# 예산, Lv 1


def solution(d, budget):
    total = 0
    for idx, cost in enumerate(sorted(d)):
        total += cost
        if total > budget:
            return idx
    return len(d)


# 필요 예산이 담긴 리스트를 오름차순으로 정렬하고 작은 예산부터 차례로 채워나가서 최대치를 넘기게 되면 반환한다.
