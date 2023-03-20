# https://school.programmers.co.kr/learn/courses/30/lessons/12979
# 기지국 설치, Lv 3

def solution(n, stations, w):
    answer = 0
    if len(stations) == 0:
        return (n - 1) // (w * 2 + 1) + 1
    if stations[0] -1 - w > 0:
        answer += (stations[0] - w - 1 - 1) // (w * 2 + 1) + 1
    if len(stations) != 1:
        for s, ns in zip(stations, stations[1:]):
            if ns - s - 1 <= w * 2:
                continue
            else:
                answer += (ns - s - 2 - (w * 2)) // (w * 2 + 1) + 1
    if n - stations[-1] - w > 0:
        answer += (n - stations[-1] - w - 1) // (w * 2 + 1) + 1
    
    return answer

# 각 끝과 station 간 거리, station 간 거리가 w를 고려해 1 이상일 때 기지국 본인을 포함한 양쪽 w, w * 2 + 1 로 거리들을 나눈 몫에 1 을 더해 answer
