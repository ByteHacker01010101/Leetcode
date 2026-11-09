import heapq

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        free = list(range(k))         
        busy = []                      
        cnt = [0] * k

        for i, (t, l) in enumerate(zip(arrival, load)):
            
            while busy and busy[0][0] <= t:
                _, sid = heapq.heappop(busy)
                heapq.heappush(free, i + (sid - i) % k)

           
            while free and free[0] < i:
                j = heapq.heappop(free)
                j += ((i - j + k - 1) // k) * k
                heapq.heappush(free, j)

          
            if free:
                sid = heapq.heappop(free) % k
                cnt[sid] += 1
                heapq.heappush(busy, (t + l, sid))

        best = max(cnt)
        return [s for s, c in enumerate(cnt) if c == best]