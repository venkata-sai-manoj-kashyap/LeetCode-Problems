def func(n, dp):
    if n in dp:
        return dp[n]
    if n % 2 == 0:
        dp[n] = 4*(func(n-1, dp) - func(n-2, dp))
        return dp[n]
    else:
        dp[n] = 2*func(n-1, dp) + 2*(3*func(n-2, dp) - 6*func(n-3, dp) - 2*func(n-4, dp) + 4*func(n-5, dp))
        return dp[n]


print(func(161, {1: 10, 2: 20, 3: 46, 4: 104, 5: 240, 6: 544}))%(10**9 + 7)
