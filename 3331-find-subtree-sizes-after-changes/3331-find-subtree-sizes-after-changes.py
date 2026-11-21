class Solution:
    def findSubtreeSizes(self, parent: list[int], s: str) -> list[int]:
        n = len(s)
        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[parent[i]].append(i)

        new_parent = parent[:]
        last = [-1] * 26
        saved = [-1] * n
        order = []

        stack = [0]
        while stack:
            u = stack.pop()
            if u >= 0:  
                c = ord(s[u]) - 97
                if u and last[c] != -1:
                    new_parent[u] = last[c]
                saved[u] = last[c]
                last[c] = u
                order.append(u)
                stack.append(~u)  
                stack.extend(children[u])
            else: 
                u = ~u
                last[ord(s[u]) - 97] = saved[u]

        ans = [1] * n
        for u in reversed(order):
            if u:
                ans[new_parent[u]] += ans[u]
        return ans