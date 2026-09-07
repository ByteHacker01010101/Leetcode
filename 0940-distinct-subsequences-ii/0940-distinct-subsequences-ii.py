class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        total = 0
        ends_with = {}  

        for c in s:
            new_val = (total + 1) % MOD
            total = (total - ends_with.get(c, 0) + new_val) % MOD
            ends_with[c] = new_val

        return total % MOD