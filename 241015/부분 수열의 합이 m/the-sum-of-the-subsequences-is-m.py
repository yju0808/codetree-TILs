MAX_ANS = 101

# 변수 선언 및 입력:
n, m = map(int, input().split())
arr = list(map(int, input().split()))

# 메모이제이션을 위한 dp 배열 생성
# dp[i][rem] : i번째 원소부터 끝까지 사용하여 남은 금액 rem을 만들기 위한 최소 수열의 길이
dp = [[-1] * (m + 1) for _ in range(n + 1)]

def dfs(index, rem):
    # 남은 금액을 정확히 0으로 만들었을 때
    if rem == 0:
        return 0
    # 인덱스를 벗어나거나 남은 금액이 음수가 된 경우
    if index == n or rem < 0:
        return MAX_ANS
    # 이미 계산한 값이 있으면 반환
    if dp[index][rem] != -1:
        return dp[index][rem]
    
    # 현재 원소를 선택하지 않는 경우
    res = dfs(index + 1, rem)
    # 현재 원소를 선택하는 경우 (각 원소를 최대 한 번씩만 선택)
    if rem >= arr[index]:
        res = min(res, dfs(index + 1, rem - arr[index]) + 1)
    
    dp[index][rem] = res
    return res

min_len = dfs(0, m)

# 합 m을 만드는 것이 불가능 할 시, -1을 출력합니다.
if min_len >= MAX_ANS:
    min_len = -1

print(min_len)