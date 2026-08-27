from collections import Counter
import string

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        cnt = Counter(s)

        snapshots = [cnt.copy()]
        cw = cnt.copy()
        max_prefix = 0
        for i in range(n):
            c = target[i]
            if cw[c] > 0:
                cw[c] -= 1
                max_prefix += 1
                snapshots.append(cw.copy())
            else:
                break

        start = min(max_prefix, n - 1)
        for i in range(start, -1, -1):
            avail = snapshots[i]
            best_c = None
            for c in string.ascii_lowercase:
                if c > target[i] and avail.get(c, 0) > 0:
                    best_c = c
                    break
            if best_c is not None:
                remaining = avail.copy()
                remaining[best_c] -= 1
                rest = []
                for c in string.ascii_lowercase:
                    rest.extend([c] * remaining.get(c, 0))
                return target[:i] + best_c + ''.join(rest)

        return ""