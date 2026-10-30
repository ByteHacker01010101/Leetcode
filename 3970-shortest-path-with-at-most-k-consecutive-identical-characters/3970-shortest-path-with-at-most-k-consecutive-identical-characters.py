import heapq

class Solution:
    def shortestPath(self, n: int, edges: list[list[int]], labels: str, k: int) -> int:
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))

        K = k + 1
        INF = float('inf')
        dist = [INF] * (n * K)

        dist[0 * K + 1] = 0
        heap = [(0, 0, 1)]  # (cost, node, run)

        while heap:
            cost, u, run = heapq.heappop(heap)

            if cost > dist[u * K + run]:
                continue
            if u == n - 1:
                return cost

            for v, w in graph[u]:
                nr = run + 1 if labels[v] == labels[u] else 1
                if nr > k:
                    continue
                nc = cost + w
                idx = v * K + nr
                if nc < dist[idx]:
                    dist[idx] = nc
                    heapq.heappush(heap, (nc, v, nr))

        return -1