class Solution:
    def stoneGameV(self, stoneValue: list[int]) -> int:
        n = len(stoneValue)
        prefix = [0] * (n + 1)
        for i, v in enumerate(stoneValue):
            prefix[i + 1] = prefix[i] + v

        def rsum(i, j):  
            return prefix[j + 1] - prefix[i]

        dp = [[0] * n for _ in range(n)]
        maxL = [[0] * n for _ in range(n)]  
        maxR = [[0] * n for _ in range(n)]  
        for i in range(n):
            maxL[i][i] = stoneValue[i]
            maxR[i][i] = stoneValue[i]

        for length in range(2, n + 1):
            for i in range(0, n - length + 1):
                j = i + length - 1
                total = rsum(i, j)

                
                lo, hi, k_eq = i, j - 1, i - 1
                while lo <= hi:
                    mid = (lo + hi) // 2
                    if 2 * rsum(i, mid) <= total:
                        k_eq = mid
                        lo = mid + 1
                    else:
                        hi = mid - 1

                best = 0
                if k_eq >= i:
                    best = max(best, maxL[i][k_eq])
                    if 2 * rsum(i, k_eq) == total:
                        best = max(best, rsum(i, k_eq) + dp[k_eq + 1][j])
                if k_eq + 2 <= j:
                    best = max(best, maxR[k_eq + 2][j])

                dp[i][j] = best
                maxL[i][j] = max(maxL[i][j - 1], dp[i][j] + total)
                maxR[i][j] = max(maxR[i + 1][j], dp[i][j] + total)

        return dp[0][n - 1]