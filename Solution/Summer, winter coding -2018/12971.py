# https://school.programmers.co.kr/learn/courses/30/lessons/12971
# 스티커 모으기 (2), Lv 3


def solution(sticker):
    l = len(sticker)
    if l == 1 or l == 2 or l == 3:
        return max(sticker)

    dp_0 = [0] * l
    dp_1 = [0] * l
    dp_0[0], dp_0[2] = sticker[0], sticker[0] + sticker[2]
    dp_1[1], dp_1[2] = (
        sticker[1],
        sticker[2],
    )
    for idx, s in enumerate(sticker[3:l], 3):
        dp_0[idx] = s + max(dp_0[idx - 3], dp_0[idx - 2])
        dp_1[idx] = s + max(dp_1[idx - 3], dp_1[idx - 2])

    return max(dp_0[0 : l - 1] + dp_1[0:])


# 다양한 경우의 수가 있어서 뭔가 복잡하다고 생각이 들면 바로 동적계획법 DP를 쓰는 게 대체로 맞다.
# 첫 번째 스티커를 선택하는 경우를 잘 생각한다.
# 0번 원소를 선택하면 마지막 원소를 선택할 수 없지만, 1번부터 원소를 선택하면 마지막 원소를 선택해도 문제가 없다.
# 그러므로 0번 원소를 먼저 선택하는 경우를 dp_0 으로 나머지 경우를 dp_1 로 2개로 나누어서 리스트를 만든다.
# 점화식을 구상한다. 특정 위치의 원소를 택할 수 있는 방법은 2 칸 앞의 원소를 선택하는 방법과 3 칸 앞의 원소를 선택하는 방법이 있다.
# 3 칸 앞 선택하고 직전 칸 선택하면 현재 칸을 선택할 수 없으므로.
# 그리고 그 두 가지 칸 중에서 더 max 함수를 활용해 더 높은 합계를 갖는 칸을 선택하고 현재 칸의 숫자를 더해서 현재 칸의 dp값을 갱신한다.
# dp_0 은 마지막 원소를 포함할 수 없으므로 마지막 원소 전까지, dp_1은 끝까지 선택해서 해당하는 리스트 원소 중 가장 큰 값을 max 함수를 활용해 return 한다.
