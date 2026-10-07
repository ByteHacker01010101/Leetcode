class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        left_rem = right_rem = 0
        for ch in s:
            if ch == '(':
                left_rem += 1
            elif ch == ')':
                if left_rem > 0:
                    left_rem -= 1
                else:
                    right_rem += 1

        n = len(s)
        res: list[str] = []
        path: list[str] = []

        def dfs(i: int, l: int, r: int, open_cnt: int) -> None:
            if i == n:
                if l == 0 and r == 0 and open_cnt == 0:
                    res.append("".join(path))
                return

            ch = s[i]
            if ch != '(' and ch != ')':
                path.append(ch)
                dfs(i + 1, l, r, open_cnt)
                path.pop()
                return

            j = i
            while j < n and s[j] == ch:
                j += 1
            run = j - i

            for remove in range(run + 1):
                keep = run - remove
                if ch == '(':
                    if remove > l:
                        break
                    nl, nr, nopen = l - remove, r, open_cnt + keep
                else:
                    if remove > r:
                        break
                    if keep > open_cnt:
                        continue
                    nl, nr, nopen = l, r - remove, open_cnt - keep

                path.extend(ch * keep)
                dfs(j, nl, nr, nopen)
                if keep:
                    del path[-keep:]

        dfs(0, left_rem, right_rem, 0)
        return res