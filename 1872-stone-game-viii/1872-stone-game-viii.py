class Solution:
    def stoneGameVIII(self, stones: list[int]) -> int:
        n = len(stones)
        pre = list(itertools.accumulate(stones))  
        
        best = pre[-1]         
        for i in range(n - 2, 0, -1):
            best = max(best, pre[i] - best)
        return best