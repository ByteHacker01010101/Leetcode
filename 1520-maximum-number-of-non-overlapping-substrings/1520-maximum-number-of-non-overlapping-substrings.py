class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        n = len(s)
        first = {}
        last = {}
        for i, c in enumerate(s):
            if c not in first:
                first[c] = i
            last[c] = i

        intervals = {}
        for c, start in first.items():
            end = last[c]
            j = start
            valid = True
            while j <= end:
                cj = s[j]
                if first[cj] < start:
                    valid = False
                    break
                end = max(end, last[cj])
                j += 1
            if valid:
                intervals[start] = end

        
        best_count = [0] * (n + 1)
        best_len = [0] * (n + 1)
        take = [False] * (n + 1)
        end_at = [-1] * (n + 1)

        for i in range(n - 1, -1, -1):
            best_count[i] = best_count[i + 1]
            best_len[i] = best_len[i + 1]
            take[i] = False

            if i in intervals:
                e = intervals[i]
                cnt = 1 + best_count[e + 1]
                length = (e - i + 1) + best_len[e + 1]
                if cnt > best_count[i] or (cnt == best_count[i] and length < best_len[i]):
                    best_count[i] = cnt
                    best_len[i] = length
                    take[i] = True
                    end_at[i] = e

        
        result = []
        i = 0
        while i < n:
            if take[i]:
                e = end_at[i]
                result.append(s[i:e + 1])
                i = e + 1
            else:
                i += 1
        return result