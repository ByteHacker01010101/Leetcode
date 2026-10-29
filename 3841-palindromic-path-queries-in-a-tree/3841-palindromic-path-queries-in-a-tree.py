class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        LOG = max(1, n.bit_length())
        up = [[0] * n for _ in range(LOG)]
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        base = [0] * n
        chars = [ord(c) - 97 for c in s]

        # iterative DFS for Euler tour
        timer = 0
        base[0] = 1 << chars[0]
        stack = [(0, 0, 0)]  # (node, parent, next-child-index)
        tin[0] = timer
        timer += 1
        while stack:
            node, par, idx = stack.pop()
            if idx < len(adj[node]):
                stack.append((node, par, idx + 1))
                nxt = adj[node][idx]
                if nxt != par:
                    up[0][nxt] = node
                    depth[nxt] = depth[node] + 1
                    base[nxt] = base[node] ^ (1 << chars[nxt])
                    tin[nxt] = timer
                    timer += 1
                    stack.append((nxt, node, 0))
            else:
                tout[node] = timer - 1

        for j in range(1, LOG):
            prev, cur = up[j - 1], up[j]
            for v in range(n):
                cur[v] = prev[prev[v]]

        def lca(a: int, b: int) -> int:
            if depth[a] < depth[b]:
                a, b = b, a
            diff = depth[a] - depth[b]
            for j in range(LOG):
                if (diff >> j) & 1:
                    a = up[j][a]
            if a == b:
                return a
            for j in range(LOG - 1, -1, -1):
                if up[j][a] != up[j][b]:
                    a = up[j][a]
                    b = up[j][b]
            return up[0][a]

        # Fenwick tree: range XOR update, point query
        size = n + 2
        tree = [0] * (size + 1)

        def add(i: int, val: int) -> None:
            i += 1
            while i <= size:
                tree[i] ^= val
                i += i & -i

        def prefix(i: int) -> int:
            i += 1
            res = 0
            while i > 0:
                res ^= tree[i]
                i -= i & -i
            return res

        def pref_mask(x: int) -> int:
            return base[x] ^ prefix(tin[x])

        ans: list[bool] = []
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                u, c = int(parts[1]), ord(parts[2]) - 97
                if chars[u] != c:
                    delta = (1 << chars[u]) ^ (1 << c)
                    add(tin[u], delta)
                    add(tout[u] + 1, delta)
                    chars[u] = c
            else:
                u, v = int(parts[1]), int(parts[2])
                l = lca(u, v)
                mask = pref_mask(u) ^ pref_mask(v) ^ (1 << chars[l])
                ans.append(mask & (mask - 1) == 0)
        return ans