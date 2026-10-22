from math import inf

class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)
        z = nums.index(0)

        def ok(step: int) -> bool:
            for i in range(1, n):
                if nums[(z + i * step) % n] != i:
                    return False
            return True

        ans = inf
        if ok(1):
            ans = min(ans, z, n - z + 2)
        if ok(-1):
            ans = min(ans, n - z, z + 2)

        return -1 if ans == inf else ans