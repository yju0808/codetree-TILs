MAX_ANS = 101

# 변수 선언 및 입력:
n, m = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

# 메모이제이션을 위한 dp 배열 생성
# dp[i][j] : i번째 원소부터 끝까지 사용하여 합이 j일 때의 최소 수열의 길이
dp = [[-1] * (m + 1) for _ in range(n + 1)]

def dfs(index, sum):
    # 합이 정확히 m이 되었을 때
    if sum == m:
        return 0
    # 인덱스를 벗어나거나 합이 초과된 경우
    if index == n or sum > m:
        return MAX_ANS
    # 이미 계산한 값이 있으면 반환
    if dp[index][sum] != -1:
        return dp[index][sum]
    
    # 현재 원소를 선택하지 않는 경우
    res = dfs(index + 1, sum)
    # 현재 원소를 선택하는 경우 (각 원소를 최대 한 번씩만 선택)
    res = min(res, dfs(index + 1, sum + arr[index]) + 1)
    
    dp[index][sum] = res
    return res

min_len = dfs(0, 0)

# 합 m을 만드는 것이 불가능 할 시, -1을 출력합니다.
if min_len >= MAX_ANS:
    min_len = -1

print(min_len)