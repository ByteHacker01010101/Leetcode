from sortedcontainers import SortedList

class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: list[int]) -> list[int]:
        s = list(s)
        n = len(s)

        starts = SortedList()      
        run_length = {}            
        lengths = SortedList()     

        def add_run(start, length):
            starts.add(start)
            run_length[start] = length
            lengths.add(length)

        def remove_run(start):
            length = run_length.pop(start)
            starts.remove(start)
            lengths.remove(length)
            return length

        def run_at(pos):
            
            i = starts.bisect_right(pos) - 1
            start = starts[i]
            return start, run_length[start]

        
        i = 0
        while i < n:
            j = i
            while j + 1 < n and s[j + 1] == s[i]:
                j += 1
            add_run(i, j - i + 1)
            i = j + 1

        ans = []
        for idx, c in zip(queryIndices, queryCharacters):
            if s[idx] == c:
                ans.append(lengths[-1])
                continue

            r_start, r_len = run_at(idx)
            r_end = r_start + r_len - 1
            remove_run(r_start)

            s[idx] = c

            if idx > r_start:                         
                add_run(r_start, idx - r_start)
            if idx < r_end:                           
                add_run(idx + 1, r_end - idx)
            add_run(idx, 1)                             

            cur_start, cur_len = idx, 1

            if idx - 1 >= 0:
                l_start, l_len = run_at(idx - 1)
                if s[l_start] == c:
                    remove_run(l_start)
                    remove_run(cur_start)
                    cur_start, cur_len = l_start, l_len + cur_len
                    add_run(cur_start, cur_len)

            if idx + 1 < n:
                r_start2, r_len2 = run_at(idx + 1)
                if s[r_start2] == c:
                    remove_run(r_start2)
                    remove_run(cur_start)
                    cur_len = cur_len + r_len2
                    add_run(cur_start, cur_len)

            ans.append(lengths[-1])

        return ans