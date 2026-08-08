class Solution:
    def validSequence(self, word1: str, word2: str) -> list[int]:
        n1, n2 = len(word1), len(word2)
        suf = [0] * (n1 + 1)
        j = n2 - 1
        for i in range(n1 - 1, -1, -1):
            if j >= 0 and word1[i] == word2[j]:
                j -= 1
            suf[i] = n2 - 1 - j

        result = []
        k = 0
        used_change = False

        for i in range(n1):
            if k == n2:
                break
            if word1[i] == word2[k]:
                result.append(i)
                k += 1
            elif not used_change and suf[i + 1] >= n2 - (k + 1):
                result.append(i)
                k += 1
                used_change = True

        return result if k == n2 else []