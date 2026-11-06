class Solution:
    def countServers(self, n: int, logs: list[list[int]], x: int, queries: list[int]) -> list[int]:
        logs.sort(key=lambda log: log[1])
        order = sorted(range(len(queries)), key=lambda i: queries[i])

        cnt = [0] * (n + 1)
        active = 0
        l = r = 0
        ans = [0] * len(queries)

        for qi in order:
            q = queries[qi]

            while r < len(logs) and logs[r][1] <= q:
                server = logs[r][0]
                if cnt[server] == 0:
                    active += 1
                cnt[server] += 1
                r += 1

            while l < r and logs[l][1] < q - x:
                server = logs[l][0]
                cnt[server] -= 1
                if cnt[server] == 0:
                    active -= 1
                l += 1

            ans[qi] = n - active

        return ans