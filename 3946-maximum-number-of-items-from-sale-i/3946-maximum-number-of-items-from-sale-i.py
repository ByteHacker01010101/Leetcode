from math import inf

class Solution:
    def maximumSaleItems(self, items: list[list[int]], budget: int) -> int:
        f = [0] * (budget + 1)
        mn = inf

        for factor, price in items:
            mn = min(mn, price)
            cnt = sum(other % factor == 0 for other, _ in items)

            for j in range(budget, price - 1, -1):
                f[j] = max(f[j], f[j - price] + cnt)

        return max(x + (budget - i) // mn for i, x in enumerate(f))