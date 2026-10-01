class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2:
            return False

        pairs = {')': '(', ']': '[', '}': '{'}
        stack = []

        for ch in s:
            if ch in pairs:
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)

        return not stack