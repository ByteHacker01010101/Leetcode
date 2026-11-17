class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        INF = float('inf')

        divisors = [[] for _ in range(n + 1)]
        for L in range(2, n + 1):
            for d in range(1, L):
                if L % d == 0:
                    divisors[L].append(d)

        cost = [[INF] * (n + 1) for _ in range(n + 1)]
        for i in range(n):
            for j in range(i + 2, n + 1):
                L = j - i
                best = INF
                for d in divisors[L]:
                    changes = 0
                    for r in range(d):
                        lo, hi = i + r, j - d + r
                        while lo < hi:
                            if s[lo] != s[hi]:
                                changes += 1
                            lo += d
                            hi -= d
                    best = min(best, changes)
                cost[i][j] = best

        dp = [[INF] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        for p in range(1, k + 1):
            for i in range(2 * p, n + 1):
                for h in range(2 * (p - 1), i - 1):
                    if dp[h][p - 1] < INF:
                        dp[i][p] = min(dp[i][p], dp[h][p - 1] + cost[h][i])

        return dp[n][k]