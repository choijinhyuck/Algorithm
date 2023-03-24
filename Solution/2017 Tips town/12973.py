# https://school.programmers.co.kr/learn/courses/30/lessons/12973
# 짝지어 제거하기, Lv 2


def solution(s):
    q = ["0"]
    for i in s:
        if q[-1] != i:
            q.append(i)
        else:
            q.pop()
            continue

    return 0 if len(q) - 1 else 1


# q에 문자열 0 을 1개 포함한 리스트 만들고 입력받은 문자열의 문자 하나씩 리스트의 마지막 원소와 비교한다.
# 같다면 append 하지 않고 리스트 마지막 원소 pop. 다르다면 append
