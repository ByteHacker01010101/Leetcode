class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2
        left, right = num[:half], num[half:]

        leftSum = leftQ = 0
        for ch in left:
            if ch == '?':
                leftQ += 1
            else:
                leftSum += int(ch)

        rightSum = rightQ = 0
        for ch in right:
            if ch == '?':
                rightQ += 1
            else:
                rightSum += int(ch)

        diff = leftSum - rightSum
        totalQ = leftQ + rightQ

        if totalQ % 2 == 1:
            return True 

        return 2 * diff + 9 * (leftQ - rightQ) != 0