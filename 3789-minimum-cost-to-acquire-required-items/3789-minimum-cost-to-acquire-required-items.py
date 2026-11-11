class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        lo = min(need1, need2)
        hi = max(need1, need2)

        only_singles = need1 * cost1 + need2 * cost2
        both_then_singles = lo * costBoth + (need1 - lo) * cost1 + (need2 - lo) * cost2
        only_both = hi * costBoth

        return min(only_singles, both_then_singles, only_both)