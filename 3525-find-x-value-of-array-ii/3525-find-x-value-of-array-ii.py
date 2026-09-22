from typing import List

class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        K = k
        KK = K * K

        def leaf_matrix(v):
            m = [0] * KK
            for s in range(K):
                m[s * K + (s * v) % K] = 1
            return m

        def combine(pA, cntA, pB, cntB):
            p = (pA * pB) % K
            out = [0] * KK
            for s in range(K):
                shifted = (s * pA) % K
                baseA = s * K
                baseB = shifted * K
                for r in range(K):
                    out[baseA + r] = cntA[baseA + r] + cntB[baseB + r]
            return p, out

        tree_P = [0] * (2 * n)
        tree_cnt = [None] * (2 * n)

        for i in range(n):
            v = nums[i] % K
            tree_P[n + i] = v
            tree_cnt[n + i] = leaf_matrix(v)

        for i in range(n - 1, 0, -1):
            p, m = combine(tree_P[2*i], tree_cnt[2*i], tree_P[2*i+1], tree_cnt[2*i+1])
            tree_P[i], tree_cnt[i] = p, m

        def update(idx, val):
            i = idx + n
            v = val % K
            tree_P[i] = v
            tree_cnt[i] = leaf_matrix(v)
            i >>= 1
            while i >= 1:
                p, m = combine(tree_P[2*i], tree_cnt[2*i], tree_P[2*i+1], tree_cnt[2*i+1])
                tree_P[i], tree_cnt[i] = p, m
                i >>= 1

        IDENTITY_CNT = [0] * KK

        def query(l, r):  
            lP, lC = 1, IDENTITY_CNT
            rP, rC = 1, IDENTITY_CNT
            l += n
            r += n
            while l < r:
                if l & 1:
                    lP, lC = combine(lP, lC, tree_P[l], tree_cnt[l])
                    l += 1
                if r & 1:
                    r -= 1
                    rP, rC = combine(tree_P[r], tree_cnt[r], rP, rC)
                l >>= 1
                r >>= 1
            _, finalC = combine(lP, lC, rP, rC)
            return finalC

        IDENTITY = 1 % K
        result = []
        for idx, val, start, x in queries:
            update(idx, val)
            m = query(start, n)
            result.append(m[IDENTITY * K + x])
        return result