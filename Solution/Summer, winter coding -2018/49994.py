# https://school.programmers.co.kr/learn/courses/30/lessons/49994
# 방문 길이, Lv 2


def solution(dirs):
    now = (0, 0)
    path = set()
    direc = {"U": (0, 1), "D": (0, -1), "L": (-1, 0), "R": (1, 0)}
    for d in dirs:
        nnow = (now[0] + direc[d][0], now[1] + direc[d][1])
        if -5 <= nnow[0] <= 5 and -5 <= nnow[1] <= 5:
            path.add((now, nnow))
            path.add((nnow, now))
            now = nnow

    return len(path) // 2


# 이동 방향 값을 direc에 매핑을 해놓고 평면이 넘어가는지 체크.
# 넘어간다면 무시하고 넘어가지 않는다면 현재 좌표와 다음 이동 좌표를 같이 Tuple로 path set에 넣어 경로 형태 데이터를 저장
# 반대 순서로도 tuple을 넣어 이미 지나간 길임을 표현
# path에 왕복 데이터를 넣어서 마지막에 2로 나눠서
