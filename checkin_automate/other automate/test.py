def f(h, ns, ne, arr):
    dp = [[0.0] * (ne - ns) for _ in range(h + 1)]  # Initialize DP table

    for i in range(ns, ne):
        dp[0][i - ns] = 1 - arr[i]  # Base case when h is 0
        dp[1][i - ns] = arr[i]  # Base case when h is 1

    for i in range(1, h + 1):
        for j in range(ne - 1, ns - 1, -1):
            if j + 1 < ne:
                dp[i][j - ns] = (arr[j] * dp[i - 1][j - ns + 1]) + ((1 - arr[j]) * dp[i][j - ns + 1])
            else:
                dp[i][j - ns] = (1 - arr[j]) * dp[i][j - ns ]

    return dp[h][0]  # Return the result for h and starting index ns

# Example usage:
arr = [0.1, 0.2, 0.3, 0.4]
ne = len(arr)
result = f(2, 0, ne, arr)
print(result)
