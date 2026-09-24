class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        def digitSum(n: int) -> int:
            total = 0
            while n > 0:
                total += n % 10
                n //= 10
            return total
        for i, num in enumerate(nums):
            if digitSum(num) == i:
                return i
        return -1
        