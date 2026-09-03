class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        min_odd = min_even = None
        has_odd = False
        for x in nums1:
            if x % 2 == 1:
                has_odd = True
                if min_odd is None or x < min_odd:
                    min_odd = x
            else:
                if min_even is None or x < min_even:
                    min_even = x

        can_even = not has_odd
        can_odd = has_odd and (min_even is None or min_odd < min_even)
        return can_even or can_odd