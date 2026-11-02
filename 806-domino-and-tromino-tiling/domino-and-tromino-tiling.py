class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1

        if n >= 2:
            dp[2] = 2

        for width in range(3, n + 1):
            dp[width] = (2 * dp[width - 1] + dp[width - 3]) % MOD

        return dp[n]
        