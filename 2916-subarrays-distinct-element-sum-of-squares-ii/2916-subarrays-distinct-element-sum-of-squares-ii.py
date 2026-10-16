class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        b1 = [0] * (n + 2)
        b2 = [0] * (n + 2)

        def upd(t, i, v):
            while i <= n + 1:
                t[i] += v
                i += i & -i

        def qry(t, i):
            s = 0
            while i > 0:
                s += t[i]
                i -= i & -i
            return s

        def prefix(i):
            return qry(b1, i) * i - qry(b2, i)

        def range_add(l, r):
            upd(b1, l, 1)
            upd(b1, r + 1, -1)
            upd(b2, l, l - 1)
            upd(b2, r + 1, -r)

        last = {}
        f = 0
        ans = 0
        for j, x in enumerate(nums, 1):
            p = last.get(x, 0)
            S = prefix(j - 1) - prefix(p)
            f = (f + 2 * S + (j - p)) % MOD
            ans = (ans + f) % MOD
            range_add(p + 1, j)
            last[x] = j

        return ans