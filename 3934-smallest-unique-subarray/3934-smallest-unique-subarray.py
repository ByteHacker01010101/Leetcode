import random
from collections import Counter

class Solution:
    def smallestUniqueSubarray(self, nums: list[int]) -> int:
        n = len(nums)
        M = (1 << 61) - 1
        B = random.randrange(10**6, M - 1)

        h = [0] * (n + 1)
        pw = [1] * (n + 1)
        for i, x in enumerate(nums):
            h[i + 1] = (h[i] * B + x) % M
            pw[i + 1] = (pw[i] * B) % M

        def exists_unique(L: int) -> bool:
            cnt = Counter()
            for i in range(n - L + 1):
                cnt[(h[i + L] - h[i] * pw[L]) % M] += 1
            return any(c == 1 for c in cnt.values())

        lo, hi = 1, n
        while lo < hi:
            mid = (lo + hi) // 2
            if exists_unique(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo