class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)

        pre = [0] * n
        for i in range(n - 1):
            pre[i + 1] = pre[i] + (nums[i] > nums[i + 1])

        ans = 0
        for k in range(1, n + 1):
            if n % k:
                continue

            prev_max = 0
            ok = True
            for l in range(0, n, k):
                r = l + k - 1

                if pre[r] - pre[l] + (nums[r] > nums[l]) > 1:
                    ok = False
                    break

                block = nums[l:r + 1]
                if min(block) < prev_max:
                    ok = False
                    break
                prev_max = max(block)

            if ok:
                ans += k

        return ans