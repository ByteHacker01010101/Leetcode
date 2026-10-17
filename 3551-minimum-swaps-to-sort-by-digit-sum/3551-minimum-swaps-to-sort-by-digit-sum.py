class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        def digit_sum(x: int) -> int:
            s = 0
            while x:
                s += x % 10
                x //= 10
            return s

        n = len(nums)
        order = sorted((digit_sum(v), v, i) for i, v in enumerate(nums))
        target = [0] * n
        for pos, (_, _, orig) in enumerate(order):
            target[orig] = pos

        visited = [False] * n
        swaps = 0

        for i in range(n):
            if visited[i] or target[i] == i:
                continue
            length = 0
            j = i
            while not visited[j]:
                visited[j] = True
                j = target[j]
                length += 1
            swaps += length - 1

        return swaps