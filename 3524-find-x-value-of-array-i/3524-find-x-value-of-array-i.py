class Solution:
    def resultArray(self, nums: list[int], k: int) -> list[int]:
        result = [0] * k
        prev = [0] * k 

        for num in nums:
            r = num % k
            curr = [0] * k
            for pr in range(k):
                if prev[pr]:
                    curr[(pr * r) % k] += prev[pr]
            curr[r] += 1  

            for x in range(k):
                result[x] += curr[x]

            prev = curr

        return result