# https://school.programmers.co.kr/learn/courses/30/lessons/12984
# 지형 편집, Lv 4


from collections import Counter


def solution(land, P, Q):
    line = []
    for a in land:  # Block 정보를 1차원 리스트로 변환
        line += a
    l = len(line)  # 전체 지형 칸 개수. 넓이
    land_dic = Counter(line)  # 특정 원소를 key로 하고 그 개수를 value로 만들어 dictionary에 넣음
    land_key = sorted(land_dic.keys())  # 오름차순 key 정렬
    total_blocks = 0
    for c in land_dic:
        total_blocks += c * land_dic[c]  # 모든 블럭 개수

    total = total_blocks * Q  # 모든 블럭 개수를 일단 파괴했을 때 드는 최대 비용. 높이를 0으로 맞출 때 드는 비용
    answer = total
    pre_key = 0
    n_blocks = 0
    temp = total

    for key in land_key:  # 매 key 값이 목표로 하는 높잇값을 의미함
        temp += ((key - pre_key) * n_blocks * P) - ((key - pre_key) * l * Q)
        # 목표 높이보다 아래에 있는 블럭들의 개수를 매번 갱신하고, 매 현재 높이와 목표 높이의 차이 * 짓는 데 필요한 값 P 를 갱신한 블럭 개수와 곱해서 temp에 더함
        # 이미 다 제거했다고 가정하고 total 값을 계산했었기 때문에, 다시 높이가 0에서부터 올라갈 때마다 해당 높이만큼 허물었던 비용을 회수함
        answer = min(answer, temp)  # 최소 비용으로 갱신
        l -= land_dic[key]  # 전체 넓이에서 더이상 허문 비용 회수할 필요 없는 부분 제거
        n_blocks += land_dic[key]  # 목표 높이보다 낮은 높이를 갖는 블럭을 매 반복마다 추가
        pre_key = key  # 현재 높이 (직전 높이) 갱신

    return answer
