def knapsack(wt, val, W, n):
    dp = [[0]*(W+1) for _ in range(n+1)]
    for i in range(n+1):
        for w in range(W+1):
            if i==0 or w==0:
                dp[i][w] = 0
            elif wt[i-1] <= w:
                dp[i][w] = max(val[i-1] + dp[i-1][w - wt[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
    return dp[n][W]

weights = [1, 3, 4, 5]
values = [1, 4, 5, 7]
capacity = 7
print("Maximum knapsack value:", knapsack(weights, values, capacity, len(weights)))
