from typing import List

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        mn = min(p for _, p in items)

        freq = [0] * (n + 1)
        for f, _ in items:
            freq[f] += 1

        mult = [0] * (n + 1)
        for f in range(1, n + 1):
            if freq[f]:
                mult[f] = sum(freq[f::f])

        deals = []
        for f, p in items:
            e = mult[f] - 1
            if e > 0 and p <= 2 * mn:
                deals.append((p, e))
        deals.sort()

        ans = 0
        for p, e in deals:
            k = min(e, budget // p)
            ans += 2 * k
            budget -= k * p
            if k < e:
                break

        return ans + budget // mn