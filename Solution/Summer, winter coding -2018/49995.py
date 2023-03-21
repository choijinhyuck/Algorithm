# https://school.programmers.co.kr/learn/courses/30/lessons/49995
# 쿠키 구입, Lv 4

# 1번 풀이 - 구간합
def solution(cookie):
    l = len(cookie)
    t = [0]
    for i in range(l):
        t.append(t[i] + cookie[i]) # 구간합을 미리 구해서 시간 복잡도를 낮춤
    answer = 0

    for i in range(l - 1): # 왼쪽 바구니 시작점
        for j in range(l - i - 1): # 오른쪽 바구니 끝점
            left = t[i + 1 + j] - t[i]  # 왼쪽 바구니 전체 쿠키 개수
            right = t[i + 2 + j] - t[i + 1 + j]  # 오른쪽 바구니 전체 쿠키 개수
            if left < answer: # 왼쪽 합이 현재 최고 쿠키 획득 개수보다 작으면 바로 스킵
                continue
            if (t[-1] - t[i])//2 < left: # 왼쪽 바구니 쿠키 총합이 전체의 반을 넘으면 오른쪽 바구니에서 같은 양 쿠키 획득 불가
                break
            if (t[-1] - t[i]) % 2 == 0 and (t[-1] - t[i])//2 == left:
                answer = max(answer, left)
                break
            if left == right:
                answer = max(answer, left)
            elif left < right:
                continue
            else: # right가 left보다 큰 경우
                if l - i - j - 1 >= 2: # 오른쪽 바구니 위치 이동 가능 여부
                    for k in range(1, l - i - j - 1):
                        right = t[i + 2 + j + k] - t[i + 1 + j]
                        if left == right:
                            answer = max(answer, left)
                            break
                        elif left < right:
                            break
                        else:
                            continue

    return answer

# 2번 풀이 - 구간합
def solution(cookie):
    n = len(cookie)
    prefix_sum = [0] * (n+1)
    # prefix_sum[i] = 0부터 i-1까지의 구간 합
    for i in range(1, n+1):
        prefix_sum[i] = prefix_sum[i-1] + cookie[i-1]
    
    answer = 0
    for i in range(n-1): # i를 기준으로 바구니를 나누기 때문에 n-1까지 반복
        for j in range(i+1, n): # j는 i+1부터 시작
            # i부터 j까지의 구간 합 계산
            sum_i_j = prefix_sum[j+1] - prefix_sum[i]
            if sum_i_j >= answer * 2:
                # 두 아들이 받을 과자 수가 같아야 하므로, i부터 m까지와 m+1부터 j까지의 합이 같을 때만 갱신
                for k in range(i, j):
                    sum_i_m = prefix_sum[k+1] - prefix_sum[i]
                    if sum_i_m == sum_i_j - sum_i_m:
                        answer = max(answer, sum_i_m)
    
    return answer

# 3번 풀이 - 투포인터
def solution(cookie):
    n = len(cookie)
    max_cookie = 0
    for m in range(n-1):
        left, right = m, m+1
        sum_left, sum_right = cookie[left], cookie[right]
        while True:
            if sum_left == sum_right:
                max_cookie = max(max_cookie, sum_left)
            if sum_left <= sum_right and left > 0:
                left -= 1
                sum_left += cookie[left]
            elif sum_left >= sum_right and right < n-1:
                right += 1
                sum_right += cookie[right]
            else:
                break
    
    return max_cookie
