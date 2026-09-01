from collections import deque

class Solution:
    def minMoves(self, classroom: list[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        grid = classroom

        start = None
        litter_index = {}
        for i in range(m):
            for j in range(n):
                c = grid[i][j]
                if c == 'S':
                    start = (i, j)
                elif c == 'L':
                    litter_index[(i, j)] = len(litter_index)

        L = len(litter_index)
        full_mask = (1 << L) - 1
        if L == 0:
            return 0

        sr, sc = start
    
        visited = [[[[False] * (1 << L) for _ in range(energy + 1)]
                    for _ in range(n)] for _ in range(m)]
        visited[sr][sc][energy][0] = True

        q = deque([(sr, sc, energy, 0, 0)])  
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while q:
            r, c, e, mask, dist = q.popleft()
            if mask == full_mask:
                return dist
            if e == 0:
                continue
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] != 'X':
                    cell = grid[nr][nc]
                    ne = energy if cell == 'R' else e - 1
                    nmask = mask
                    if cell == 'L' and (nr, nc) in litter_index:
                        nmask |= (1 << litter_index[(nr, nc)])
                    if not visited[nr][nc][ne][nmask]:
                        visited[nr][nc][ne][nmask] = True
                        q.append((nr, nc, ne, nmask, dist + 1))

        return -1