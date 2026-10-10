class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        k = k1 + k2
        diffs = [abs(a - b) for a, b in zip(nums1, nums2)]
        max_d = max(diffs)
        cnt = [0] * (max_d + 1)
        for d in diffs:
            cnt[d] += 1

        for v in range(max_d, 0, -1):
            if cnt[v] == 0:
                continue
            if k >= cnt[v]:
                k -= cnt[v]
                cnt[v - 1] += cnt[v]
                cnt[v] = 0
            else:
                cnt[v] -= k
                cnt[v - 1] += k
                k = 0
                break

        return sum(c * v * v for v, c in enumerate(cnt))