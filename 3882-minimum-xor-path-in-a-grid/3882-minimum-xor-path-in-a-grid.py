class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp: list[set[int]] = [set() for _ in range(n)]

        for i in range(m):
            for j in range(n):
                g = grid[i][j]
                if i == 0 and j == 0:
                    dp[0] = {g}
                    continue

                prev: set[int] = set()
                prev |= dp[j]           
                if j > 0:
                    prev |= dp[j - 1]   

                dp[j] = {x ^ g for x in prev}

        return min(dp[n - 1])