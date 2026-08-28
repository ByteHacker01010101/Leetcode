class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - 97] += 1

        odd = [i for i in range(26) if cnt[i] % 2 == 1]
        if n % 2 == 0:
            if odd:
                return ""
            mid_char = None
        else:
            if len(odd) != 1:
                return ""
            mid_char = odd[0]

        half = n // 2
        pool = [cnt[i] // 2 for i in range(26)]
        t = [ord(ch) - 97 for ch in target]

        def smallest_greater(arr, x):
            for c in range(x + 1, 26):
                if arr[c] > 0:
                    return c
            return -1

        pool_work = pool[:]
        fallback_pos = -1
        fallback_char = -1
        fallback_snapshot = None
        tie_ok = True

        for j in range(half):
            tc = t[j]
            g = smallest_greater(pool_work, tc)
            if g != -1:
                fallback_pos, fallback_char = j, g
                fallback_snapshot = pool_work[:]
            if pool_work[tc] > 0:
                pool_work[tc] -= 1
            else:
                tie_ok = False
                break

        result = None

        if tie_ok:
            first_half = t[:half]
            suffix = ([mid_char] if mid_char is not None else []) + list(reversed(first_half))
            target_suffix = t[half:]
            if suffix > target_suffix:
                result = first_half + ([mid_char] if mid_char is not None else []) + list(reversed(first_half))

        if result is None:
            if fallback_pos == -1:
                return ""
            pool2 = fallback_snapshot[:]
            pool2[fallback_char] -= 1
            first_half = t[:fallback_pos] + [fallback_char]
            for c in range(26):
                first_half.extend([c] * pool2[c])
            result = first_half + ([mid_char] if mid_char is not None else []) + list(reversed(first_half))

        return ''.join(chr(97 + i) for i in result)