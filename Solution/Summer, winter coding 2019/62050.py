# https://school.programmers.co.kr/learn/courses/30/lessons/62050
# 지형 이동, Lv 4

import heapq

def find(a, parent):
    if parent[a] == a:
        return parent[a]
    else:
        parent[a] = find(parent[a], parent)
        return parent[a]
        
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
        
def solution(land, height):
    graph_1 = [(abs(land[i][j]-land[i][j+1]), len(land)*i+j+1, len(land)*i+j+2) for i in range(len(land)) for j in range(len(land)-1)]
    graph_2 = [(abs(land[i][j]-land[i+1][j]), len(land)*i+j+1, len(land)*(i+1)+j+1) for i in range(len(land)-1) for j in range(len(land))]
    
    parent = [i for i in range(len(land)*len(land)+1)]
    graph = graph_1 + graph_2
    heapq.heapify(graph)
    
    total_cost = 0
    while graph:
        cost, a, b = heapq.heappop(graph)
        if union(a, b, parent):
            if cost > height:
                total_cost += cost
                

    return total_cost
