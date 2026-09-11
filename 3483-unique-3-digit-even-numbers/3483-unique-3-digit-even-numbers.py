from typing import List
from collections import Counter

class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        count = Counter(digits)
        result = 0

        for hundreds in range(1, 10):       # no leading zero
            for tens in range(0, 10):
                for units in range(0, 10, 2):  # even → last digit 0,2,4,6,8
                    need = Counter([hundreds, tens, units])
                    # check we have enough of each digit
                    if all(count[d] >= need[d] for d in need):
                        result += 1

        return result