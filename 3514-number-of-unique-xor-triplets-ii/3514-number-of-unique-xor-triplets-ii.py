from typing import List

class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        MAX_BIT = 2048  

        values = list(set(nums))  
        n = len(values)

        
        pair_xor = [False] * MAX_BIT
        for i in range(n):
            vi = values[i]
            for j in range(i, n):
                pair_xor[vi ^ values[j]] = True

        
        result = [False] * MAX_BIT
        for p in range(MAX_BIT):
            if pair_xor[p]:
                for c in values:
                    result[p ^ c] = True

        return sum(result)