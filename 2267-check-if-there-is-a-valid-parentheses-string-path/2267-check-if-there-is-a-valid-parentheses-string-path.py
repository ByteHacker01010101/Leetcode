class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])

        if (m + n - 1) % 2 == 1:
            return False
        if grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False

        visited = set()

        def dfs(i: int, j: int, bal: int) -> bool:
            bal += 1 if grid[i][j] == '(' else -1

            if bal < 0 or bal > (m - i - 1) + (n - j - 1):
                return False

            if i == m - 1 and j == n - 1:
                return bal == 0

            if (i, j, bal) in visited:
                return False
            visited.add((i, j, bal))

            if i + 1 < m and dfs(i + 1, j, bal):
                return True
            if j + 1 < n and dfs(i, j + 1, bal):
                return True
            return False

        return dfs(0, 0, 0)