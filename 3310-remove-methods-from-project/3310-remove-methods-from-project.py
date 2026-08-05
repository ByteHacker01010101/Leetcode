from collections import deque

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: list[list[int]]) -> list[int]:
        adj = [[] for _ in range(n)]
        for a, b in invocations:
            adj[a].append(b)

        suspicious = [False] * n
        suspicious[k] = True
        queue = deque([k])
        while queue:
            node = queue.popleft()
            for nxt in adj[node]:
                if not suspicious[nxt]:
                    suspicious[nxt] = True
                    queue.append(nxt)

        for a, b in invocations:
            if not suspicious[a] and suspicious[b]:
                return list(range(n))  

        return [i for i in range(n) if not suspicious[i]]