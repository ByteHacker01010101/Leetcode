from bisect import bisect_left

class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        arr2.sort()
        count = 0

        for x in arr1:
            i = bisect_left(arr2, x - d)
            if i == len(arr2) or arr2[i] > x + d:
                count += 1

        return count