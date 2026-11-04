class Solution:
    def minOperations(self, nums: list[int], x: int, k: int) -> int:
        n = len(nums)
        vals = sorted(set(nums))
        idx = {v: i + 1 for i, v in enumerate(vals)}
        m = len(vals)
        LOG = m.bit_length()
        cnt = [0] * (m + 1)
        sm = [0] * (m + 1)

        def update(v: int, c: int) -> None:
            i = idx[v]
            while i <= m:
                cnt[i] += c
                sm[i] += c * v
                i += i & -i

        def kth(kk: int):
            pos = c = s = 0
            for b in range(LOG, -1, -1):
                nxt = pos + (1 << b)
                if nxt <= m and c + cnt[nxt] < kk:
                    pos = nxt
                    c += cnt[nxt]
                    s += sm[nxt]
            return vals[pos], c, s  
        cost = []
        total = 0
        kk = (x + 1) // 2
        for r in range(n):
            update(nums[r], 1)
            total += nums[r]
            if r >= x:
                update(nums[r - x], -1)
                total -= nums[r - x]
            if r >= x - 1:
                med, c, s = kth(kk)
                sum_le = s + med * (kk - c)
                cost.append(med * kk - sum_le + (total - sum_le) - med * (x - kk))

        INF = float("inf")
        prev = [0] * (n + 1)  # j = 0
        for j in range(1, k + 1):
            cur = [INF] * (n + 1)
            for i in range(j * x, n + 1):
                cur[i] = min(cur[i - 1], prev[i - x] + cost[i - x])
            prev = cur
        return prev[n]