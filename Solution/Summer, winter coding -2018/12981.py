# https://school.programmers.co.kr/learn/courses/30/lessons/12981
# 영어 끝말잇기, Lv 2

def solution(n, words):
    if len(words[0]) == 1:
        return [1,1]
    for idx, word in enumerate(words[1:], 1):
        if len(word) == 1 or words[idx-1][-1] != word[0] or word in words[:idx]:
            return [(idx % n) + 1, (idx // n) + 1]
    return [0,0]

# 전 단어의 끝 문자와 다음에 오는 문자의 첫 번째 문자가 같은지 확인하고, 새로 오는 단어가 이미 나온 단어인지 체크하면 된다.
# 길이가 1인 단어를 자꾸 체크했는데 지금은 단어 길이가 2이상 이라고 명시 돼 있는데 전에는 없었을 지도 모르겠다.
# input의 데이터가 크지 않아서 위처럼 작성해도 문제가 되진 않지만, word 가 이미 있는지 체크하는 부분에서 현재 index 까지 리스트를
# 조사하는 것이기 때문에 시간복잡도가 커진다.
# 단어가 문제 없이 넘어갈 때마다 set를 만들어서 add 한 다음, 단어를 체크하는 게 시간복잡도가 훨씬 줄어들 수 있을 것이다.
# 아니면dictionary를 활용해서 체크할 수도 있을 것 같다. Hash를 사용하는게 효율적이다.
