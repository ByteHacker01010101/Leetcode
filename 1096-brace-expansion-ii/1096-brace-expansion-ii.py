from typing import List

class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        def merge(a: set, b: set) -> set:
           
            if not a:
                return set(b)
            if not b:
                return set(a)
            return {x + y for x in a for y in b}

        stack = [[set()]]  

        for ch in expression:
            if ch == '{':
                stack.append([set()])
            elif ch == '}':
                group = stack.pop()
                union_set = set()
                for term in group:
                    union_set |= term
                stack[-1][-1] = merge(stack[-1][-1], union_set)
            elif ch == ',':
                stack[-1].append(set())
            else:  
                stack[-1][-1] = merge(stack[-1][-1], {ch})

        result = set()
        for term in stack[0]:
            result |= term
        return sorted(result)