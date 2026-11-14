from typing import List

class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        ans = float("inf")

        for i in range(n):
            for length in range(l, r + 1):
                end = i + length
                if end > n:
                    break
                s = prefix[end] - prefix[i]
                if s > 0:
                    ans = min(ans, s)

        return ans if ans != float("inf") else -1