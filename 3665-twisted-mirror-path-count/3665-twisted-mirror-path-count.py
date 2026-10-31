class Solution:
    def uniquePaths(self, grid: list[list[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        right = [[0] * n for _ in range(m)]  # entered cell moving right
        down = [[0] * n for _ in range(m)]   # entered cell moving down
        right[0][0] = 1

        for i in range(m):
            for j in range(n):
                r, d = right[i][j], down[i][j]

                if grid[i][j] == 0:
                    tot = (r + d) % MOD
                    if j + 1 < n:
                        right[i][j + 1] = (right[i][j + 1] + tot) % MOD
                    if i + 1 < m:
                        down[i + 1][j] = (down[i + 1][j] + tot) % MOD
                else:
                    if i + 1 < m:
                        down[i + 1][j] = (down[i + 1][j] + r) % MOD
                    if j + 1 < n:
                        right[i][j + 1] = (right[i][j + 1] + d) % MOD

        return (right[m - 1][n - 1] + down[m - 1][n - 1]) % MOD