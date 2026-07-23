class Solution:
    def uniqueXorTriplets(self, nums: list[int]) -> int:
        n = len(nums)
        if n < 3:
            return n

        m = n.bit_length() - 1  
        return 1 << (m + 1)