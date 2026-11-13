from collections import deque

class Solution:
    def countNonDecreasingSubarrays(self, nums: list[int], k: int) -> int:
        n = len(nums)
        ans = 0
        cost = 0
        dq = deque()          
        j = n - 1

        for i in range(n - 1, -1, -1):
            num = nums[i]
            cnt = 1

            while dq and dq[0][0] <= num:
                v, c = dq.popleft()
                cost += (num - v) * c
                cnt += c
            dq.appendleft((num, cnt))

            while cost > k:
                v, c = dq[-1]
                cost -= v - nums[j]
                if c == 1:
                    dq.pop()
                else:
                    dq[-1] = (v, c - 1)
                j -= 1

            ans += j - i + 1

        return ans