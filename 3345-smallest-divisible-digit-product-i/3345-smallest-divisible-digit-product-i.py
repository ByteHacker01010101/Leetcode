class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def digit_product(x: int) -> int:
            p = 1
            for ch in str(x):
                p *= int(ch)
            return p

        num = n
        while digit_product(num) % t != 0:
            num += 1
        return num