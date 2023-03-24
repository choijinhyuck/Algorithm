# https://school.programmers.co.kr/learn/courses/30/lessons/62050
# 지형 이동, Lv 4

import heapq


def find(a, parent):
    if parent[a] == a:
        return parent[a]
    else:
        parent[a] = find(parent[a], parent)
        return parent[a]


# 재귀적으로 부모 그룹을 계속 찾아 최상위 부모를 찾고, 매번 최상위 부모로 값을 갱신한다.


def union(a, b, parent):
    A = find(a, parent)
    B = find(b, parent)
    if A > B:
        parent[A] = B
    elif A < B:
        parent[B] = A
    else:
        return False
    return True


# a와 b의 최상위 부모를 찾아 서로 같은 그룹에 속해 있는지 비교한다. 다른 그룹이라면 index가 더 작은 부모쪽 그룹으로 합친다.
# 서로 같은 그룹일 경우 이미 어딘가에 사다리가 설치되었거나 높이차가 cost보다 낮은 경우이기 때문에 False를 반환해 바로 다음 graph 탐색을 하도록 한다.
# 이미 처리된 경우라 신경쓰지 않아도 된다.


def solution(land, height):
    graph_1 = [
        (abs(land[i][j] - land[i][j + 1]), len(land) * i + j + 1, len(land) * i + j + 2)
        for i in range(len(land))
        for j in range(len(land) - 1)
    ]
    # 행별로 모든 높이차를 계산하고, 각 위치 좌표를 1차원으로 바꾸어서 저장
    graph_2 = [
        (abs(land[i][j] - land[i + 1][j]), len(land) * i + j + 1, len(land) * (i + 1) + j + 1)
        for i in range(len(land) - 1)
        for j in range(len(land))
    ]
    # 열별로 모든 높이차를 계산하고, 각 위치 좌표를 1차원으로 바꾸어서 저장

    parent = [i for i in range(len(land) * len(land) + 1)]  # index는 자식, 값은 부모 index를 가리키는 리스트
    graph = graph_1 + graph_2
    heapq.heapify(
        graph
    )  # 서로 인접한 모든 장소간 높이차와 위치 정보가 담긴 graph를 생성하고, 가장 작은 cost 값을 갖는 리스트부터 반환하도록 최소힙을 사용한다.

    total_cost = 0
    while graph:
        cost, a, b = heapq.heappop(graph)
        if union(a, b, parent):  # a와 b가 서로 다른 그룹일 경우
            if cost > height:  # height 보다 cost가 높으면 total_cost에 cost 추가
                total_cost += cost

    return total_cost
