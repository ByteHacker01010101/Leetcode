class Solution:
    def maxSubarrayLength(self, nums: list[int], k: int) -> int:
        count = {}
        left = 0
        best = 0

        for right, val in enumerate(nums):
            count[val] = count.get(val, 0) + 1

            while count[val] > k:
                left_val = nums[left]
                count[left_val] -= 1
                left += 1

            best = max(best, right - left + 1)

        return best