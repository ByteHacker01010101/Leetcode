class Solution:
    def countCommas(self, n: int) -> int:
        total = 0
        d = 1
        while True:
            lo = 1 if d == 1 else 10 ** (d - 1)
            if lo > n:
                break
            hi = min(10 ** d - 1, n)
            count = hi - lo + 1
            commas_per_number = (d - 1) // 3
            total += count * commas_per_number
            d += 1
        return total