class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)
        best = ""
        left = 0
        ones = 0

        for right in range(n):
            if s[right] == '1':
                ones += 1

            while ones == k:
                while s[left] == '0':
                    left += 1

                candidate = s[left:right + 1]
                if best == "" or len(candidate) < len(best) or \
                   (len(candidate) == len(best) and candidate < best):
                    best = candidate

                ones -= 1
                left += 1

        return best