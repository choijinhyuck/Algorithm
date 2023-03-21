# https://school.programmers.co.kr/learn/courses/30/lessons/12978
# 배달, Lv 2

from collections import deque

def solution(N, road, K):
    q = deque([1])  # 원소가 최대 1개씩만 들어갈 거라 list를 사용해도 무방
    t = [int(1e9)] * (N+1)  # 1번 마을부터 해당 마을까지 거리, 일단 1e9로 초기화
    t[1] = 0
    visited = [False] * (N+1)
    visited[0] = True
    graph = [[] for _ in range(N+1)]

    for start, end, cost in road:
        graph[start].append((end, cost))
        graph[end].append((start, cost))
    # 길의 왕복을 고려해 거리 정보도 함께 graph에 담음
    
    while q:
        now = q.popleft()
        visited[now] = True
        for dest, cost in graph[now]:
            if not visited[dest]:
                t[dest] = min(t[now] + cost, t[dest])  # 현재 최대 거리와 지금 방문 마을에서 갈 때 걸리는 거리 중 짧은 것으로 갱신
        q_idx = 0
        temp_t = int(1e9)
        for visit, time, idx in zip(visited, t, range(N+1)):  # enumerate 함수를 사용해도 괜찮고 데이터가 작아서 상관없지만 커질수록 최소힙을 사용하는 게 유리함.
            if not visit:
                if time < temp_t:
                    temp_t = time
                    q_idx = idx
        if q_idx:
            q.append(q_idx)  # 방문하지 않은 마을 중 가장 짧은 거리를 갖는 곳 큐에 넣음.
    
    answer = 0
    for i in t[2:]:  # 0 번 마을은 없으니 제외. 1 번 마을은 무조건 거리가 0 이라 제외.
        if i <= K:
            answer += 1
        
    return answer + 1  # 1 번 마을 추가


# path를 graph에 왕복을 고려하여 정리하고 매번 가장 가까운 node를 방문하면서 최단거리를 갱신하는 게 
