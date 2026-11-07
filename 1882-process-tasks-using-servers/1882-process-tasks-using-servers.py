import heapq
from typing import List

class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        idle = [(w, i) for i, w in enumerate(servers)]
        heapq.heapify(idle)
        busy = []
        ans = []
        time = 0

        for j, duration in enumerate(tasks):
            time = max(time, j)

            while busy and busy[0][0] <= time:
                _, w, i = heapq.heappop(busy)
                heapq.heappush(idle, (w, i))

            if not idle:
                time = busy[0][0]
                while busy and busy[0][0] <= time:
                    _, w, i = heapq.heappop(busy)
                    heapq.heappush(idle, (w, i))

            w, i = heapq.heappop(idle)
            ans.append(i)
            heapq.heappush(busy, (time + duration, w, i))

        return ans