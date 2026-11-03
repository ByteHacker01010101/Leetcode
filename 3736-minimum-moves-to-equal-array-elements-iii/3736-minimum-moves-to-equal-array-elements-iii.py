class Solution:
    def minMoves(self, nums: list[int]) -> int:
        mx = max(nums)
        return mx * len(nums) - sum(nums)