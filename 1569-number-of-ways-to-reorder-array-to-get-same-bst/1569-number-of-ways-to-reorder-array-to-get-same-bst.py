from math import comb

class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        MOD = 10**9 + 7

        def ways(arr: list[int]) -> int:
            if len(arr) <= 2:
                return 1

            root = arr[0]
            left = [x for x in arr if x < root]
            right = [x for x in arr if x > root]

            return (
                comb(len(left) + len(right), len(left))
                * ways(left)
                * ways(right)
            ) % MOD

        return (ways(nums) - 1) % MOD