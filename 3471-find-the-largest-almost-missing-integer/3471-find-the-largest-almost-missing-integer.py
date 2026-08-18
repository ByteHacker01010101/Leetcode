class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        best = -1

        for x in set(nums):
            count = 0
            for start in range(n - k + 1):
                if x in nums[start:start + k]:
                    count += 1
                    if count > 1:
                        break
            if count == 1:
                best = max(best, x)
        return best
        
        