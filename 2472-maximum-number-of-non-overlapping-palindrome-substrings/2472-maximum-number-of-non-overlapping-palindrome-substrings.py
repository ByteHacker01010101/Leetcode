class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)

        # isPal[i][j] = True if s[i..j] (inclusive) is a palindrome
        isPal = [[False] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            isPal[i][i] = True
            for j in range(i + 1, n):
                if s[i] == s[j] and (j - i == 1 or isPal[i + 1][j - 1]):
                    isPal[i][j] = True

        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i - 1]
            if i >= k and isPal[i - k][i - 1]:
                dp[i] = max(dp[i], dp[i - k] + 1)
            if i >= k + 1 and isPal[i - k - 1][i - 1]:
                dp[i] = max(dp[i], dp[i - k - 1] + 1)

        return dp[n]