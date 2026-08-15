class Solution:
    def longestSubsequence(self, nums: list[int]) -> int:
        n = len(nums)
        total = 0
        has_nonzero = False

        for num in nums:
            total ^= num
            if num != 0:
                has_nonzero = True

        if total != 0:
            return n
        if has_nonzero:
            return n - 1
        return 0