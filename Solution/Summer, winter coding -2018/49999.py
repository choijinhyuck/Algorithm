# https://school.programmers.co.kr/learn/courses/30/lessons/49993
# 스킬 트리, Lv 2

def solution(skill, skill_trees):
    answer = len(skill_trees)
    
    for tree in skill_trees:
        idx = -2
        for s in skill:
            if tree.find(s) == -1:
                idx = -1
                continue
            elif tree.find(s) > idx and idx != -1:
                idx = tree.find(s)
            else:
                answer -= 1
                break
    return answer
