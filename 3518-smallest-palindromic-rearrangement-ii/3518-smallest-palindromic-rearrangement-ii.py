import math
from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        n = len(s)
        freq = Counter(s)

        middle_char = ''
        half_freq = {}
        for c, cnt in freq.items():
            if cnt % 2 == 1:
                middle_char = c
            half_freq[c] = cnt // 2

        L = n // 2

        def count_perms(counts: dict, cap: int) -> int:
            total = 0
            value = 1
            for c, cnt in counts.items():
                if cnt == 0:
                    continue
                total += cnt
                value *= math.comb(total, cnt)
                if value >= cap:
                    return cap
            return value

        if count_perms(half_freq, k) < k:
            return ""

        remaining_k = k
        half_result = []
        letters = sorted(half_freq.keys())

        for _ in range(L):
            for c in letters:
                if half_freq[c] == 0:
                    continue
                half_freq[c] -= 1
                cnt = count_perms(half_freq, remaining_k)
                if cnt >= remaining_k:
                    half_result.append(c)
                    break
                else:
                    remaining_k -= cnt
                    half_freq[c] += 1  

        half_str = ''.join(half_result)
        if middle_char:
            return half_str + middle_char + half_str[::-1]
        return half_str + half_str[::-1]