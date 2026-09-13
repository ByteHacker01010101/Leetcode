from collections import Counter
from typing import List

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        onesA = [(x, y) for x in range(n) for y in range(n) if img1[x][y] == 1]
        onesB = [(x, y) for x in range(n) for y in range(n) if img2[x][y] == 1]

        if not onesA or not onesB:
            return 0

        shift_counts = Counter()
        for x1, y1 in onesA:
            for x2, y2 in onesB:
                shift_counts[(x2 - x1, y2 - y1)] += 1

        return max(shift_counts.values())