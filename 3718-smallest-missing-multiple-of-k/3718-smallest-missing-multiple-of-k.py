class Solution:
    def missingMultiple(self, nums: list[int], k: int) -> int:
        seen = set(nums)
        multiple = k
        while multiple in seen:
            multiple += k
        return multiple