# https://school.programmers.co.kr/learn/courses/30/lessons/12983
# 단어 퍼즐, Lv 4

from collections import defaultdict


def solution(strs, t):
    str_d = defaultdict(list)
    for word in strs:
        str_d[word[0]].append([word, len(word)])

    count = [int(1e9)] * (len(t) + 1)
    count[0] = 0
    for i in range(len(t)):
        for word, word_l in str_d[t[i]]:
            if word == t[i:i+word_l]:
                count[i + word_l] = min(count[i + word_l], count[i] + 1)

    return count[-1] if count[-1] != int(1e9) else -1
  
# 거스름돈이 높은 가치를 갖는 화폐부터 낮은 가치 화폐순서로 차례대로 채우면 목푯값을 만들 수 있음 Greedy 탐욕법 알고리즘과는 달리
# 동전이 700원처럼 애매한 가치를 갖는 것이 있는 경우엔 동적계획법(DP; Dynamic Programming) 으로 최소 개수 동전으로 목푯값 달성하는 것과 비슷한 문제.
# 단어를 완성하는 모든 경우의 수를 다 계산해서 사용된 문자열 개수를 구하는 것은 굉장히 오래 걸린다.
# 각 단어 조각들을 첫 글자를 key로 하는 dictionary를 만들고 value 로는 해당 단어와 그 단어의 길이를 원소로 갖는 list를 갖는 list를 전달한다.
# 목표로 하는 문자열의 길이 만큼 (여기서는 +1) count list를 만들고 목표 문자열의 첫 문자부터 사용될 수 있는 모든 단어들을 넣어 보며
# count list의 숫자를 더 작은 것으로 갱신한다. 그리고 count의 마지막 값을 return 한다. 1e9 값이면 불가능한 것이므로 -1 반환.

# 여기서는 단어 조각들이 무한으로 있다고 가정되어 있어서 이런 방법이 가능한데 개수 제한이 있으면 다른 접근을 해야할 듯하다.
