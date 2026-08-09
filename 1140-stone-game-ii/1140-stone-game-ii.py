from functools import lru_cache

class Solution:
    def stoneGameII(self, piles: list[int]) -> int:
        n = len(piles)
        # suffix_sum[i] = sum of piles[i:]
        suffix_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]

        @lru_cache(maxsize=None)
        def dp(i: int, M: int) -> int:
            if i >= n:
                return 0
            if 2 * M >= n - i:
                return suffix_sum[i]

            best = 0
            for X in range(1, 2 * M + 1):
                if i + X > n:
                    break
                best = max(best, suffix_sum[i] - dp(i + X, max(M, X)))
            return best

        return dp(0, 1)