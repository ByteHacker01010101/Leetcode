class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        n = len(nums)
        total = nums[0]
        i = 1
        while i < n and nums[i] == nums[i - 1] + 1:
            total += nums[i]
            i += 1
        num_set = set(nums)
        x = total
        while x in num_set:
            x += 1
        
        return x