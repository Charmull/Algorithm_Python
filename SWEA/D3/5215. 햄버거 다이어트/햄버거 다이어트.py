# dp[i][j] = i번째 재료를 고려하여 j칼로리로 제한할때 최대 맛
# dp[i][j] = dp[i - 1][j] (i번째 재료의 칼로리가 j보다 크면)
# dp[i][j] = max(dp[i - 1][j - ki] + ki, dp[i - 1][j])			(i번째 재료의 칼로리가 j보다 작거나 같으면)
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, l = map(int, input().split())
    data = [[0, 0]] + [list(map(int, input().split())) for _ in range(n)]
    data.sort(key=lambda x: x[1])
    dp = [[0] * 10001 for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, 10001):
            if data[i][1] > j:
                dp[i][j] = dp[i - 1][j]
                continue
            dp[i][j] = max(dp[i - 1][j - data[i][1]] + data[i][0], dp[i - 1][j])

    print(f'#{test_case}', dp[n][l])
