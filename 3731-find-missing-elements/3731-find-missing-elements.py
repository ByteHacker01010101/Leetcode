class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        lo, hi = min(nums), max(nums)
        present = set(nums)

        missing = []
        for x in range (lo, hi + 1):
            if x not in present:
                missing.append(x)
        
        return missing 
        