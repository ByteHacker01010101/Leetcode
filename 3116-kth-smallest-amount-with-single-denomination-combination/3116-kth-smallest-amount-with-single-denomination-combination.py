from math import gcd
from typing import List

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        n = len(coins)

        def count(x: int) -> int:
            total = 0
           
            for mask in range(1, 1 << n):
                lcm = 1
                bits = 0
                for i in range(n):
                    if mask & (1 << i):
                        bits += 1
                        lcm = lcm * coins[i] // gcd(lcm, coins[i])
                        if lcm > x:
                            break
                if lcm > x:
                    continue
                if bits % 2 == 1:
                    total += x // lcm
                else:
                    total -= x // lcm
            return total

        lo, hi = 1, min(coins) * k
        while lo < hi:
            mid = (lo + hi) // 2
            if count(mid) >= k:
                hi = mid
            else:
                lo = mid + 1
        return lo