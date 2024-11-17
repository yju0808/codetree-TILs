import copy

# 입력 받기
a_length, b_length = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

# 1-based 인덱싱을 위해 앞에 0 추가
a.insert(0, 0)
b.insert(0, 0)

# DP 테이블 초기화: dp[i][j]는 a[1..i]와 b[1..j]의 LCS를 저장
dp = [[[] for _ in range(len(b))] for _ in range(len(a))]

# dp[1][1] 초기화
dp[1][1] = [a[1]] if a[1] == b[1] else []

def get_max_str(list1, list2):
    """
    두 리스트 중 더 긴 리스트를 반환합니다.
    길이가 같을 경우, 사전 순으로 더 작은 리스트를 반환합니다.
    """
    if len(list1) > len(list2):
        return list1.copy()
    elif len(list1) < len(list2):
        return list2.copy()
    else:
        return list1.copy() if list1 < list2 else list2.copy()

# DP 테이블 첫 번째 열 초기화
for i in range(1, len(a)):
    if a[i] == b[1]:
        dp[i][1] = [a[i]]
    else:
        dp[i][1] = dp[i - 1][1].copy()

# DP 테이블 첫 번째 행 초기화
for j in range(1, len(b)):
    if a[1] == b[j]:
        dp[1][j] = [b[j]]
    else:
        dp[1][j] = dp[1][j - 1].copy()

# DP 테이블 채우기
for i in range(2, len(a)):
    for j in range(2, len(b)):
        if a[i] == b[j]:
            dp[i][j] = dp[i - 1][j - 1].copy() + [a[i]]
        else:
            dp[i][j] = get_max_str(dp[i - 1][j], dp[i][j - 1])

# 최종 LCS 출력
ans = dp[len(a) - 1][len(b) - 1]
print(*ans)
