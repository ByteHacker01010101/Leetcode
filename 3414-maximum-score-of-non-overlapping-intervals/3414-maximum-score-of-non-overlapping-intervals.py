import bisect
from typing import List

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        order = sorted(range(n), key=lambda i: intervals[i][1])
        sl = [intervals[i][0] for i in order]
        sr = [intervals[i][1] for i in order]
        sw = [intervals[i][2] for i in order]
        dp = [[(0, ()) for _ in range(5)] for _ in range(n + 1)]
        def better(a, b):
            if a[0] != b[0]:
                return a if a[0] > b[0] else b
            return a if a[1] <= b[1] else b
        for i in range(1, n + 1):
            idx = order[i - 1]
            l, r, w = sl[i - 1], sr[i - 1], sw[i - 1]
            j = bisect.bisect_left(sr, l, 0, i - 1)
            for k in range(1, 5):
                skip = dp[i - 1][k]
                prev_score, prev_idx = dp[j][k - 1]
                take = (prev_score + w, tuple(sorted(prev_idx + (idx,))))
                dp[i][k] = better(skip, take)

        return list(dp[n][4][1])